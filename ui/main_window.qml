import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material

// #363945 navy
// #2e313b dark navy
// #00a9e1 light blue
// #30c296 green
// #e34d50 red

ApplicationWindow {
    visible: true
    width: 800
    height: 600
    title: "T212 Portfolio Scraper"

    Material.theme: Material.Dark
    Material.background: "#2e313b"
    Material.primary: "#363945"
    Material.accent: "#00a9e1"

    menuBar: MenuBar {
        background: Pane {
            Material.elevation: 6
            Rectangle {
                color: Material.primary
            }
        }
        Menu {
            title: qsTr("File")
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
}