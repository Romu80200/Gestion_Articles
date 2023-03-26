# -*- coding: utf-8 -*-
# Version Python 3.7.6

from qtpy.QtWidgets import QWidget
from qtpy.QtWidgets import QVBoxLayout, QGridLayout
from qtpy.QtWidgets import QPushButton, QLabel, QFrame, QLineEdit, QComboBox, QProgressBar, QStatusBar
from qtpy.QtCore import Qt

import constant
import constant_qss
import config_articles


class TabCreate(QWidget):
    def __init__(self):
        super().__init__()
        self.number_combobox_required = 3
        self.number_element_required_to_create_article = len(constant.DICT_STEP)
        self.step_create_code_validated = [False] * len(constant.DICT_STEP)

        self.init_tab_create_widgets()
        self.init_tab_create_widgets_property()
        self.init_tab_create_connections()
        self.init_formular_create()

    def init_tab_create_widgets(self):
        self.main_layout = QVBoxLayout(self)
        self.lbl_title_create = QLabel()
        self.frm_create_article = QFrame()
        self.frm_create_article.layout = QGridLayout(self.frm_create_article)
        self.lbl_frame_create = QLabel()
        self.lbl_required_1 = QLabel()
        self.lbl_required_2 = QLabel()
        self.lbl_required_3 = QLabel()
        self.lbl_required_4 = QLabel()
        self.lbl_required_5 = QLabel()
        self.lbl_required_6 = QLabel()
        self.lbl_machine = QLabel()
        self.lbl_family = QLabel()
        self.lbl_element = QLabel()
        self.lbl_designation = QLabel()
        self.lbl_reference = QLabel()
        self.lbl_supplier = QLabel()
        self.lbl_article_placed_on_machine = QLabel()
        self.lbl_image_product = QLabel()
        self.lbl_image_file = QLabel()
        self.cbb_machine = QComboBox()
        self.cbb_family = QComboBox()
        self.cbb_element = QComboBox()
        self.le_designation = QLineEdit()
        self.le_reference = QLineEdit()
        self.le_supplier = QLineEdit()
        self.le_article_placed_on_machine = QLineEdit()
        self.btn_search_file = QPushButton()
        self.lbl_article_assigned = QLabel()
        self.lbl_create_article_number = QLabel()
        self.btn_create_article = QPushButton()
        self.prgbar_create_article = QProgressBar()
        self.sb_create_info = QStatusBar()
        self.sb_create_warning = QStatusBar()
        self.sb_required = QStatusBar()
        self.frm_create_article.layout.addWidget(self.lbl_frame_create, 0, 0, 1, 7)
        self.frm_create_article.layout.addWidget(self.lbl_machine, 1, 0, 1, 1)
        self.frm_create_article.layout.addWidget(self.lbl_required_1, 1, 1, 1, 1)
        self.frm_create_article.layout.addWidget(self.cbb_machine, 1, 2, 1, 4)
        self.frm_create_article.layout.addWidget(self.prgbar_create_article, 1, 6, 6, 1)
        self.frm_create_article.layout.addWidget(self.lbl_family, 2, 0, 1, 1)
        self.frm_create_article.layout.addWidget(self.lbl_required_2, 2, 1, 1, 1)
        self.frm_create_article.layout.addWidget(self.cbb_family, 2, 2, 1, 4)
        self.frm_create_article.layout.addWidget(self.lbl_element, 3, 0, 1, 1)
        self.frm_create_article.layout.addWidget(self.lbl_required_3, 3, 1, 1, 1)
        self.frm_create_article.layout.addWidget(self.cbb_element, 3, 2, 1, 4)
        self.frm_create_article.layout.addWidget(self.lbl_designation, 4, 0, 1, 1)
        self.frm_create_article.layout.addWidget(self.lbl_required_4, 4, 1, 1, 1)
        self.frm_create_article.layout.addWidget(self.le_designation, 4, 2, 1, 4)
        self.frm_create_article.layout.addWidget(self.lbl_reference, 5, 0, 1, 1)
        self.frm_create_article.layout.addWidget(self.lbl_required_5, 5, 1, 1, 1)
        self.frm_create_article.layout.addWidget(self.le_reference, 5, 2, 1, 4)
        self.frm_create_article.layout.addWidget(self.lbl_supplier, 6, 0, 1, 1)
        self.frm_create_article.layout.addWidget(self.lbl_required_6, 6, 1, 1, 1)
        self.frm_create_article.layout.addWidget(self.le_supplier, 6, 2, 1, 4)
        self.frm_create_article.layout.addWidget(self.lbl_article_placed_on_machine, 7, 0, 1, 1)
        self.frm_create_article.layout.addWidget(self.le_article_placed_on_machine, 7, 2, 1, 2)
        self.frm_create_article.layout.addWidget(self.btn_search_file, 7, 4, 4, 3)
        self.frm_create_article.layout.addWidget(self.lbl_image_product, 8, 0, 1, 1)
        self.frm_create_article.layout.addWidget(self.lbl_image_file, 8, 2, 1, 2)
        self.frm_create_article.layout.addWidget(self.lbl_article_assigned, 9, 0, 1, 1)
        self.frm_create_article.layout.addWidget(self.lbl_create_article_number, 9, 2, 1, 2)
        self.frm_create_article.layout.addWidget(self.sb_required, 10, 0, 1, 1)
        self.frm_create_article.layout.addWidget(self.btn_create_article, 10, 2, 1, 2)
        self.frm_create_article.layout.addWidget(self.sb_create_info, 11, 0, 1, 7)
        self.frm_create_article.layout.addWidget(self.sb_create_warning, 12, 0, 1, 7)
        self.main_layout.addWidget(self.lbl_title_create)
        self.main_layout.addWidget(self.frm_create_article)
        self.setLayout(self.main_layout)

    def init_tab_create_widgets_property(self):
        # lbl_title_create
        self.lbl_title_create.setText("Formulaire de création d'un Code Article")
        self.lbl_title_create.setObjectName("lbl_title_create")
        self.lbl_title_create.setAlignment(Qt.AlignCenter)
        self.lbl_title_create.setMaximumHeight(50)
        # lbl_frame_create
        self.lbl_frame_create.setText("Remplissez les zones suivantes")
        self.lbl_frame_create.setObjectName("lbl_frame_create")
        self.lbl_frame_create.setMaximumHeight(50)
        self.lbl_frame_create.setAlignment(Qt.AlignCenter)
        # setText & setObjectName for all lbl required
        list_lbl_required = [self.lbl_required_1, self.lbl_required_2, self.lbl_required_3,
                             self.lbl_required_4,self.lbl_required_5, self.lbl_required_6]
        list_lbl_step_required = [self.lbl_machine, self.lbl_family, self.lbl_element,
                                  self.lbl_designation, self.lbl_reference, self.lbl_supplier]
        for key, value in constant.DICT_STEP.items():
            list_lbl_step_required[key-1].setText(str(key) + " : " + value + " :")
            list_lbl_step_required[key-1].setObjectName("lbl_information_article")
            list_lbl_required[key-1].setText("👉")
            list_lbl_required[key-1].setMaximumWidth(20)
        # lbl_article_placed_on_machine
        self.lbl_article_placed_on_machine.setText("Emplacement sur la Machine :")
        self.lbl_article_placed_on_machine.setObjectName("lbl_information_article")
        # lbl_image_product
        self.lbl_image_product.setText("Image de l'Article :")
        self.lbl_image_product.setObjectName("lbl_information_article")
        # lbl_image_file
        self.lbl_image_file.setObjectName("lbl_image_file")
        self.lbl_image_file.setText("Non disponible pour le moment")
        self.lbl_image_file.setMaximumHeight(22)
        # cbb_machine
        self.cbb_machine.setEditable(False)
        # cbb_family
        self.cbb_family.setEditable(False)
        # cbb_element
        self.cbb_element.setEnabled(False)
        self.cbb_element.setEditable(False)
        # le_designation
        self.le_designation.setPlaceholderText("Renseigner le type de l'article")
        # le_reference
        self.le_reference.setPlaceholderText("Renseigner la référence de l'article")
        # le_supplier
        self.le_supplier.setPlaceholderText("Renseigner le fournisseur ou la marque de l'article")
        # le_article_placed_on_machine
        self.le_article_placed_on_machine.setPlaceholderText("Facultatif")
        # btn_search_file
        # Todo : later maybe / btn disabled unless needed
        self.btn_search_file.setEnabled(False)
        self.btn_search_file.setObjectName("btn_search_file")
        self.btn_search_file.setText("Cliquez ici\npour sélectionner\nune image du produit\n\n(Facultatif)")
        self.btn_search_file.setMaximumSize(300, 300)
        self.btn_search_file.setToolTip("Fonction non disponible pour le moment")
        # lbl_article_assigned
        self.lbl_article_assigned.setText("Code Article attribué :")
        self.lbl_article_assigned.setObjectName("lbl_information_article")
        # lbl_create_article
        self.lbl_create_article_number.setText("*" * 10)
        self.lbl_create_article_number.setStyleSheet(constant_qss.LBL_CREATE_ARTICLE_NUMBER_NOK)
        self.lbl_create_article_number.setAlignment(Qt.AlignCenter)
        self.lbl_create_article_number.setMaximumHeight(40)
        # btn_create_article
        self.btn_create_article.setText("Créer Article")
        self.btn_create_article.setStyleSheet(constant_qss.BTN_CREATE_ARTICLE_NOK)
        self.btn_create_article.setMinimumHeight(60)
        self.btn_create_article.setMaximumHeight(60)
        self.btn_create_article.setEnabled(False)
        # prgbar_create_article
        self.prgbar_create_article.setObjectName("prgbar_create_article")
        self.prgbar_create_article.setAlignment(Qt.AlignCenter)
        self.prgbar_create_article.setOrientation(Qt.Vertical)
        self.prgbar_create_article.setInvertedAppearance(True)
        self.prgbar_create_article.setValue(0)
        # sb_required
        self.sb_required.setStyleSheet(constant_qss.SB_REQUIRED)
        self.sb_required.setSizeGripEnabled(False)
        self.sb_required.setMaximumHeight(30)
        self.sb_required.setMaximumWidth(220)
        self.sb_required.showMessage("👉 Zone Obligatoire à remplir")
        # sb_crete_info
        self.sb_create_info.setStyleSheet(constant_qss.SB_CREATE_INFO_NOK)
        self.sb_create_info.setSizeGripEnabled(False)
        self.sb_create_info.setMaximumHeight(30)
        self.sb_create_info.showMessage(constant.MESSAGE_STATUS_INFO.format(1, constant.DICT_STEP[1]))
        # sb_create_warning
        self.sb_create_warning.setStyleSheet(constant_qss.SB_CREATE_WARNING_NOK)
        self.sb_create_warning.setSizeGripEnabled(False)
        self.sb_create_warning.setMaximumHeight(30)
        self.sb_create_warning.showMessage(constant.MESSAGE_STATUS_WARNING_NOK)

    def init_tab_create_connections(self):
        self.cbb_machine.currentTextChanged.connect(self.cbb_machine_changed)
        self.cbb_family.currentTextChanged.connect(self.cbb_family_changed)
        self.cbb_element.currentTextChanged.connect(self.cbb_element_changed)
        self.le_designation.editingFinished.connect(self.le_supplier_changed)
        self.le_designation.textChanged.connect(self.le_designation_changed)
        self.le_reference.editingFinished.connect(self.le_supplier_changed)
        self.le_reference.textChanged.connect(self.le_reference_changed)
        self.le_supplier.editingFinished.connect(self.le_supplier_changed)
        self.le_supplier.textChanged.connect(self.le_supplier_changed)
        self.btn_create_article.released.connect(self.btn_create_article_cliked)

    def init_formular_create(self):
        """initialize the formular at the beggining and after creation of code article"""
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
        """1st step of creation of code article"""
        self.actions_when_formular_changed(step=1, current_text=self.cbb_machine.currentText())

    def cbb_family_changed(self):
        """2nd step of creation of code article"""
        self.cbb_element.clear()  # the element combobox depends on the family combobox
        self.actions_when_formular_changed(step=2, current_text=self.cbb_family.currentText())

    def cbb_element_changed(self):
        """3rd step of creation of code article"""
        self.actions_when_formular_changed(step=3, current_text=self.cbb_element.currentText())

    def le_designation_changed(self):
        """4th step of creation of code article"""
        self.actions_when_formular_changed(step=4, current_text=self.le_designation.text())

    def le_reference_changed(self):
        """5th step of creation of code article"""
        self.actions_when_formular_changed(step=5, current_text=self.le_reference.text())

    def le_supplier_changed(self):
        """6th step of creation of code article"""
        self.actions_when_formular_changed(step=6, current_text=self.le_supplier.text())

    def actions_when_formular_changed(self, step, current_text):
        """list of functions to execute when formular changed"""
        if step in range(self.number_combobox_required + 1):
            self.actions_when_cbb_create_tab_changed(step, current_text)
            self.assign_create_tab_number()
        # define if step is validated
        self.step_create_code_validated[step - 1] = False if current_text == "" else True
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
        middle_code = dict_code[step]["middle_code_nok"] if current_text == "" else dict_code[step]["middle_code_ok"]
        end_code = dict_code[step]["end_code"]

        # update the code article
        self.lbl_create_article_number.setText(start_code + middle_code + end_code)

        if step == 2:
            # enabled combobox cbb_element or not
            self.cbb_element.setEnabled(False if current_text == ""else True)

            # add item in cbb_element
            if current_text != "":
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
        """
        assign the 3 last numbers of code article only if 3 first step are validated

        begin : search the biggest code which starts with 7 first characters of lbl_create_number
        else : add 1 to the biggest code found to complete the new code for the new article
            warning : new_max_number always contains 3 characters -> zfill(3)
        end : update the code article lbl_create_article_number with number_code
        """
        number = self.number_combobox_required
        if sum(self.step_create_code_validated[:number]) == number:
            max_number_found = self.search_max_number()
            new_max_number = max_number_found + 1
            new_max_number = str(new_max_number).zfill(3)
            self.lbl_create_article_number.setText(self.lbl_create_article_number.text()[:7] + new_max_number)

    def search_max_number(self):
        """
        search in DataBase the list of codes
        which starts with 7 first characters of lbl_create_article_number
        and return of the biggest number of this list
        """
        start_number = self.lbl_create_article_number.text()[:7]
        # Todo : search in Database here
        max_number_found = start_number  # for test, use start_number
        return int(max_number_found[-3:])

    def update_create_tab_progress_bar(self):
        """modify progress bar of create tab"""
        self.prgbar_create_article.setValue(
            round(sum(self.step_create_code_validated) * 100 / len(constant.DICT_STEP))
        )

    def modify_create_tab_stylesheet(self):
        """modify stylesheet lbl_create_article_number & btn_create_article if form is completed"""
        if sum(self.step_create_code_validated) == len(constant.DICT_STEP):
            self.lbl_create_article_number.setStyleSheet(constant_qss.LBL_CREATE_ARTICLE_NUMBER_OK)
            self.btn_create_article.setStyleSheet(constant_qss.BTN_CREATE_ARTICLE_OK)
            self.btn_create_article.setEnabled(True)
        else:
            self.lbl_create_article_number.setStyleSheet(constant_qss.LBL_CREATE_ARTICLE_NUMBER_NOK)
            self.btn_create_article.setStyleSheet(constant_qss.BTN_CREATE_ARTICLE_NOK)
            self.btn_create_article.setEnabled(False)

    def modify_create_tab_status_bar(self):
        """modify 2 status bar if form is completed"""
        if sum(self.step_create_code_validated) == len(constant.DICT_STEP):
            self.sb_create_info.showMessage(constant.MESSAGE_STATUS_INFO_OK)
            self.sb_create_info.setStyleSheet(constant_qss.SB_CREATE_INFO_OK)
            self.sb_create_warning.showMessage(constant.MESSAGE_STATUS_WARNING_OK)
            self.sb_create_warning.setStyleSheet(constant_qss.SB_CREATE_WARNING_OK)
        else:
            # search first step which is not validated (False)
            # Todo : to optimize if possible
            for step, value in enumerate(self.step_create_code_validated, start=1):
                if not value:
                    break
            self.sb_create_info.showMessage(constant.MESSAGE_STATUS_INFO.format(step, constant.DICT_STEP[step]))
            self.sb_create_info.setStyleSheet(constant_qss.SB_CREATE_INFO_NOK)
            self.sb_create_warning.showMessage(constant.MESSAGE_STATUS_WARNING_NOK)
            self.sb_create_warning.setStyleSheet(constant_qss.SB_CREATE_WARNING_NOK)

    def btn_create_article_cliked(self):
        """fill the database with the various information transmitted via the form"""
        # Todo create function
        # Todo choice a DataBase
        # begin : fill the DataBase with data in the formular
        # else : display a popup to confirm the creation of code article
        # end : clear the formular to create a new article if needed
        self.init_formular_create()
