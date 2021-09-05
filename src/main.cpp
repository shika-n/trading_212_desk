#include <iostream>

#include "QtWidgets/qapplication.h"
#include "QtQml/qqmlapplicationengine.h"
#include "QtWidgets/qwidget.h"

int main(int argc, char **argv) {
	QApplication app(argc, argv);

	QQmlApplicationEngine engine;
	QObject::connect(&engine, &QQmlEngine::quit, &app, &QApplication::quit);
	engine.load(":/qml/main_window.qml");

	return app.exec();
}
