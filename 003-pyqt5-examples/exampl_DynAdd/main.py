import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView

# Пример динамического добавления новых элементов.
# Note: Элементы добавляются только средствами QML!!!

app = QGuiApplication(sys.argv)

qmlFile = 'main.qml'

view = QQuickView()
view.setResizeMode(QQuickView.SizeRootObjectToView)
view.engine().quit.connect(app.quit)

engine = view.engine()
view.setSource(QUrl(qmlFile))

view.show()
sys.exit(app.exec_())
