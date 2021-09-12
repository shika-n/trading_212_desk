#pragma once

#include <chrono>
#include <cstdint>

#include <QString>

namespace trading_212_desk {
	class DnsEntry {
	public:
		DnsEntry();
		DnsEntry(const QString& name, uint16_t type, uint16_t ttl, const QString& data);

		const QString& get_name();
		const QString& get_data();

		uint16_t get_type();
		bool is_expired();

	private:
		QString name;
		uint16_t type;
		std::chrono::steady_clock::time_point expires_at;
		QString data;
	};
}