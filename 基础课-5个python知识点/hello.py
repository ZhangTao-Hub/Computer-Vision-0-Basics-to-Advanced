"""
author: tao
date: 25.2

演示程序: 使用终端进行代码运行，并输入参数
"""
from argparse import ArgumentParser

parse = ArgumentParser()
parse.add_argument("--width", type=int, default=960, help="宽度")
parse.add_argument("--height", type=int, default=540, help="高度")
args = parse.parse_args()

area = int(args.width * args.height)
print(f"area = {area}")