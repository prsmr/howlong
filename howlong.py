#!/usr/bin/python3
import sys
from datetime import datetime

def calculate_time_difference(target_date_str):
    formats = ["%d/%m/%Y %H:%M:%S", "%d/%m/%Y %H:%M", "%d/%m/%Y %H", "%d/%m/%Y", "%d.%m.%Y", "%d.%m.%Y %H:%M:%S", "%d.%m.%Y %H:%M", "%d.%m.%Y %H"]
    target_date = None
    
    # try to parse the date
    for date_format in formats:
        try:
            target_date = datetime.strptime(target_date_str, date_format)
            break
        except ValueError:
            continue
    
    if not target_date:
        print("Please enter a valid date.")
        return
    
    now = datetime.now()
    
    time_difference = target_date - now
    
    # output
    if time_difference.total_seconds() > 0:
        days = time_difference.days
        seconds = time_difference.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        now_f = now.strftime("%d/%m/%Y %H:%M:%S")


        print(f"Time from {now_f} to {target_date_str}: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
    else:
        print("The date is in the past.")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please enter a valid date.")
    else:
        calculate_time_difference(sys.argv[1])
