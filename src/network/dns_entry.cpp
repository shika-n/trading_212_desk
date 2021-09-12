#include "dns_entry.h"

namespace trading_212_desk {

	DnsEntry::DnsEntry() {

	}

	DnsEntry::DnsEntry(const QString& name, uint16_t type, uint16_t ttl, const QString& data) : name(name), type(type), data(data) {
		expires_at = std::chrono::high_resolution_clock::now() + std::chrono::seconds(ttl);
	}

	const QString& DnsEntry::get_name() {
		return name;
	}

	const QString& DnsEntry::get_data() {
		return data;
	}

	uint16_t DnsEntry::get_type() {
		return type;
	}

	bool DnsEntry::is_expired() {
		time_t diff = std::chrono::duration_cast<std::chrono::milliseconds>(expires_at - std::chrono::high_resolution_clock::now()).count();

		return diff <= 0;
	}

}