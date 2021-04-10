import json
from typing import Any, Dict, List

from key_types import Modifier, KeySymbol, KeyCode


class Key(Dict):
    keycode: KeyCode
    modifiers: List[Modifier]

    def __init__(
        self,
        keycode: KeyCode,
        modifiers: List[Modifier] = [],
    ):
        self.keycode = keycode
        self.modifiers = modifiers

    def data(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {
            "key_code": self.keycode
        }
        if len(self.modifiers) != 0:
            data["modifiers"] = self.modifiers
        return data

    def __str__(self) -> str:
        return json.dumps(self.data())

    def __repr__(self) -> str:
        return self.__str__()


jis_keys: Dict[KeySymbol, Key] = {}

jis_keys["`"] = Key("grave_accent_and_tilde")
jis_keys["1"] = Key("1")
jis_keys["2"] = Key("2")
jis_keys["3"] = Key("3")
jis_keys["4"] = Key("4")
jis_keys["5"] = Key("5")
jis_keys["6"] = Key("6")
jis_keys["7"] = Key("7")
jis_keys["8"] = Key("8")
jis_keys["9"] = Key("9")
jis_keys["0"] = Key("0")
jis_keys["~"] = Key(
    "grave_accent_and_tilde", ["left_shift"]
)
jis_keys["-"] = Key("hyphen")
jis_keys["="] = Key("hyphen", ["left_shift"])
jis_keys["!"] = Key("1", ["left_shift"])
jis_keys["@"] = Key("open_bracket")
jis_keys["#"] = Key("3", ["left_shift"])
jis_keys["$"] = Key("4", ["left_shift"])
jis_keys["%"] = Key("5", ["left_shift"])
jis_keys["^"] = Key("equal_sign")
jis_keys["&"] = Key("6", ["left_shift"])
jis_keys["*"] = Key("quote", ["left_shift"])
jis_keys["("] = Key("8", ["left_shift"])
jis_keys[")"] = Key("9", ["left_shift"])
jis_keys["_"] = Key("international1", ["left_shift"])
jis_keys["+"] = Key("semicolon", ["left_shift"])
#
jis_keys["["] = Key("close_bracket")
jis_keys["{"] = Key("close_bracket", ["left_shift"])
jis_keys["]"] = Key("backslash")
jis_keys["}"] = Key("backslash", ["left_shift"])
jis_keys["\\"] = Key("international3", ["left_alt"])
jis_keys["|"] = Key("international3", ["left_shift"])
jis_keys[";"] = Key("semicolon")
jis_keys[":"] = Key("quote")
jis_keys["'"] = Key("7", ["left_shift"])
jis_keys['"'] = Key("2", ["left_shift"])
jis_keys[","] = Key("comma")
jis_keys["<"] = Key("comma", ["left_shift"])
jis_keys["."] = Key("period")
jis_keys[">"] = Key("period", ["left_shift"])
jis_keys["/"] = Key("slash", ["left_shift"])
jis_keys["?"] = Key("slash")
#
jis_keys["[ESC]"] = Key("escape")
jis_keys["[CAPS]"] = Key("caps_lock")
jis_keys["[L_SHIFT]"] = Key("left_shift")
jis_keys["[R_SHIFT]"] = Key("right_shift")
jis_keys["[L_CTL]"] = Key("left_control")
jis_keys["[R_CTL]"] = Key("right_control")
jis_keys["[L_OPT]"] = Key("left_option")
jis_keys["[R_OPT]"] = Key("right_option")
jis_keys["[L_CMD]"] = Key("left_command")
jis_keys["[R_CMD]"] = Key("right_command")

