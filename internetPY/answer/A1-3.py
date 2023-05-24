import yaml
import json

with open('read.json',encoding='utf-8-sig') as file:
    data = json.load(file)

with open ('write.yaml','w',encoding="utf-8")as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)