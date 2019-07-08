import QtQuick 2.0
import QtQuick.Layouts 1.3

Rectangle {

    id: rec_main
    width: 300; height: 300
    transformOrigin: Item.BottomRight
    property alias rec_main: rec_main

//    anchors.verticalCenter: parent.verticalCenter
//    anchors.horizontalCenter: parent.horizontalCenter


    Rectangle {

        id:green_rectangle
        x: 0
        y: 0
        width: 150
        height: 150

        //задаем свойства нашему прямоугольнику


        //цвет нашего прямоугольника
        color:"green"

        //аналогично свойству border-radius
        radius: 7
        border.width: 9
        border.color: "#11694e"
        z: 10
        rotation: 30
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        transformOrigin: Item.Center



        Text {
            id: btn_green_label
            text: "Click me"
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter
        }
        MouseArea {
            anchors.rightMargin: 0
            anchors.bottomMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 0
            anchors.fill: parent
            onClicked: {
                console.log("Hey Programmer");
            }
        }

    }
}
