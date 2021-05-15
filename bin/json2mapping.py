import json
import sys

data = """
[
  {
    "action": "ADD_IR",
    "currency": "USD_SOFR",
    "ir_curves": [
      {
        "points": [
          {
            "date": "2019-05-18",
            "df": 3.96
          },
          {
            "date": "2020-05-18",
            "df": 3.8
          }
        ],
        "type": "BASE_CURVE",
        "identifier": "USD_SOFR",
        "foo": "bar"
      }
    ]
  },
  {
    "action": "ADD_IR",
    "currency": "EUR_ESTR",
    "ir_curves": [
      {
        "points": [
          {
            "date": "2019-05-18",
            "df": 3.96
          },
          {
            "date": "2020-05-18",
            "df": 3.8
          }
        ],
        "type": "BASE_CURVE",
        "identifier": "EUR_ESTR",
        "foo": "bar"
      }
    ]
  }
]
"""

if len(sys.argv) > 1:
  with open(sys.argv[1], 'r') as f:
    data = f.read()

def main():
    mapping = analyze(json.loads(data), {})
    fmt = {"mapping":mapping}
    output = json.dumps(fmt,indent=2)
    if sys.getsizeof(output) < 20000:
        print(output)
    with open("format.json", "w") as out:
        out.write(output)


def analyze(node, mapping):
    if type(node) == dict:
        mapping = analyze_obj(node, mapping)
    if type(node) == list:
        mapping = analyze_arr(node, mapping)
    return mapping

def analyze_obj(node, mapping):
    mapping["type"] = "object"
    mapping["children"] = []
    for name, value in node.items():
        child_mapping = analyze(value, {"name": name})
        mapping["children"].append(child_mapping)
    return mapping

def analyze_arr(node, mapping):
    mapping["type"] = "array"
    mapping["children"] = []
    for child in node:
        child_mapping = analyze(child, {})
        if not mapping["children"]:
            mapping["children"].append(child_mapping)
        elif not any([x == child_mapping for x in mapping["children"]]):
            mapping["children"].append(child_mapping)
    return mapping

if __name__ == '__main__':
    main()
