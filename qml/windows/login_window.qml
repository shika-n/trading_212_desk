import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts

ApplicationWindow {
	id: loginWindow
	minimumWidth: 400
	minimumHeight: 300
	maximumWidth: minimumWidth
	maximumHeight: minimumHeight
	modality: Qt.WindowModal

	property var cLoginView
	
	header: TabBar {
		id: tabs
		width: parent.width
		TabButton {
			text: qsTr("Credential")
		}
		TabButton {
			text: qsTr("Token")
		}
	}
	StackLayout {
		currentIndex: tabs.currentIndex
		anchors.fill: parent
		Container {
			id: credentialTab
			padding: 8
			contentItem: GridLayout {
				columns: 2
				rows: 3
				anchors.horizontalCenter: credentialTab.horizontalCenter
				Label {
					text: qsTr("E-mail")
				}
				TextField {
					placeholderText: qsTr("E-mail")
					selectByMouse: true
					Layout.fillWidth: true
				}
				Label {
					text: qsTr("Password")
				}
				TextField {
					placeholderText: qsTr("Password")
					echoMode: TextInput.Password
					selectByMouse: true
					Layout.fillWidth: true
				}
				Label {
					text: qsTr("Feels unsafe using credentials? Use a token instead!")
					Layout.fillWidth: true
					Layout.fillHeight: true
					Layout.columnSpan: 2
					horizontalAlignment: Text.AlignHCenter
					verticalAlignment: Text.AlignVCenter
				}
			}
		}
		Container {
			id: tokenTab
			padding: 16
			contentItem: GridLayout {
				columns: 2
				rows: 2
				anchors.horizontalCenter: tokenTab.horizontalCenter
				Label {
					text: qsTr("Token")
				}
				TextField {
					placeholderText: qsTr("Token")
					selectByMouse: true
					Layout.fillWidth: true
				}
				Label {
					text: qsTr("To get your token:\n1. Login to Trading 212 on your web browser\n2. Press F12\n3. Go to Cookies\n4. Get the value of TRADING212_SESSION_LIVE")
					Layout.fillWidth: true
					Layout.fillHeight: true
					Layout.columnSpan: 2
					verticalAlignment: Text.AlignVCenter
				}
			}
		}
	}
	footer: Container {
		height: 64
		contentItem: RowLayout {
			Button {
				text: qsTr("Cancel")
				flat: true
				Layout.fillWidth: true
				Layout.fillHeight: true
				onReleased: {
					loginWindow.close();
				}
			}
			Button {
				text: qsTr("Login")
				flat: true
				Layout.fillWidth: true
				Layout.fillHeight: true
				onReleased: {
					cLoginView.login();
				}
			}
		}
	}
}