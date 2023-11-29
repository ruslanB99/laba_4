import json

def task(file_name):
    with open(file_name) as f:
        total = sum([d['score'] * d['weight'] for d in json.load(f)])
    return round(total,3)
print (task('input.json'))