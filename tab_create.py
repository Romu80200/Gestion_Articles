# -*- coding: utf-8 -*-
# Version Python 3.7.6
from qtpy.QtWidgets import QWidget
from qtpy.QtWidgets import QVBoxLayout, QGridLayout
from qtpy.QtWidgets import QPushButton, QLabel, QFrame, QLineEdit, QComboBox, QProgressBar
from qtpy.QtWidgets import QStatusBar
from qtpy.QtCore import Qt

import constant
import constant_qss
import config_articles


class TabCreate(QWidget):
    def __init__(self):
        super().__init__()
        self.step_create_code_validated = [False] * 6
        # self.step_create_code_validated = [False, True, True, True, True, True]  # for test stylesheet
        self.init_tab_create()
        self.init_formular_create()

    def init_tab_create(self):
        self.main_layout = QVBoxLayout(self)
        self.lbl_title_create = QLabel()
        self.lbl_title_create.setText("Formulaire de création d'un Code Article")
        self.lbl_title_create.setObjectName("lbl_title_create")
        self.lbl_title_create.setAlignment(Qt.AlignCenter)
        self.lbl_title_create.setMaximumHeight(50)
        self.frm_create_article = QFrame()
        self.frm_create_article.layout = QGridLayout(self.frm_create_article)
        self.lbl_frame_create = QLabel()
        self.lbl_frame_create.setText("Remplissez les zones suivantes")
        self.lbl_frame_create.setObjectName("lbl_frame_create")
        self.lbl_frame_create.setMaximumHeight(50)
        self.lbl_frame_create.setAlignment(Qt.AlignCenter)
        self.lbl_machine = QLabel()
        self.lbl_machine.setText("Choisir la Machine :")
        self.lbl_machine.setObjectName("lbl_information_article")
        self.lbl_family = QLabel()
        self.lbl_family.setText("Choisir la Famille :")
        self.lbl_family.setObjectName("lbl_information_article")
        self.lbl_element = QLabel()
        self.lbl_element.setText("Choisir une Catégorie :")
        self.lbl_element.setObjectName("lbl_information_article")
        self.lbl_designation = QLabel()
        self.lbl_designation.setText("Renseigner la Désignation :")
        self.lbl_designation.setObjectName("lbl_information_article")
        self.lbl_reference = QLabel()
        self.lbl_reference.setText("Renseigner la Référence :")
        self.lbl_reference.setObjectName("lbl_information_article")
        self.lbl_supplier = QLabel()
        self.lbl_supplier.setText("Renseigner le Fournisseur :")
        self.lbl_supplier.setObjectName("lbl_information_article")
        self.lbl_article_placed_on_machine = QLabel()
        self.lbl_article_placed_on_machine.setText("Emplacement sur la Machine :")
        self.lbl_article_placed_on_machine.setObjectName("lbl_information_article")
        self.lbl_image_product = QLabel()
        self.lbl_image_product.setText("Image de l'Article :")
        self.lbl_image_product.setObjectName("lbl_information_article")
        self.lbl_image_file = QLabel()
        self.lbl_image_file.setObjectName("lbl_image_file")
        self.lbl_image_file.setText("Facultatif")
        self.lbl_image_file.setMaximumHeight(22)
        self.cbb_machine = QComboBox()
        self.cbb_machine.setEditable(False)
        self.cbb_machine.currentTextChanged.connect(self.cbb_machine_changed)
        self.cbb_family = QComboBox()
        self.cbb_family.setEditable(False)
        self.cbb_family.currentTextChanged.connect(self.cbb_family_changed)
        self.cbb_element = QComboBox()
        self.cbb_element.setEnabled(False)
        self.cbb_element.setEditable(False)
        self.cbb_element.currentTextChanged.connect(self.cbb_element_changed)
        self.le_designation = QLineEdit()  # Multiligne
        # self.le_designation.setMaximumHeight(75)
        self.le_designation.editingFinished.connect(self.le_designation_changed)
        self.le_reference = QLineEdit()
        self.le_supplier = QLineEdit()
        self.le_article_placed_on_machine = QLineEdit()
        self.le_article_placed_on_machine.setPlaceholderText("Facultatif")
        self.btn_search_file = QPushButton()
        self.btn_search_file.setEnabled(False)  # btn désactivé pour le moment/Todo:option à implémenter par la suite
        self.btn_search_file.setObjectName("btn_search_file")
        self.btn_search_file.setText("Cliquez ici\npour sélectionner\nune image du produit\n\n(Facultatif)")
        self.btn_search_file.setMaximumSize(300, 300)
        self.btn_search_file.setToolTip("Fonction non disponible pour le moment")
        self.lbl_article_assigned = QLabel()
        self.lbl_article_assigned.setText("Code Article attribué :")
        self.lbl_article_assigned.setObjectName("lbl_information_article")
        self.lbl_create_article_number = QLabel()
        self.lbl_create_article_number.setText("*" * 10)
        self.lbl_create_article_number.setStyleSheet(constant_qss.LBL_CREATE_ARTICLE_NUMBER_NOK)
        self.lbl_create_article_number.setAlignment(Qt.AlignCenter)
        self.lbl_create_article_number.setMaximumHeight(40)
        self.btn_create_article = QPushButton("Créer Article")
        self.btn_create_article.setStyleSheet(constant_qss.BTN_CREATE_ARTICLE_NOK)
        self.btn_create_article.setMaximumHeight(60)
        self.btn_create_article.setEnabled(False)
        self.btn_create_article.released.connect(self.btn_create_article_cliked)
        self.prgbar_create_article = QProgressBar()
        self.prgbar_create_article.setObjectName("prgbar_create_article")
        self.prgbar_create_article.setAlignment(Qt.AlignCenter)
        self.prgbar_create_article.setOrientation(Qt.Vertical)
        self.prgbar_create_article.setInvertedAppearance(True)
        self.prgbar_create_article.setValue(0)
        self.sb_create_info = QStatusBar()
        self.sb_create_info.setStyleSheet(constant_qss.SB_CREATE_INFO_NOK)
        self.sb_create_info.setSizeGripEnabled(False)
        self.sb_create_info.setMaximumHeight(30)
        self.sb_create_info.showMessage(constant.MESSAGE_STATUS_INFO.format(1, constant.DICT_STEP[1]))
        self.sb_create_warning = QStatusBar()
        self.sb_create_warning.setStyleSheet(constant_qss.SB_CREATE_WARNING_NOK)
        self.sb_create_warning.setSizeGripEnabled(False)
        self.sb_create_warning.setMaximumHeight(30)
        self.sb_create_warning.showMessage(constant.MESSAGE_STATUS_WARNING_NOK)
        self.frm_create_article.layout.addWidget(self.lbl_frame_create, 0, 0, 1, 6)
        self.frm_create_article.layout.addWidget(self.lbl_machine, 1, 0, 1, 1)
        self.frm_create_article.layout.addWidget(self.cbb_machine, 1, 1, 1, 4)
        self.frm_create_article.layout.addWidget(self.prgbar_create_article, 1, 5, 6, 1)
        self.frm_create_article.layout.addWidget(self.lbl_family, 2, 0, 1, 1)
        self.frm_create_article.layout.addWidget(self.cbb_family, 2, 1, 1, 4)
        self.frm_create_article.layout.addWidget(self.lbl_element, 3, 0, 1, 1)
        self.frm_create_article.layout.addWidget(self.cbb_element, 3, 1, 1, 4)
        self.frm_create_article.layout.addWidget(self.lbl_designation, 4, 0, 1, 1)
        self.frm_create_article.layout.addWidget(self.le_designation, 4, 1, 1, 4)
        self.frm_create_article.layout.addWidget(self.lbl_reference, 5, 0, 1, 1)
        self.frm_create_article.layout.addWidget(self.le_reference, 5, 1, 1, 4)
        self.frm_create_article.layout.addWidget(self.lbl_supplier, 6, 0, 1, 1)
        self.frm_create_article.layout.addWidget(self.le_supplier, 6, 1, 1, 4)
        self.frm_create_article.layout.addWidget(self.lbl_article_placed_on_machine, 7, 0, 1, 1)
        self.frm_create_article.layout.addWidget(self.le_article_placed_on_machine, 7, 1, 1, 2)
        self.frm_create_article.layout.addWidget(self.lbl_image_product, 8, 0, 1, 1)
        self.frm_create_article.layout.addWidget(self.lbl_image_file, 8, 1, 1, 2)
        self.frm_create_article.layout.addWidget(self.btn_search_file, 7, 3, 4, 3)
        self.frm_create_article.layout.addWidget(self.lbl_article_assigned, 9, 0, 1, 1)
        self.frm_create_article.layout.addWidget(self.lbl_create_article_number, 9, 1, 1, 2)
        self.frm_create_article.layout.addWidget(self.btn_create_article, 10, 1, 1, 2)
        self.frm_create_article.layout.addWidget(self.sb_create_info, 11, 0, 1, 6)
        self.frm_create_article.layout.addWidget(self.sb_create_warning, 12, 0, 1, 6)
        self.main_layout.addWidget(self.lbl_title_create)
        self.main_layout.addWidget(self.frm_create_article)
        self.setLayout(self.main_layout)

    def init_formular_create(self):
        """initialize the formular at the beggining or after creation of code article"""
        self.cbb_machine.clear()
        self.cbb_family.clear()
        for key in config_articles.config["machine"].keys():
            self.cbb_machine.addItem(key)
        for key in config_articles.config["famille"].keys():
            self.cbb_family.addItem(key)
        self.le_designation.clear()
        self.le_reference.clear()
        self.le_supplier.clear()
        self.le_article_placed_on_machine.clear()
        self.lbl_create_article_number.setText("*" * 10)

    def cbb_machine_changed(self):
        """first step of creation of code article"""
        self.actions_when_formular_changed(step=1, current_text=self.cbb_machine.currentText())

    def cbb_family_changed(self):
        """second step of creation of code article"""
        self.cbb_element.clear()  # the element combobox depends on the family combobox
        self.actions_when_formular_changed(step=2, current_text=self.cbb_family.currentText())

    def cbb_element_changed(self):
        """third step of creation of code article"""
        self.actions_when_formular_changed(step=3, current_text=self.cbb_element.currentText())

    def le_designation_changed(self):
        print("LineEdit Exit")

    def actions_when_formular_changed(self, step, current_text):
        """list of functions to execute when formular changed"""
        self.actions_when_cbb_create_tab_changed(step, current_text)
        self.assign_create_tab_number()
        self.update_create_tab_progress_bar()
        self.modify_create_tab_stylesheet()
        self.modify_create_tab_status_bar()

    def actions_when_cbb_create_tab_changed(self, step, current_text):
        """Actions to execute when a combobox changed"""
        # define differents bit of code article for each step of form
        dict_code = {
            1: {"start_code": "",
                "middle_code_ok": config_articles.config["machine"].get(current_text, "*" * 4),
                "middle_code_nok": "*" * 4,
                "end_code": self.lbl_create_article_number.text()[4:],
                },
            2: {"start_code": self.lbl_create_article_number.text()[:4],
                "middle_code_ok": config_articles.config["famille"].get(current_text, "*" * 1),
                "middle_code_nok": "*" * 1,
                "end_code": self.lbl_create_article_number.text()[5:],
                },
            3: {"start_code": self.lbl_create_article_number.text()[:5],
                "middle_code_ok":
                    config_articles.config["element"][self.cbb_family.currentText()].get(current_text, "*" * 2),
                "middle_code_nok": "*" * 2,
                "end_code": self.lbl_create_article_number.text()[7:],
                },
        }
        # define if step is validated
        self.step_create_code_validated[step - 1] = False if current_text == "" else True
        # define middile_code is ok or nok + start_code number + end code number -> update the new code article
        start_code = dict_code[step]["start_code"]
        middle_code = \
            dict_code[step]["middle_code_nok"] if current_text == "" else dict_code[step]["middle_code_ok"]
        end_code = dict_code[step]["end_code"]
        # update the code article
        self.lbl_create_article_number.setText(start_code + middle_code + end_code)
        # enabled combobox cbb_element or not
        self.cbb_element.setEnabled(False if current_text == "" and step == 2 else True)
        # add item in cbb_element
        if current_text != "" and step == 2:
            for key in config_articles.config["element"][current_text].keys():
                self.cbb_element.addItem(key)
        # Todo : clear below old code if application ok
        """below old code -> optimized: Maybe 😅
        if cbb_current_text == "":
            self.lbl_create_article_number.setText(
                dict_code[step]["start_code"] + dict_code[step]["middle_code_nok"] + dict_code[step]["end_code"]
            )
            self.step_create_code_validated[step - 1] = False
            if step == 2:
                self.cbb_element.setEnabled(False)
        else:
            self.lbl_create_article_number.setText(
                dict_code[step]["start_code"] + dict_code[step]["middle_code_ok"] + dict_code[step]["end_code"]
            )
            self.step_create_code_validated[step - 1] = True
            if step == 2:
                for key in config_articles.config["element"][cbb_current_text].keys():
                    self.cbb_element.addItem(key)
                self.cbb_element.setEnabled(True)"""

    def assign_create_tab_number(self):
        # attribuer les 3 derniers chiffres
        # il faut rechercher tous les codes articles
        # qui commencent par les 7 premiers caractères du lbl_create_article_number
        # et ajouter 1 au plus grand code trouvé
        # afin de completer le nouveau code pour le nouvel article
        # Todo function
        if sum(self.step_create_code_validated[:3]) == 3:
            print("fonction pour attribuer un numéro sur 3 caratère")

    def update_create_tab_progress_bar(self):
        """modify progress bar of create tab"""
        self.prgbar_create_article.setValue(sum(self.step_create_code_validated) * 100 / 6)

    def modify_create_tab_stylesheet(self):
        """modify stylesheet lbl_create_article_number & btn_create_article if form is completed"""
        if sum(self.step_create_code_validated) == 6:
            self.lbl_create_article_number.setStyleSheet(constant_qss.LBL_CREATE_ARTICLE_NUMBER_OK)
            self.btn_create_article.setStyleSheet(constant_qss.BTN_CREATE_ARTICLE_OK)
            self.btn_create_article.setEnabled(True)
        else:
            self.lbl_create_article_number.setStyleSheet(constant_qss.LBL_CREATE_ARTICLE_NUMBER_NOK)
            self.btn_create_article.setStyleSheet(constant_qss.BTN_CREATE_ARTICLE_NOK)
            self.btn_create_article.setEnabled(False)

    def modify_create_tab_status_bar(self):
        """modify 2 status bar if form is completed"""
        if sum(self.step_create_code_validated) == 6:
            self.sb_create_info.showMessage(constant.MESSAGE_STATUS_INFO_OK)
            self.sb_create_info.setStyleSheet(constant_qss.SB_CREATE_INFO_OK)
            self.sb_create_warning.showMessage(constant.MESSAGE_STATUS_WARNING_OK)
            self.sb_create_warning.setStyleSheet(constant_qss.SB_CREATE_WARNING_OK)
        else:
            for step, _value in enumerate(self.step_create_code_validated, start=1):
                if not _value:
                    break
            self.sb_create_info.showMessage(constant.MESSAGE_STATUS_INFO.format(step, constant.DICT_STEP[step]))
            self.sb_create_info.setStyleSheet(constant_qss.SB_CREATE_INFO_NOK)
            self.sb_create_warning.showMessage(constant.MESSAGE_STATUS_WARNING_NOK)
            self.sb_create_warning.setStyleSheet(constant_qss.SB_CREATE_WARNING_NOK)

    def btn_create_article_cliked(self):
        # Todo create function
        # Todo choice a DataBase
        # fill the database with the various information transmitted via the form
        # display a popup to confirm the creation of code article
        print("Btn Create Article Clicked")
        # clear the formular to create a new article
        self.init_formular_create()
