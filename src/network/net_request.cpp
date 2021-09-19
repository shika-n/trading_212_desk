#include "net_request.h"

#include <algorithm>

#include <QNetworkReply>

#include "dns_over_https.h"

namespace trading_212_desk {

	NetRequest::NetRequest() {
		// Connect to handler
		connect(&net_manager, &QNetworkAccessManager::finished, this, &NetRequest::request_finished);
	}

	NetRequest::NetRequest(const char *url) {
		// Connect to handler
		connect(&net_manager, &QNetworkAccessManager::finished, this, &NetRequest::request_finished);

		set_url(url);
	}

	void NetRequest::set_url(const char *url) {
		// Convert the url to QUrl so that we can modify the url and queries later on
		qurl.setUrl(url);

		// Also set the newly set qurl to the request
		request.setUrl(qurl);

		// Duplicate query from the url, enabling us to add query to the existing query from the url
		query.setQuery(qurl.query());

		// Set unresolved host and Host header
		// Since this function is the only way of setting url this is fine
		unresolved_host = qurl.host();
		set_header("Host", unresolved_host);
	}

	void NetRequest::set_header(const char *key, const QString &value) {
		request.setRawHeader(key, value.toUtf8());
	}

	void NetRequest::set_query(const char *key, const QString &value) {
		// Removes and re-adds the query
		query.removeQueryItem(key);
		query.addQueryItem(key, value);
		// Set the query to the existing QUrl (overwrite)
		qurl.setQuery(query);
		// Set the new url with the new query
		request.setUrl(qurl);
	}

	void NetRequest::get(DnsOverHttps *doh) {
		if (doh != nullptr) {
			request.setPeerVerifyName(unresolved_host);

			auto connection = std::make_unique<QMetaObject::Connection>();
			auto connection_ptr = connection.get();
			*connection_ptr = (connect(doh, &DnsOverHttps::resolved, [this, connection = std::move(connection)](const QString &resolved_host) mutable -> void {
				std::unique_ptr<QMetaObject::Connection> _connection = std::move(connection);
				replace_host(resolved_host);
				net_manager.get(request);

				disconnect(*_connection);
			}));

			doh->resolve(unresolved_host);
			return;
		} else {
			request.setPeerVerifyName(nullptr);
		}
		net_manager.get(request);
	}

	void NetRequest::replace_host(const QString &resolved_host) {
		qurl.setHost(resolved_host);
		request.setUrl(qurl);
	}

	void NetRequest::request_finished(QNetworkReply *reply) {
		QString error_message;
		QByteArray result;

		if (reply->error()) {
			error_message = reply->errorString();
		} else {
			result = reply->readAll();
		}

		uint16_t status_code = reply->attribute(QNetworkRequest::Attribute::HttpStatusCodeAttribute).toUInt();
		emit finished(status_code, result, error_message);
	}

}