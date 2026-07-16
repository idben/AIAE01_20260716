# import pathlib
from pathlib import Path




# 組合路徑
base_folder = Path("m01") # 建立基本目錄 Path
path01 = base_folder / "aaa" / "bbb" / "c1.txt" # 由基本目錄往下用 / 接字串
print(path01)

# 取得當前工作目錄
# pathlib.Path.cwd()
print(f"取得當前工作目錄 {Path.cwd()}")


# 目前檔案的目錄的絕對路徑
print(__file__)                          # 路徑字串
print(Path(__file__))                    # Path物件
print(Path(__file__).resolve())          # 整理路徑
print(Path(__file__).resolve().parent)   # 取得上層目錄
base_folder = Path(__file__).resolve().parent
csv_path = base_folder / "dataset_202607160330.csv"
print(csv_path)

# 檔名副檔名的取得
print(csv_path.name)        # 完整當名副檔名
print(csv_path.stem)        # 不含副檔名的檔名
print(csv_path.suffix)      # 副檔名

# 讀取檔案
data = csv_path.read_text(encoding="utf-8")
# print(data)

# 寫入檔案
note_path = Path("note.txt")
note_path.write_text("Hello", encoding="utf-8")