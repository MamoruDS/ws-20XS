import sys
import json
import jsonc

filepath = sys.argv[1]
f = open(filepath, encoding="utf-8")
d = json.loads(jsonc.to_json(f.read()))
sys.stdout.write(f"{json.dumps(d, indent=4)}\n")

