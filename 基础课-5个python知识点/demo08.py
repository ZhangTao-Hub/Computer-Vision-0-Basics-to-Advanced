"""
author: tao
date: 25.2

演示python dict
"""

dic = {
    "name": "tao",
    "age": 18,
    "height": 180,
    "graduated": True
}

print(dic)
print(dic['name'])
print(len(dic))

dic['weight'] = 70
print(dic)

dic['height'] = 170
print(dic)

del dic['weight']
print(dic)