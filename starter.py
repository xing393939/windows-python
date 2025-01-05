import os
import importlib.util

def load_and_run_main_py():
    script_name = 'index.py'
    script_path = os.path.join(os.path.dirname(__file__), script_name)

    if os.path.exists(script_path):
        spec = importlib.util.spec_from_file_location("index", script_path)
        index_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(index_module)
        # 检查是否存在 entry_function 函数
        if hasattr(index_module, 'main'):
            entry_func = getattr(index_module, 'main')
            if callable(entry_func):
                print(f"执行 {script_name} 中的 entry_function 函数...")
                entry_func()
            else:
                print(f"{script_name} 中的 entry_function 不是一个可调用函数。")
    else:
        print(f"未找到 {script_name} 文件，请确保它位于与此可执行文件相同的目录中。")

if __name__ == '__main__':
    load_and_run_main_py()
