#include "main_view.h"

#include <QQmlApplicationEngine>
#include <QQmlComponent>
#include <QQmlContext>
#include <QQuickItem>
#include <QQuickWindow>

#include "login_view.h"

namespace trading_212_desk {

	MainView::MainView(QQmlApplicationEngine *engine) : engine(engine), login_view(engine), doh(DnsProvider::kCloudflare) {
		engine->load(":/qml/main_window.qml");

		QObject *root = engine->rootObjects().first();
		root->setProperty("cMainView", QVariant::fromValue(this));
	}

	void MainView::show_login_form() {
		login_view.show();
	}

}