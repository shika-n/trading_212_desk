#include <iostream>

#include <QApplication>
#include <QQmlApplicationEngine>

#include "views/main_view.h"

int main(int argc, char **argv) {
	QApplication app(argc, argv);

	QQmlApplicationEngine engine;
	QObject::connect(&engine, &QQmlEngine::quit, &app, &QApplication::quit);

	trading_212_desk::MainView main(&engine);

	return app.exec();
}
