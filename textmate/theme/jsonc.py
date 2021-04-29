import re


def to_json(input: str) -> str:
    RE_CMT = re.compile(
        r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)",
        re.MULTILINE | re.DOTALL,
    )
    RE_COMMA = re.compile(r",([\s|\n]{1,}[\}|\]])")
    try:
        res = RE_CMT.sub(r"\1", input)
        res = RE_COMMA.sub(r"\1", res)
        return res
    except Exception as e:
        # TODO:
        raise e
