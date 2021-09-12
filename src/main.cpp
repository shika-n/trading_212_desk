#include <iostream>

#include <QApplication>
#include <QQmlApplicationEngine>

#include "network/net_request.h"
#include "network/dns_over_https.h"

int main(int argc, char** argv) {
	QApplication app(argc, argv);

	QQmlApplicationEngine engine;
	QObject::connect(&engine, &QQmlEngine::quit, &app, &QApplication::quit);

	engine.load(":/qml/main_window.qml");

	trading_212_desk::NetRequest req("https://live.trading212.com/rest/companies");
	trading_212_desk::DnsOverHttps doh(trading_212_desk::DnsProvider::kGoogle);
	req.get(&doh);

	return app.exec();
}
