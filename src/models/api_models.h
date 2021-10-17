#pragma once

#include <cstdint>
#include <QString>

namespace trading_212_desk {

	struct Equity {
        QString ticker;
        QString type;
        QString isin;
        QString currency;
        QString shortName;
        QString fullName;
        QString description;
        QString countryOfOrigin;
        float minTrade;
        uint8_t digitsPrecision;
        uint8_t quantityPrecision;
        uint8_t exchangeId;
	};

}