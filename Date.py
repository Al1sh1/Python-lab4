from datetime import datetime, timedelta

# 1
current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print("Date after subtracting 5 days:", new_date.strftime("%Y-%m-%d"))

# 2
today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

# 3
datetime_without_microseconds = current_date.replace(microsecond=0)
print("Datetime without microseconds:", datetime_without_microseconds)

# 4
date1 = datetime(2025, 2, 10, 14, 30, 0)
date2 = datetime(2025, 2, 14, 18, 45, 0)
difference = abs((date2 - date1).total_seconds())
print(f"Difference in seconds: {difference}")
