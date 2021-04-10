from typing import Any, Dict, List
from typing_extensions import Literal

KeySymbol = Literal[
    "1",
    "!",
    "2",
    "@",
    "3",
    "#",
    "4",
    "$",
    "5",
    "%",
    "6",
    "^",
    "7",
    "&",
    "8",
    "*",
    "9",
    "(",
    "0",
    ")",
    "`",
    "~",
    "-",
    "_",
    "=",
    "+",
    "[",
    "{",
    "]",
    "}",
    "\\",
    "|",
    ";",
    ":",
    "'",
    '"',
    ",",
    "<",
    ".",
    ">",
    "/",
    "?",
    "[ESC]",
    "[CAPS]",
    "[L_SHIFT]",
    "[R_SHIFT]",
    "[L_CTL]",
    "[R_CTL]",
    "[L_OPT]",
    "[R_OPT]",
    "[L_CMD]",
    "[R_CMD]",
]
KeyCode = Literal[
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "hyphen",
    "equal_sign",
    "international1",
    "international3",
    "delete_or_backspace",
    "return_or_enter",
    "close_bracket",
    "open_bracket",
    "semicolon",
    "quote",
    "backslash",
    "comma",
    "period",
    "slash",
    "grave_accent_and_tilde",
    "",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "left_option",
    "right_option",
    "left_shift",
    "right_shift",
    "left_control",
    "right_control",
    "left_command",
    "right_command",
    "japanese_eisuu",
    "japanese_kana",
    "space_bar",
    "caps_lock",
    "escape",
    "tab",
    "f1",
    "f2",
    "f3",
    "f4",
    "f5",
    "f6",
    "f7",
    "f8",
    "f9",
    "f10",
    "f11",
    "f12",
]
Modifier = Literal["left_shift", "left_alt"]


class ModifierFrom(Dict):
    mandatory: List[str]
    optional: List[str]

    def __init__(
        self, mandatory: List[str], optional: List[str]
    ):
        self.mandatory = mandatory
        self.optional = optional

    def data(self) -> Dict[str, Any]:
        return self.__dict__
