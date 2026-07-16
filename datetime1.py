from datetime import datetime
# import datetime

today = datetime.now()
week = ["一", "二", "三", "四", "五", "六", "天"]

print(today)
print(f"今天是西元 {today.year} 年 {today.month} 月 {today.day} 日 星期{ week[today.weekday()]}")
