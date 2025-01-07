import os
import sys
import chardet
import importlib.util


def get_executable_dir():
    # 检查是否为打包后的可执行文件
    if getattr(sys, 'frozen', False):
        executable_dir = os.path.dirname(sys.executable)
    else:
        executable_dir = os.path.dirname(os.path.abspath(__file__))
    return executable_dir


def replace_main_with_index(input_file, output_file):
    # 读取文件，检查文件的编码
    with open(input_file, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    with open(input_file, 'r', encoding=encoding.lower()) as file:
        data = file.read()
    new_data = data.replace("__name__ == '__main__'", "__name__ == 'index'")
    # 将替换后的内容写入输出文件
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(new_data)


def load_and_run_main_py():
    script_name = 'index.py'
    script_path = os.path.join(get_executable_dir(), script_name)
    if os.path.exists(script_path):
        replace_main_with_index(script_path, script_path)
        spec = importlib.util.spec_from_file_location("index", script_path)
        index_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(index_module)
    else:
        print(f"未找到 {script_path}，请确保它位于与此可执行文件相同的目录中。")


if __name__ == '__main__':
    load_and_run_main_py()
    input("请按回车键退出...")
