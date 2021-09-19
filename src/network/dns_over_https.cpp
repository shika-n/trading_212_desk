#include "dns_over_https.h"

#include <cstdint>

#include <QByteArray>
#include <QJsonArray>
#include <QJsonDocument>
#include <QString>

#include "dns_entry.h"

namespace trading_212_desk {

	DnsOverHttps::DnsOverHttps(DnsProvider dns_provider) {
		connect(&request, &NetRequest::finished, this, &DnsOverHttps::request_responded);

		if (dns_provider == DnsProvider::kCloudflare) {
			request.set_url("https://cloudflare-dns.com/dns-query?type=A&ct=application/dns-json");
		} else if (dns_provider == DnsProvider::kGoogle) {
			request.set_url("https://dns.google/resolve?type=A&ct=application/dns-json");
		}
	}

	void DnsOverHttps::resolve(const QString &host) {
		// Try to get entry from cache
		DnsEntry *entry_from_cache = resolve_from_cache(host);
		// If there is a good entry in cache, use it and return
		if (entry_from_cache != nullptr) {
			if (entry_from_cache->is_expired()) {
				qDebug() << entry_from_cache->get_name() << "is expired";
				// Request with the expired host
				send_doh_request(entry_from_cache->get_name());
			} else {
				emit resolved(entry_from_cache->get_data());
			}
			return;
		}

		// Request
		send_doh_request(host);

		// When send_doh_request finishes request_responded is called (see ctor)
	}

	DnsEntry *DnsOverHttps::resolve_from_cache(const QString &host) {
		// If host exist in cache
		if (cache.find(host) != cache.end()) {
			DnsEntry &entry = cache.at(host);

			// If expired, return the dns
			if (entry.is_expired()) {
				return &entry;
			}

			// Check entry type id:
			// 1: A (address record), emit resolved
			// 5: CNAME (canonical name record), resolve the new name from cache recursively
			if (entry.get_type() == 1) {
				return &entry;
			} else if (entry.get_type() == 5) {
				return resolve_from_cache(entry.get_data());
			}
		}

		// Host doesn't exist in cache
		return nullptr;
	}

	void DnsOverHttps::send_doh_request(const QString &host) {
		// Send request 
		request.set_query("name", host);
		request.get();
	}

	void DnsOverHttps::request_responded(uint16_t status_code, const QByteArray &data, const QString &error_message) {
		if (status_code == 200) {
			// Convert Json string to map object (QJsonDocument)
			QJsonDocument json_doc = QJsonDocument::fromJson(data);
			QString requested_name = json_doc["Question"][0]["name"].toString();
			const QJsonArray &answers = json_doc["Answer"].toArray();

			// For every entry, store it to cache
			for (const QJsonValue &value : answers) {
				QString name = value["name"].toString();
				uint16_t type = value["type"].toInt();
				uint16_t ttl = value["TTL"].toInt();
				QString data = value["data"].toString();

				// Remove the dot at the end of domain name for easier look up later on
				if (name.back() == '.') { // name also contains a dot at the end when using Google's DNS
					name.erase(name.end() - 1, name.end());
				}
				if (data.back() == '.') {
					data.erase(data.end() - 1, data.end());
				}

				DnsEntry entry(name, type, ttl, data);

				cache[name] = entry;
			}

			// Remove dot from the back of requested name
			if (requested_name.back() == '.') {
				requested_name.erase(requested_name.end() - 1, requested_name.end());
			}
			// Try to get the answer from the fresh cache
			DnsEntry *entry_from_cache = resolve_from_cache(requested_name);
			if (entry_from_cache != nullptr) {
				emit resolved(entry_from_cache->get_data());
			} else {
				qDebug() << "Failed to get fresh resolved host";
			}
		} else {
			qDebug() << status_code << " HTTP: " << error_message;
		}
	}

	std::unordered_map<QString, DnsEntry> DnsOverHttps::cache;

}