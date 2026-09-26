import json
def save(records,filename="data.json"):
    data=[app for app in records]
    with open(filename,"w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=4)


def load(filename="data.json"):
    try:
        with open(filename,"r",encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        pass
    return []

