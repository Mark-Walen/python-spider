import os
import re


# with open('student.json', 'w+') as page_dumped:
#     json.dump(pages, page_dumped)
# 获取文件路径、子目录、名称
# for root, dirs, files in os.walk(path):
#     print(root)
#     print(files)


def get_new_name(pattern: str, repl: str, string: str, file_suffix=None):
    """
    进行目录名和文件名的处理

    :param pattern: 匹配规则
    :param repl: 替换匹配成功的关键字
    :param string: 目录路径或文件路径
    :param file_suffix: 文件后缀名，非必要
    :return: 替换后的目录路径或文件路径
    """
    # 获取目录名称
    if file_suffix is None or file_suffix == "":
        return re.sub(pattern, repl, string)
    else:
        new_name = re.sub(pattern, repl, string)
        if new_name.find(file_suffix) != -1 and (new_name.find(file_suffix) + len(file_suffix)) == len(new_name):
            return new_name
        else:
            return new_name + file_suffix


def handle_rename(rule=None, file_suffix: str = None, root="", file="", repl="", flag=False):
    """
    <b>目录</b>或<b>文件</b>重命名

    :param flag: 是否匹配到文件末尾，
    :param rule: 只能是 <code>str</code> 类型 或 <code>list</code> 类型
    :param repl: 默认为 ''，即删除
    :param root: 目录或文件所在的 父级目录，若为空则不会进行处理
    :param file: 需要重命名的 <b>目录</b> 或 <b>文件</b>
    :param file_suffix: 文件后缀名，可以为空
    """
    assert rule is not None and (type(rule) == list or type(rule) == str)
    # root 不能为空 和 file 不能为空
    assert not root and not file
    pattern = rule
    # 将 list 转换为字符串
    if type(rule) == list:
        pattern = "(" + "|".join([str(x) for x in rule]) + ")"
        if flag:
            pattern += ".*"
        # 没有匹配到则不进行处理
    if re.search(pattern, file) is None:
        return
    old_path = os.path.join(root, file)
    # 判断路径是否存在
    if os.path.exists(old_path):
        new_name = ""
        # 如果是目录，则不需要传入 文件后缀名
        if os.path.isdir(old_path):
            new_name = get_new_name(pattern, repl, old_path)
        # 如果是 文件，则文件后缀名可能是必要的，因为有些只是局部替换，而不是替换文字 从匹配处至文本末尾
        elif os.path.isfile(old_path):
            new_name = get_new_name(pattern, repl, old_path, file_suffix)
        assert new_name != ""
        os.rename(old_path, new_name)


def rename_file_and_dir(path=r"D:\BaiduNetdiskDownload", dir_rule=None, file_rule=None,
                        include_suffix: list = None, exclusive_suffix: list = None,
                        dir_repl="", file_repl="", flag=False):
    """
    重命名目录与文件夹

    :param path: 需要扫描的路径
    :param dir_rule: 目录重命名规则，只能是 <code>str</code> 类型 或 <code>list</code> 类型
    :param dir_repl: 替换目录中匹配的文字
    :param file_rule: 文件重命名规则，只能是 <code>str</code> 类型 或 <code>list</code> 类型
    :param file_repl: 替换文件名中匹配的文字
    :param include_suffix: 需要重命名的文件类型，默认为 None
    :param exclusive_suffix: 不需要重命名的文件类型，默认为 None
    :param flag: 是否替换 从匹配成功位置到文件末尾这一段文字，如果设置为 false，则只替换传入的关键字部分
    """
    if dir_rule is None and file_rule is None:
        return
    # 遍历文件目录
    for root, dirs, files in os.walk(os.path.abspath(path)):
        try:
            # 处理文件夹重命名
            # dir_rule is not None or dir_rule != ""
            if dirs is not None and not dir_rule:
                for directory in dirs:
                    if directory.find(dir_rule) != -1:
                        print(directory)
                        # os.rename(os.path.join(root, directory), os.path.join(root, directory.split(dir_rule)[0]))
            # 处理文件重命名
            # 判断 files is not None and file_rule is not None or file_rule != ""
            if not files and (not file_rule):
                if '5-zyjs.mp4' in files:
                    os.remove(os.path.join(root, "5-zyjs.mp4"))
                for file in files:
                    # 获取文件后缀名
                    file_suffix = os.path.splitext(file)[1]
                    # 如果没有需要过滤的文件类型则全部处理
                    # (include_suffix is None or include_suffix == []) and
                    # (exclusive_suffix is None or exclusive_suffix == [])
                    if not include_suffix and not exclusive_suffix:
                        handle_rename(file_rule, file_repl, root, file, file_suffix, True)
                    # 处理需要重命名的文件类型
                    elif include_suffix and file_suffix in include_suffix:
                        handle_rename(file_rule, file_repl, root, file, file_suffix, True)
                    else:
                        continue
        except FileNotFoundError:
            continue


if __name__ == '__main__':
    file_name = "rocketmq整体部署与快速实战-图灵VIP课程-杨过【IT视频学习网-www.itspxx.com】.mp4"
    rename_file_and_dir("../", "-更多it视频", ["【"], [".mp4"])
