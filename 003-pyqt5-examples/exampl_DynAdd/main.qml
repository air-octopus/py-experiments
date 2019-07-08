import QtQuick 2.2
Rectangle {
    id: mainRec
    width: 480
    height: 480
    MouseArea
    {
        id: mArea
        anchors.fill: parent
        onClicked:
        {
            var component = Qt.createComponent("KnowledgeItem.qml");
            if (component.status == Component.Ready) {
                var childRec = component.createObject(mainRec);
                childRec.x = mArea.mouseX - (childRec.width / 2);
                childRec.y = mArea.mouseY - (childRec.height / 2);
            }
        }
    }
}
