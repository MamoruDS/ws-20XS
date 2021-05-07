import sys
import json
import jsonc
import xml.etree.ElementTree as ET

from typing import Union


M = ["author", "colorSpaceName", "name", "uuid"]
S = [
    "background",
    "foreground",
    "caret",
    "invisibles",
    "lineHighlight",
    "selection",
]

GLOBAL: dict[str, str] = {}


class ScopeStyle(dict):
    background: str
    foreground: str
    bold: bool
    underline: bool
    italic: bool


def add_prop(
    parent: ET.Element,
    key: str,
    val: str,
    tag="string",
) -> tuple[ET.Element, ET.Element]:
    e_k = ET.SubElement(parent, "key")
    e_k.text = key
    e_v = ET.SubElement(parent, tag)
    e_v.text = val
    return e_k, e_v


def add_scope(
    root: ET.Element,
    name: str,
    scope: Union[str, list[str]],
    style: ScopeStyle,
) -> None:
    body = ET.SubElement(root, "dict")
    add_prop(body, "name", name)
    _scope: str
    if isinstance(scope, str):
        _scope = scope
    else:
        _scope = ",".join(scope)
    add_prop(body, "scope", _scope)
    style_k = ET.SubElement(body, "key")
    style_k.text = "settings"
    style_v = ET.SubElement(body, "dict")
    G = ["background", "foreground"]
    for g in G:
        try:
            c: str = style[g]
            if c != None:
                if c[:1] != "#":
                    c = GLOBAL[c]
                    if len(c) == 0:
                        raise KeyError
                add_prop(style_v, g, c)
        except KeyError:
            # TODO: error message
            pass
    FS = ["bold", "underline", "italic"]
    font_style = []
    for fs in FS:
        try:
            if style[fs]:
                font_style.append(fs)
        except KeyError:
            pass
    if len(font_style):
        add_prop(
            style_v, "fontStyle", " ".join(font_style)
        )
    return


def main() -> None:
    filepath = sys.argv[1]
    f = open(filepath, encoding="utf-8")
    profile = json.loads(jsonc.to_json(f.read()))
    f.close()

    # load initial global color
    try:
        for c in profile["global"].keys():
            GLOBAL[c] = profile["global"][c]
    except KeyError:
        pass

    body = ET.Element("plist", version="1.0")
    data = ET.SubElement(body, "dict")
    for k in M:
        add_prop(data, k, profile[k])
    settings_top_k = ET.SubElement(data, "key")
    settings_top_k.text = "settings"
    settings_top = ET.SubElement(data, "array")

    settings_g_ctr = ET.SubElement(
        settings_top, "dict"
    )
    settings_g_k = ET.SubElement(settings_g_ctr, "key")
    settings_g_k.text = "settings"
    settings_g_v = ET.SubElement(
        settings_g_ctr, "dict"
    )
    for k in S:
        add_prop(
            settings_g_v, k, profile["settings"][k]
        )

    for scope in profile["settings"]["scopes"]:
        add_scope(
            settings_top,
            scope["name"],
            scope["scope"],
            scope["prop"],
        )
    print(ET.tostring(body).decode(encoding="utf-8"))


if __name__ == "__main__":
    main()
