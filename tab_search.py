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
        self.le_search_reference = QLabel()
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
        self.frm_search_article.layout.addWidget(self.frm_search_code, 1, 1, 4, 1)
        self.frm_search_code.layout.addWidget(self.lbl_search_code)
        self.frm_search_code.layout.addWidget(self.le_search_code)
        self.frm_search_code.layout.addWidget(self.btn_search_code)
        self.frm_search_article.layout.addWidget(self.rbtn_search_reference, 2, 0, 1, 1)
        self.frm_search_article.layout.addWidget(self.frm_search_reference, 2, 1, 4, 1)
        self.frm_search_article.layout.addWidget(self.rbtn_search_by_step, 3, 0, 1, 1)
        self.frm_search_article.layout.addWidget(self.frm_search_by_step, 3, 1, 4, 1)
        self.main_layout.addWidget(self.lbl_title_search)
        self.main_layout.addWidget(self.frm_search_article)
        self.setLayout(self.main_layout)

    def init_tab_search_widgets_property(self):
        # lbl_title_create
        self.lbl_title_search.setText("Formulaire de recherche d'un Code Article")
        self.lbl_title_search.setObjectName("lbl_title_search")
        self.lbl_title_search.setAlignment(Qt.AlignCenter)
        self.lbl_title_search.setMaximumHeight(50)
        self.lbl_frame_search.setText("Choisissez votre mode de recherche")
        self.lbl_frame_search.setObjectName("lbl_frame_create")
        self.lbl_frame_search.setMaximumHeight(50)
        self.lbl_frame_search.setAlignment(Qt.AlignCenter)

    def init_tab_search_connections(self):
        pass

    def init_formular_search(self):
        pass
