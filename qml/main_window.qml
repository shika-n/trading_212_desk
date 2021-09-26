import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts

// #363945 navy
// #2e313b dark navy
// #00a9e1 light blue
// #30c296 green
// #e34d50 red

ApplicationWindow {
	id: rootWindow
	title: "Trading 212 Desk"
	width: 1280
	height: 720
	visible: true

	property var cMainView

	menuBar: MenuBar {
		background: Pane {
			Material.elevation: 6
			background: Rectangle {
				color: Material.primary
			}
		}
		Menu {
			title: qsTr("File")
			MenuItem {
				text: qsTr("Login")
				onTriggered: {
					cMainView.show_login_form();
				}
			}
			MenuSeparator {
				padding: 2
			}
			MenuItem {
				text: qsTr("Quit")
				onTriggered: Qt.quit()
			}
		}
	}

	Drawer {
		id: drawer
		modal: false
		y: menuBar.height
		width: 48
		height: rootWindow.height - menuBar.height
		interactive: false
		visible: true
		background: Rectangle {
			color: Material.primary
		}
		ColumnLayout {
			spacing: 0
			anchors.left: parent.left
			anchors.right: parent.right
			RoundButton {
				id: home
				Layout.preferredWidth: parent.width
				Layout.preferredHeight: Layout.preferredWidth
				flat: true
			}
			RoundButton {
				Layout.preferredWidth: parent.width
				Layout.preferredHeight: Layout.preferredWidth
				flat: true
			}
		}
	}

	Container {
		width: parent.width
		height: parent.height
		leftInset: drawer.width
		leftPadding: leftInset

		contentItem: Item {
		}
	}
}