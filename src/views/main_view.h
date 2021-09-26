#pragma once

#include <QObject>

#include "network/dns_over_https.h"
#include "login_view.h"

class QQmlApplicationEngine;

namespace trading_212_desk{
	class MainView : public QObject {
		Q_OBJECT

	public:
		MainView(QQmlApplicationEngine *engine);

	public slots:
		void show_login_form();

	private:
		QQmlApplicationEngine *engine;

		LoginView login_view;

		DnsOverHttps doh;
	};
}