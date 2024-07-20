# 获取学校id信息
import json

if __name__ == '__main__':
    f = open('2c.txt', 'r', encoding='utf-8').readlines()
    dt = {}
    for item in f:
        k, v = item.strip().split(':')
        dt[k] = v
    print(dt)
