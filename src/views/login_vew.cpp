#include "login_view.h"

#include <QQmlApplicationEngine>
#include <QQuickWindow>
#include <memory>

namespace trading_212_desk {

	LoginView::LoginView(QQmlApplicationEngine *engine) : engine(engine), instance(nullptr) {
	}

	void LoginView::show() {
		// If there is no instance yet
		if (instance == nullptr) {
			// Get the root window/parent
			QObject *root_window = qobject_cast<QWindow *>(engine->rootObjects().first());
			
			// Load the component
			QQmlComponent component(engine, ":/qml/windows/login_window.qml", root_window);

			// Create the instance
			instance = component.create();

			// If component creation is successful
			if (instance != nullptr) {
				instance->setProperty("cLoginView", QVariant::fromValue(this));
				// Set the component's parent
				instance->setParent(root_window);
				// Set the window's parent
				static_cast<QQuickWindow *>(instance)->setTransientParent(static_cast<QWindow *>(root_window));
				// Set as visible
				instance->setProperty("visible", true);
			}
		} else {
			// If instance exists, show the window
			instance->setProperty("visible", true);
		}
	}

	void LoginView::close() {
		instance->deleteLater();
		instance = nullptr;
	}

	LoginView::~LoginView() {
		close();
	}

}