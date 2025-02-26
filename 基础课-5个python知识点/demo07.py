"""
author: tao
date: 25.2

演示python list与tuple区别
"""

fruit_list = ["apple", "banana", "cherry"]
fruit_list[1] = "pear"

# 'tuple' object does not support item assignment
fruit_tuple = ("apple", "banana", "cherry")
fruit_tuple[1] = "pear"

