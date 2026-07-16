from datetime import datetime, timedelta
# import datetime

# 基本用法
today = datetime.now()
week = ["一", "二", "三", "四", "五", "六", "天"]

print(today)
print(f"今天是西元 {today.year} 年 {today.month} 月 {today.day} 日 星期{ week[today.weekday()]}")

# 時間戳計
timestamp01 = int(today.timestamp())
print(f"時間戳計 {timestamp01}")
int1 = 1784184660
time01 = datetime.fromtimestamp(int1)
print(time01)
print(f"今天是西元 {time01.year} 年 {time01.month} 月 {time01.day} 日 星期{ week[time01.weekday()]}")


# 指定日期
datetime01 = datetime(2025, 11, 22, 13, 18)
datetime02 = datetime(2025, 12, 1, 18, 30)
print(f"指定日期是西元 {datetime02.year} 年 {datetime02.month} 月 {datetime02.day} 日 星期{ week[datetime02.weekday()]}")
datetime03 = datetime(2025, 12, 1, 22, 17)
datetime04 = datetime(2025, 12, 1, 22, 17)
# 日期相減會得到 timedelta 物件
timedelta01 = datetime01 - datetime02
timedelta02 = datetime03 - datetime02
# timedelta 物件可以轉成總秒數 .total_seconds()
print(timedelta01.total_seconds())
print(timedelta02.total_seconds())
# 時間物件可以直接比大小
print(datetime01 < datetime02)
print(datetime03 < datetime02)
print(datetime03 == datetime04) # 可以用等號 (==) 相比

# 日期的加減使用 timedelta
next3days = today + timedelta(days=3)
print(next3days)
next2hours = today + timedelta(hours=2)
print(next2hours)

# 指定日期格式 strftime
print(f"{today.strftime("%Y-%m-%d %H:%M:%S")}")
print(f"{today.strftime("%Y 年 %m 月 %d 日 %H:%M:%S")}")

# 轉回日期物件 strptime
datestr01 = "2026-07-16 15:18:03"
datetime05 = datetime.strptime(datestr01, "%Y-%m-%d %H:%M:%S")
print(datetime05)