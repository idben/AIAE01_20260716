from pathlib import Path

write_ptah = Path("aa1234.txt")
write_ptah.write_text("Today...", encoding="utf-8")

# 建立資料夾
working_path = Path("yy123")
write_ptah2 = working_path / "aa" / "bb" / "bb345.txt"
# 建立寫檔目的地的上層路徑
write_ptah2.parent.mkdir(parents=True, exist_ok=True)
write_ptah2.write_text("test test 123", encoding="utf-8")