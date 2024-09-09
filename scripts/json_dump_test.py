import json

json_p = {
    "name": "sagar lathiya",
    "age": 27,
    "email": "abc@abc.com"
}

p1 = {
    "field1": "value1",
    "field2": "value2",
    "field3": "value3",
    "field4": "value4",
    "field5": "value5",
    "field6": "value6",
    "json_p": json_p
}

p1_json = json.dumps(p1)

print(p1_json)