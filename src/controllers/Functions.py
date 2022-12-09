from src.model.Settings import Settings
import hjson


# read from json file
def read_from_json(file, mode, lvl, sub_lvls):
    with open(file, mode) as json_file:
        data = hjson.load(json_file)
        result = data[sub_lvls[0]]
        for level in range(lvl - 1):
            result = result[sub_lvls[level]]
        return result


# translate
def translate(lang_object):
    language = Settings.read_settings("Language", "language")
    data = read_from_json("json/localisation.hjson", "r", 1, [language])
    try:
        return data[lang_object]
    except KeyError:
        return "error"


# set language settings
def set_language(language, actions):
    Settings.store_setting("Language", "language", language)
    for action in actions.keys():
        if action != language:
            actions[action].setChecked(False)
        actions[language].setChecked(True)

    print(Settings.read_settings("Language", "language"))


# retrieve text from QLineEdit
def get_text_from_mode(display):
    return display.text()


# app mode string
mode = "calc"


def set_mode(_mode):
    global mode
    mode = _mode


def get_mode():
    print(mode)
    return mode
from src.model.Settings import Settings
import hjson


# read from json file
def read_from_json(file, mode, lvl, sub_lvls):
    with open(file, mode, encoding="utf-8") as json_file:
        data = hjson.load(json_file)
        result = data[sub_lvls[0]]
        for level in range(lvl - 1):
            result = result[sub_lvls[level]]
        return result


# translate
def translate(lang_object):
    language = Settings.read_settings("Language", "language")
    data = read_from_json("json/localisation.hjson", "r", 1, [language])
    try:
        return data[lang_object]
    except KeyError:
        return "error"


# set language settings
def set_language(language, actions):
    Settings.store_setting("Language", "language", language)
    for action in actions.keys():
        if action != language:
            actions[action].setChecked(False)
        actions[language].setChecked(True)

    print(Settings.read_settings("Language", "language"))


# retrieve text from QLineEdit
def get_text_from_mode(display):
    return display.text()


# app mode string
mode = "calc"


def set_mode(_mode):
    global mode
    mode = _mode


def get_mode():
    print(mode)
    return mode
