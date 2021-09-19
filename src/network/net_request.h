#pragma once

#include <memory>

#include <QNetworkAccessManager>
#include <QNetworkRequest>
#include <QUrlQuery>

class QNetworkReply;

namespace trading_212_desk {
	class DnsOverHttps;

	class NetRequest : public QObject {
		Q_OBJECT

	public:
		NetRequest();
		NetRequest(const char *url);

		void set_url(const char *url);

		void set_header(const char *key, const QString &value);
		void set_query(const char *key, const QString &value);

		// Send a GET request
		void get(DnsOverHttps *cloudflare_doh = nullptr);

	signals:
		// A simplified, ready to use response signal
		void finished(uint16_t status_code, const QByteArray &data, const QString &error_message);

	private:
		QString unresolved_host;

		QNetworkAccessManager net_manager;
		QNetworkRequest request;
		QUrl qurl;
		QUrlQuery query;

		void replace_host(const QString &resolved_host);

	private slots:
		void request_finished(QNetworkReply *reply);
	};
}