import os
import shutil

dest_path = "D:\\Bilibili\\xiaoyan"
path = r"D:\Bilibili\843567240"


def gci(filepath):
    files = os.listdir(filepath)
    for file in files:
        full_path = os.path.join(filepath, file)
        if os.path.isdir(full_path):
            gci(full_path)
        else:
            s_path = os.path.join(filepath, full_path)
            file_suffix = os.path.splitext(s_path)[1]
            if file_suffix == ".mp4":
                filename = os.path.splitext(file)[0]
                dest_file = dest_path + filename + ".mp4"
                print(dest_file)
                shutil.move(s_path, dest_file)


if __name__ == '__main__':
    gci(path)
