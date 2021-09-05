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

    Material.theme: Material.Dark
    Material.background: "#2e313b"
    Material.primary: "#363945"
    Material.accent: "#00a9e1"

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
                text: qsTr("Start Scraping")
            }
            MenuItem {
                text: qsTr("Open HTML")
            }
            MenuSeparator {
                padding: 2
            }
            MenuItem {
                text: qsTr("Open History CSV")
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

    Button {
        text: ">"
        width: 8
        height: 64
        leftInset: 0
        rightInset: 0
        padding: 0
        anchors.left: parent.left
        anchors.verticalCenter: parent.verticalCenter
        visible: !drawerExpanded
        onClicked: {
            drawerExpanded = !drawerExpanded
        }
    }

    Drawer {
        id: drawer
        modal: false
        y: menuBar.height
        width: Math.min(Math.max(window.width * 0.2, 200), 300)
        height: window.height - menuBar.height
        interactive: false
        visible: drawerExpanded
        background: Rectangle {
            color: Material.primary
        }
        ColumnLayout {
            spacing: 0
            anchors.left: parent.left
            anchors.right: parent.right
            Button {
                text: qsTr("Home")
                font.pixelSize: 18
                flat: true
                leftInset: 8
                rightInset: 8
                Layout.fillWidth: true
                Layout.preferredHeight: 64
                background: Rectangle {
                    color: Material.accent
                    radius: 8
                }

                Rectangle {
                    width: 32
                    height: 32
                    anchors.left: parent.left
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.leftMargin: parent.leftInset + 8
                }
            }
        }

        Button {
            text: "<"
            y: 32
            width: 8
            height: 64
            padding: 0
            leftInset: 0
            rightInset: 0
            anchors.right: parent.right
            anchors.verticalCenter: parent.verticalCenter
            visible: drawerExpanded

            onClicked: {
                drawerExpanded = !drawerExpanded
            }
        }
    }
}