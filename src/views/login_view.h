#pragma once

#include <QObject>
#include <QQmlComponent>

class QQmlApplicationEngine;

namespace trading_212_desk {
	class LoginView : public QObject {
		Q_OBJECT

	public:
		LoginView(QQmlApplicationEngine *engine);

		void show();

		~LoginView();

	public slots:
		void close();

	private:
		QQmlApplicationEngine *engine;

		QObject *instance;
	};
}