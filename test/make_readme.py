import os

dic_en_en = {}
dic_en_zh = {
    "format": "格式化字符串",
    "list": "列表",
    "if": "判断",
    "print": "输出",
    "set": "集合",
    "sort": "排序",
    "Iteration": "迭代",
    "list comprehensiion": "列表生成式",
    "eval": "eval",
    "lambda": "匿名函数",
    "iterator": "迭代器",
    "recursion": "递归",
    "decorator": "装饰器",
    "filter": "过滤",
    "func as return": "函数返回值",
    "map": "映射",
    "reduce": "聚合",
    "generator": "生成器",
    "decorator with parameter": "带参数的装饰器",
    "partial func": "偏函数",
    "contextor": "上下文管理器",
    "generator yield": "yield生成器",
    "monkey patch": "猴子补丁",
    "coroutines": "协程",
    "duck type": "鸭子类型",
    "coroutines async": "async协程"
}
lan = dic_en_en
file_list = ["", ""]
(dir_list := os.listdir('../LifeIsShort')).sort()

for dir in dir_list:
    max_feature = 0
    dir_files = f"|{dir}|"
    if not os.path.isdir(f'../LifeIsShort/{dir}') or 'pycache' in dir:
        continue
    i = 0
    for file in os.listdir(f'../LifeIsShort/{dir}'):
        if "init" in file or file[-3:] != ".py":
            continue
        i += 1
        title = lan.get((t := file.replace("_.py", "").replace(".py", "").replace("_", " ")), t)
        dir_files += f"[{title}](./LifeIsShort/{dir}/{file})|"
    max_feature = max(i, max_feature)
    file_list.append(dir_files)
max_feature += 4
file_list[0] = "|" + '|' * max_feature
file_list[1] = '|---' * max_feature + '|'

for f in file_list:
    print(f)
