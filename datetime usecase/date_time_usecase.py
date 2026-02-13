from datetime import datetime

now = datetime.now()
midnight = datetime(now.year, now.month, now.day)
t = now - midnight

print("Hours:", t.seconds // 3600)
print("Minutes:", (t.seconds % 3600) // 60)
print("Seconds:", t.seconds % 60)

