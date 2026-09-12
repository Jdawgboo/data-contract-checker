"""Validate JSON-like records against small declarative contracts."""
from __future__ import annotations
from typing import Any
TYPE_MAP={"str":str,"int":int,"float":(int,float),"bool":bool,"list":list,"dict":dict}

def validate(record: dict[str, Any], contract: dict[str, dict]) -> list[str]:
    errors=[]
    for name, rule in contract.items():
        if rule.get("required") and name not in record: errors.append(f"missing {name}"); continue
        if name in record and record[name] is not None:
            expected=TYPE_MAP[rule.get("type","str")]
            if not isinstance(record[name], expected) or (rule.get("type")=="int" and isinstance(record[name],bool)): errors.append(f"{name} has wrong type")
    return errors

def validate_many(records: list[dict], contract: dict[str,dict]) -> dict[int,list[str]]:
    return {index: errors for index, record in enumerate(records) if (errors:=validate(record, contract))}

if __name__ == "__main__":
    import json, sys
    payload=json.load(sys.stdin); print(json.dumps(validate_many(payload["records"], payload["contract"]), indent=2, sort_keys=True))
