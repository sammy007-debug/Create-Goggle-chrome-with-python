import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

#First thing we do is create a class
class MainWindow(QMainWindow):
    # We create a constructor - Python relies on the constructor to perform tasks such as initializing
    # (assigning values to) any instance variables that the object will need when it starts.
    def __init__(self):
        # Creates a super connection with parent class (QMainWindow)
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        # makes browser full screen
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('<-', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('->', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Refresh', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Youtube', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.youtube.com/channel/UCEzLeU7OURzqrpOBYHLXf4w'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

# initialize app and pass system argument
app = QApplication(sys.argv)
# set app name
QApplication.setApplicationName('SamCodes Chrome')
# Window class that we created above
window = MainWindow()
# call app to execute
app.exec_()