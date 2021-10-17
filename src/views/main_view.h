#pragma once

#include <vector>

#include <QObject>

#include "login_view.h"
#include "models/api_models.h"
#include "network/dns_over_https.h"
#include "network/net_request.h"

class QQmlApplicationEngine;

namespace trading_212_desk{
	class MainView : public QObject {
		Q_OBJECT

	public:
		MainView(QQmlApplicationEngine *engine);

	public slots:
		void show_login_form();

		void instruments_response(uint16_t status_code, const QByteArray &data, const QString &error_message);

	private:
		QQmlApplicationEngine *engine;

		LoginView login_view;

		DnsOverHttps doh;

		std::vector<Equity> equities;
		NetRequest instruments_request;
	};
}