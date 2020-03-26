import os
import re

dic_en = {}
dic_zh = {
    "format": "格式化字符串",
    "list": "列表",
    "if": "判断",
    "print": "输出",
    "set": "集合",
    "sort": "排序",
    "Iteration": "迭代",
    "list comprehension": "列表生成式",
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
    "coroutines async": "async协程",
    "process pool": "线程池",
    "callback":"回调",
}


def make_table(language_dic):
    lines = ["", ""]
    (dir_list := os.listdir('../LifeIsShort')).sort()
    max_example_count = 0

    for dir in dir_list:
        dir_files = f"|{dir}|"
        if not os.path.isdir(f'../LifeIsShort/{dir}') or 'pycache' in dir:
            continue
        i = 0
        for file in os.listdir(f'../LifeIsShort/{dir}'):
            if "init" in file or file[-3:] != ".py":
                continue
            i += 1
            title = language_dic.get((t := file.replace("_.py", "").replace(".py", "").replace("_", " ")), t)
            dir_files += f"[{title}](./LifeIsShort/{dir}/{file})|"
        max_example_count = max(i, max_example_count)
        lines.append(dir_files)
    max_example_count += 1
    lines[0] = "|" + '|' * max_example_count
    lines[1] = '|---' * max_example_count + '|'

    return "\n".join(lines)


def update_readme():
    tasks = [("../readme.md", dic_en), ("../readme_zh.md", dic_zh)]
    for task in tasks:
        with open(task[0], "r+") as f:
            content = f.read()
            f.seek(0)
            f.truncate()
            example_table = make_table(task[1])
            f.write(re.sub(r"<!-- Example:DO NOT MODIFY THIS! -->(.|\n)+<!-- DO NOT MODIFY THIS! -->",
                           f"<!-- Example:DO NOT MODIFY THIS! -->\n{example_table}\n<!-- DO NOT MODIFY THIS! -->",
                           content))
    print(f"Update readme in {len(tasks)} files")


update_readme()
