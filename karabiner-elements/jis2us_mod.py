import json
from key_mod import Mod
from key_types import ModifierFrom

from_mod_shift = ModifierFrom(["shift"], ["caps_lock"])
from_common = ModifierFrom([], ["caps_lock"])
m = Mod("WS-20XS")
sub = m.add_rule("JIS->US (generated", from_common)
sub.add("1", "!", from_mod_shift)
sub.add("2", "@", from_mod_shift)
sub.add("3", "#", from_mod_shift)
sub.add("4", "$", from_mod_shift)
sub.add("5", "%", from_mod_shift)
sub.add("6", "^", from_mod_shift)
sub.add("7", "&", from_mod_shift)
sub.add("8", "*", from_mod_shift)
sub.add("9", "(", from_mod_shift)
sub.add("0", ")", from_mod_shift)
sub.add("hyphen", "-")
sub.add("hyphen", "_", from_mod_shift)
sub.add("equal_sign", "=")
sub.add("equal_sign", "+", from_mod_shift)
sub.add("international3", "`")
sub.add("international3", "~", from_mod_shift)
sub.add("open_bracket", "[")
sub.add("open_bracket", "{", from_mod_shift)
sub.add("close_bracket", "]")
sub.add("close_bracket", "}", from_mod_shift)
sub.add("semicolon", ";")
sub.add("semicolon", ":", from_mod_shift)
sub.add("quote", "'")
sub.add("quote", '"', from_mod_shift)
sub.add("backslash", "\\")
sub.add("backslash", "|", from_mod_shift)
sub.add("comma", ",")
sub.add("comma", "<", from_mod_shift)
sub.add("period", ".")
sub.add("period", ">", from_mod_shift)
sub.add("slash", "/")
sub.add("slash", "?", from_mod_shift)
sub.add("left_control", "[CAPS]")
sub.add("caps_lock", "[ESC]")
sub.add("left_option", "[L_CTL]")
sub.add("left_command", "[L_OPT]")
sub.add("japanese_eisuu", "[L_CMD]")
sub.add("japanese_kana", "[R_CMD]")
sub.add("right_command", "[R_OPT]")
sub.add("international1", "[R_CTL]")

print(json.dumps(m.data()))
