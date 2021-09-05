import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts
import QtCharts

// #363945 navy
// #2e313b dark navy
// #00a9e1 light blue
// #30c296 green
// #e34d50 red

ApplicationWindow {
	id: window
	visible: true
	width: 1280
	height: 720
	title: "T212 Portfolio Scraper"

	property bool drawerExpanded: true

	// Material.theme: Material.Dark
	// Material.background: "#2e313b"
	// Material.primary: "#363945"
	// Material.accent: "#00a9e1"

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
		height: window.height - menuBar.height
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
}