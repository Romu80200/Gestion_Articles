""" define stylesheet constants """

LBL_CREATE_ARTICLE_NUMBER = """
    color: blue;
    font-weight: bold;
    font-size: 11pt;
    border: 5 solid;
    """

LBL_CREATE_ARTICLE_NUMBER_NOK = LBL_CREATE_ARTICLE_NUMBER + """
    background-color: salmon;
    border-bottom-left-radius: 5;
    border-bottom-right-radius: 5;
    border-top-left-radius: 25;
    border-top-right-radius: 25;
    border-color: red;
    """
LBL_CREATE_ARTICLE_NUMBER_OK = LBL_CREATE_ARTICLE_NUMBER + """
    background-color: lime;
    border-bottom-left-radius: 25;
    border-bottom-right-radius: 25;
    border-top-left-radius: 5;
    border-top-right-radius: 5;
    border-color: limegreen;
    """

BTN_CREATE_ARTICLE = """QPushButton {
    font-size: 14pt;
    font-weight: bold;
    border: 5 solid;
    border-radius:30;
    border-style: outset;
    """

BTN_CREATE_ARTICLE_NOK = BTN_CREATE_ARTICLE + """
    background-color:lightgray;
    color: gray;
    border-color: gray;}
    """

BTN_CREATE_ARTICLE_OK = BTN_CREATE_ARTICLE + """
    background-color: lime;
    color: green;
    border-color: green;}
    
    QPushButton:pressed {
    border-style: inset;
    }
    """

SB_CREATE_INFO = """
    font-size: 10pt;
    font-weight: bold;
    border: 1px solid gray;
    border-radius: 15;
"""

SB_CREATE_INFO_OK = SB_CREATE_INFO + """
    background-color: lime;
    color: green;
"""

SB_CREATE_INFO_NOK = SB_CREATE_INFO + """
    background-color: gold;
    color: midnightblue;
"""

SB_CREATE_WARNING = """
    font-size: 10pt;
    font-weight: bold;
    border: 1px solid gray;
    border-radius: 15;
"""

SB_CREATE_WARNING_OK = SB_CREATE_WARNING + """
    background-color: gold;
    color: midnightblue;
"""

SB_CREATE_WARNING_NOK = SB_CREATE_WARNING + """
    background-color: salmon;
    color: midnightblue;
"""
