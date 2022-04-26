import os


def file_scan(directory=r"C:\\"):
    filename_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1] == ".ts":
                filename_list.append("file '" + file + "'\r")
    return filename_list


if __name__ == '__main__':
    for item in file_scan("C:\\Users\\BlueVincent\\Desktop\\video-dbofporn_com-16412291191522"):
        with open("test.txt", "a") as f:
            f.write(item)
