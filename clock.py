from datetime import datetime, timedelta

previousTime = datetime.now()
while True:
    currentTime = datetime.now()
    if currentTime - previousTime < timedelta(seconds=1/30):
        continue
    print(f"{currentTime}\r", end="")
    previousTime = currentTime
