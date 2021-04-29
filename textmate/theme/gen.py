import sys
import json
import jsonc
import xml.etree.ElementTree as ET


M = ["author", "colorSpaceName", "name", "uuid"]
S = [
    "background",
    "foreground",
    "caret",
    "invisibles",
    "lineHighlight",
    "selection",
]


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
    scope: str,
    style: ScopeStyle,
) -> None:
    body = ET.SubElement(root, "dict")
    add_prop(body, "name", name)
    add_prop(body, "scope", scope)
    style_k = ET.SubElement(root, "key")
    style_k.text = "settings"
    style_v = ET.SubElement(root, "dict")
    G = ["background", "foreground"]
    for g in G:
        try:
            if style[g] != None:
                add_prop(style_v, g, style[g])
        except KeyError:
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
