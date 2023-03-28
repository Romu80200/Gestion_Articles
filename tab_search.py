# -*- coding: utf-8 -*-
# Version Python 3.7.6

from qtpy.QtWidgets import QWidget
from qtpy.QtWidgets import QVBoxLayout, QGridLayout, QHBoxLayout
from qtpy.QtWidgets import QPushButton, QLabel, QFrame, QLineEdit, QComboBox, QProgressBar, QStatusBar, QRadioButton
from qtpy.QtCore import Qt

import constant
import constant_qss
import config_articles


class TabSearch(QWidget):
    def __init__(self):
        super().__init__()

        self.init_tab_search_widgets()
        self.init_tab_search_widgets_property()
        self.init_tab_search_connections()
        self.init_formular_search()

    def init_tab_search_widgets(self):
        self.main_layout = QVBoxLayout(self)
        self.lbl_title_search = QLabel()
        self.frm_search_article = QFrame()
        self.frm_search_article.layout = QGridLayout(self.frm_search_article)
        self.lbl_frame_search = QLabel()
        self.rbtn_search_code = QRadioButton()
        self.rbtn_search_reference = QRadioButton()
        self.rbtn_search_by_step = QRadioButton()
        self.frm_search_code = QFrame()
        self.frm_search_code.layout = QVBoxLayout(self.frm_search_code)
        self.lbl_search_code = QLabel()
        self.le_search_code = QLineEdit()
        self.btn_search_code = QPushButton()
        self.frm_search_reference = QFrame()
        self.frm_search_reference.layout = QVBoxLayout(self.frm_search_reference)
        self.lbl_search_reference = QLabel()
        self.le_search_reference = QLineEdit()
        self.btn_search_reference = QPushButton()
        self.frm_search_by_step = QFrame()
        self.frm_search_by_step.layout = QGridLayout(self.frm_search_by_step)
        self.lbl_machine = QLabel()
        self.cbb_machine = QComboBox()
        self.lbl_family = QLabel()
        self.cbb_family = QComboBox()
        self.lbl_element = QLabel()
        self.cbb_element = QComboBox()
        self.prgbar_search = QProgressBar()
        self.btn_search_by_step = QPushButton()
        self.frm_sb_info = QFrame()
        self.frm_sb_info.layout = QHBoxLayout(self.frm_sb_info)
        self.sb_info = QStatusBar()
        self.btn_display_result = QPushButton()
        self.sb_warning = QStatusBar()
        self.frm_search_article.layout.addWidget(self.lbl_frame_search, 0, 0, 1, 2)
        self.frm_search_article.layout.addWidget(self.rbtn_search_code, 1, 0, 1, 1)
        self.frm_search_article.layout.addWidget(self.frm_search_code, 1, 1, 1, 1)
        self.frm_search_code.layout.addWidget(self.lbl_search_code)
        self.frm_search_code.layout.addWidget(self.le_search_code)
        self.frm_search_code.layout.addWidget(self.btn_search_code)
        self.frm_search_article.layout.addWidget(self.rbtn_search_reference, 2, 0, 1, 1)
        self.frm_search_article.layout.addWidget(self.frm_search_reference, 2, 1, 1, 1)
        self.frm_search_reference.layout.addWidget(self.lbl_search_reference)
        self.frm_search_reference.layout.addWidget(self.le_search_reference)
        self.frm_search_reference.layout.addWidget(self.btn_search_reference)
        self.frm_search_article.layout.addWidget(self.rbtn_search_by_step, 3, 0, 1, 1)
        self.frm_search_article.layout.addWidget(self.frm_search_by_step, 3, 1, 1, 1)
        self.frm_search_by_step.layout.addWidget(self.lbl_machine)
        self.frm_search_by_step.layout.addWidget(self.cbb_machine)
        self.frm_search_by_step.layout.addWidget(self.lbl_family)
        self.frm_search_by_step.layout.addWidget(self.cbb_family)
        self.frm_search_by_step.layout.addWidget(self.lbl_element)
        self.frm_search_by_step.layout.addWidget(self.cbb_element)
        self.frm_search_by_step.layout.addWidget(self.btn_search_by_step)
        self.frm_search_article.layout.addWidget(self.sb_info, 4, 0, 1, 2)
        self.frm_search_article.layout.addWidget(self.sb_warning, 5, 0, 1, 2)
        self.main_layout.addWidget(self.lbl_title_search)
        self.main_layout.addWidget(self.frm_search_article)
        self.setLayout(self.main_layout)

    def init_tab_search_widgets_property(self):
        # lbl_title_create
        self.lbl_title_search.setText("Formulaire de recherche d'un Code Article")
        self.lbl_title_search.setObjectName("lbl_title_search")
        self.lbl_title_search.setAlignment(Qt.AlignCenter)
        self.lbl_title_search.setMaximumHeight(50)
        # lbl_frame_search
        self.lbl_frame_search.setText("Choisissez le mode de recherche")
        self.lbl_frame_search.setObjectName("lbl_frame_create")
        self.lbl_frame_search.setMaximumHeight(50)
        self.lbl_frame_search.setAlignment(Qt.AlignCenter)
        # rbtn_search_code
        self.rbtn_search_code.setText("Recherche par code")
        # frm_search_code
        self.frm_search_code.setEnabled(False)
        # lbl_search_code
        self.lbl_search_code.setText("Saisir un code Article")
        # le_search_code
        self.le_search_code.setPlaceholderText("Saisir le code ici")
        # btn_search_code
        self.btn_search_code.setText("Rechercher")
        # rbtn_search_reference
        self.rbtn_search_reference.setText("Recherche par Référence ou Désignation")
        # frm_search_reference
        self.frm_search_reference.setEnabled(False)
        # lbl_search_reference
        self.lbl_search_reference.setText("Saisir une référence ou une désignation")
        # le_search_reference
        self.le_search_reference.setPlaceholderText("Saisir la référence ici")
        # btn_search_refernce
        self.btn_search_reference.setText("Rechercher")
        # rbtn_search_by_step
        self.rbtn_search_by_step.setText("Recherche par étape")
        # frm_search_by_step
        self.frm_search_by_step.setEnabled(False)
        # lbl machine
        self.lbl_machine.setText("Choisir la machine :")
        # lbl_family
        self.lbl_family.setText("Choisir la famille :")
        # lbl_element
        self.lbl_element.setText("Choisir la catégorie :")
        # btn_search_by_step
        self.btn_search_by_step.setText("Rechercher")
        # sb_info
        self.sb_info.showMessage("INFO | Choisir un mode de recherche")

    def init_tab_search_connections(self):
        self.rbtn_search_code.toggled.connect(self.actions_when_rbtn_changed)
        self.rbtn_search_reference.toggled.connect(self.actions_when_rbtn_changed)
        self.rbtn_search_by_step.toggled.connect(self.actions_when_rbtn_changed)
        self.cbb_family.currentTextChanged.connect(self.cbb_family_changed)
        # self.frm_search_code.mouseDoubleClickEvent.connect(self.rbtn_search_code_checked)

    def init_formular_search(self):
        self.le_search_code.clear()
        self.le_search_reference.clear()
        self.cbb_machine.clear()
        self.cbb_family.clear()
        for key in config_articles.config["machine"].keys():
            self.cbb_machine.addItem(key)
        for key in config_articles.config["famille"].keys():
            self.cbb_family.addItem(key)
        self.cbb_element.clear()

    def actions_when_rbtn_changed(self):
        self.init_formular_search()
        self.set_enabled_frame()

    def set_enabled_frame(self):
        """ enabled frame if radioButton is checked """
        self.frm_search_code.setEnabled(self.rbtn_search_code.isChecked())
        self.frm_search_reference.setEnabled(self.rbtn_search_reference.isChecked())
        self.frm_search_by_step.setEnabled(self.rbtn_search_by_step.isChecked())

    def cbb_family_changed(self):
        self.cbb_element.clear()
        current_text = self.cbb_family.currentText()
        for key in config_articles.config["element"][current_text].keys():
            self.cbb_element.addItem(key)

    def rbtn_search_code_checked(self):
        self.rbtn_search_code.setChecked(True)
