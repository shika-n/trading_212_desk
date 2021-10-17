import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material
import QtQuick.Layouts

SplitView {
	anchors.fill: parent
	Item {
		SplitView.minimumWidth: 300
		ScrollView {
			id: scrollView
			anchors.fill: parent
			
			padding: 4
			rightPadding: 16 + padding

			ScrollBar.horizontal.policy: ScrollBar.AlwaysOff
			ScrollBar.vertical.policy: ScrollBar.AsNeeded

			ListView {
				id: listView
				model: 20
				spacing: 4

				boundsBehavior: Flickable.StopAtBounds
				
				delegate: Rectangle {
					width: listView.width
					height: 80
					radius: 8.0

					color: Material.primary
				}
			}
		}
	}
	Item {
		Rectangle {
			width: 200
			height: 200

		}
	}
}