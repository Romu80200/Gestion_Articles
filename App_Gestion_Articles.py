# -*- coding: utf-8 -*-
# Version Python 3.7.6

"""
Application to manage item codes in a store
Possible actions:
    - Search codes in DataBase
    - Create codes (10 digits required) only possible with login or password
    - Modify codes (the system does not allow deleting codes) with login or password
    - Administration mode (database modification, user management ...)
"""

from qtpy.QtWidgets import QApplication, QWidget, QTabWidget
from qtpy.QtWidgets import QVBoxLayout
from qtpy.QtGui import QFont, QIcon

from tab_create import TabCreate
from tab_search import TabSearch


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Logiciel de gestion des Codes Article")
        self.resize(800, 800)
        try:
            self.setWindowIcon(QIcon("icon.jpg"))  # Todo add icon file
        except:
            self.setWindowIcon("")
        self.main_layout = QVBoxLayout(self)
        # Init Tab Screen
        self.tab_widget = QTabWidget()
        self.tab_home = QWidget()
        self.tab_search = TabSearch()  # QWidget()
        self.tab_create = TabCreate()  # QWidget()
        self.tab_modify = QWidget()
        self.tab_overview = QWidget()  # Maybe
        self.tab_admin = QWidget()
        # Add Tab
        self.tab_widget.addTab(self.tab_home, "Accueil")
        self.tab_widget.addTab(self.tab_search, "Rechercher un Code Article")
        self.tab_widget.addTab(self.tab_create, "Créer un Code Article")
        self.tab_widget.addTab(self.tab_modify, "Modifier un Code Article")
        self.tab_widget.addTab(self.tab_overview, "Aperçu Config")
        self.tab_widget.addTab(self.tab_admin, "Admin")

        self.tab_widget.setTabShape(QTabWidget.Triangular)

        # Add TabWidget to Widget
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)


app = QApplication([])
with open("style.qss", "r") as f:
    _style = f.read()
    app.setStyleSheet(_style)
    app.setFont(QFont("Times", 11))
main_window = MainWindow()
main_window.show()
app.exec_()
