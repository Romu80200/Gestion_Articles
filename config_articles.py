"""
Temporary file :
    Todo : transform this file in json file because it will be modify via form or create a Dataase
"""

"""
TO RESPECT :
    /!\ do not modify the keys : "machine", "famille" et "element"
    machine -> 4 characters numerics required
    famille -> 1 character numeric required
    element -> 2 characters numerics required

Avoid accents
"""


config = {
    "machine": {
        "": "vide",
        "Machine1": "8031",
        "Machine2": "8050",
        "Machine3": "8038",
        "Machine4": "8065",
        "Machine5": "8066",
    },
    "famille": {
        "": "vide",
        "Famille1": "0",
        "Famille2": "1",
        "Famille3": "2",
        "Famille4": "3",
    },
    "element": {
        "": {"": "vide"},
        "Famille1": {
            "": "vide",
            "Item1": "00",
            "Item2": "01",
            "Item3": "02",
            "Item4": "11",
            "Item5": "15",
            "Item6": "27",
        },
        "Famille2": {
            "": "vide",
            "Item1": "03",
            "Item2": "05",
            "Item3": "06",
            "Item4": "36",
            "Item5": "54",
            "Item6": "75",
        },
        "Famille3": {
            "": "vide",
            "Item1": "09",
            "Item2": "12",
            "Item3": "24",
            "Item4": "75",
            "Item5": "95",
            "Item6": "99",
        },
        "Famille4": {
            "": "vide",
            "Item1": "05",
            "Item2": "07",
            "Item3": "10",
            "Item4": "38",
            "Item5": "45",
            "Item6": "88",
        },
    },
}
