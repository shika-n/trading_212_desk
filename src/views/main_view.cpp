#include "main_view.h"

#include <QJsonArray>
#include <QJsonDocument>
#include <QQmlApplicationEngine>
#include <QQmlComponent>
#include <QQmlContext>
#include <QQuickItem>
#include <QQuickWindow>

#include "login_view.h"

namespace trading_212_desk {

	MainView::MainView(QQmlApplicationEngine *engine) : engine(engine), login_view(engine), doh(DnsProvider::kCloudflare) {
		engine->load(":/qml/MainWindow.qml");

		QObject *root = engine->rootObjects().first();
		root->setProperty("cMainView", QVariant::fromValue(this));

		connect(&instruments_request, &NetRequest::finished, this, &MainView::instruments_response);
		instruments_request.set_url("https://live.trading212.com/rest/instruments/EQUITY/-1830575850");
		instruments_request.get(&doh);
	}

	void MainView::show_login_form() {
		login_view.show();
	}

	void MainView::instruments_response(uint16_t status_code, const QByteArray &data, const QString &error_message) {
		if (status_code == 200) {
			QJsonDocument json_document = QJsonDocument::fromJson(data);
			QJsonArray items = json_document["items"].toArray();

			equities.reserve(items.size());// TODO: threads
			for (const QJsonValue &item : items) {
				Equity equity = {
					item["ticker"].toString(),
					item["type"].toString(),
					item["isin"].toString(),
					item["currency"].toString(),
					item["shortName"].toString(),
					item["fullName"].toString(),
					item["description"].toString(),
					item["countryOfOrigin"].toString(),
					item["minTrade"].toDouble(),
					item["digitsPrecision"].toInt(),
					item["quantityPrecision"].toInt(),
					item["exchangeId"].toInt()
				};
				equities.push_back(equity);
			}

			qDebug() << "Got" << equities.size() <<"instruments!";
		} else {
			qDebug() << error_message;
		}
	}

}