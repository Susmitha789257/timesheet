from datetime import datetime, timedelta
from tabulate import tabulate
import os

schedule = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

headers = ["Start", "End", "Activity", "Duration"]

while True:
    clear_screen()
    print("🕒 Your Daily Schedule:")
    print(tabulate(schedule, headers=headers, tablefmt="fancy_grid"))
    print("\n📥 Add a new activity (or type 'done' to finish)\n")

    activity = input("Activity: ")
    if activity.lower() == 'done':
        break

    start = input("Start time (HH:MM:SS): ")
    end = input("End time (HH:MM:SS): ")

    try:
        start_dt = datetime.strptime(start, "%H:%M:%S")
        end_dt = datetime.strptime(end, "%H:%M:%S")
        if end_dt < start_dt:
            end_dt += timedelta(days=1)
        duration = end_dt - start_dt
        schedule.append([start, end, activity, str(duration)])
    except:
        input("❌ Invalid time format. Press Enter to try again...")
