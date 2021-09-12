#pragma once

#include <unordered_map>

#include <QObject>

#include "net_request.h"

namespace trading_212_desk {
	class DnsEntry;

	enum class DnsProvider {
		kCloudflare,
		kGoogle
	};

	class DnsOverHttps : public QObject {
		Q_OBJECT

	public:
		DnsOverHttps(DnsProvider dns_provider);

		void resolve(const QString& host);

	signals:
		void resolved(const QString& resolved_host);

	private:
		static std::unordered_map<QString, DnsEntry> cache;
		NetRequest request;

		DnsEntry* resolve_from_cache(const QString& host);

		void send_doh_request(const QString& host);

	private slots:
		void request_responded(uint16_t status_code, const QByteArray& data, const QString& error_message);
	};
}