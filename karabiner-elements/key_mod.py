import json
from typing import Any, Dict, List, Literal

from key_types import KeyCode, ModifierFrom, KeySymbol
from key_mapping import jis_keys


class Rule(Dict):
    desc: str
    sub_rules: List[Dict[str, Any]]

    def __init__(self, description: str):
        self.desc = description
        self.sub_rules = []

    def add(
        self,
        from_key_code: KeyCode,
        to_symbol: KeySymbol,
        from_modifiers: ModifierFrom = None,
        rule_type: Literal["basic"] = "basic",
    ) -> None:
        key_from: Dict[str, Any] = {
            "key_code": from_key_code,
        }
        if from_modifiers != None:
            key_from[
                "modifiers"
            ] = from_modifiers.data()
        data = {
            "from": key_from,
            "to": [],
            "type": rule_type,
        }
        key = jis_keys[to_symbol]
        data["to"].append(key.data())
        self.sub_rules.append(data)


class Mod(Dict):
    title: str
    rules: List[Rule]

    def __init__(self, title: str):
        self.title = title
        self.rules = []

    def add_rule(self, description: str) -> Rule:
        _rule = Rule(description)
        self.rules.append(_rule)
        return _rule

    def data(self) -> Dict[str, Any]:
        data = {"title": self.title, "rules": []}
        for rule in self.rules:
            body = {
                "description": rule.desc,
                "manipulators": [],
            }
            for sub in rule.sub_rules:
                body["manipulators"].append(sub)
            data["rules"].append(body)
        return data

    def __str__(self) -> str:
        return json.dumps(self.data())
