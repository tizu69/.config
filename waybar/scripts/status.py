#!/usr/bin/env python3
import json
from datetime import datetime
from hyprpy import Hyprland

# config
work_times = [
    [("08:00am", "04:00pm")],  # Monday
    [("08:00am", "04:00pm")],  # Tuesday
    [("08:00am", "04:00pm")],  # Wednesday
    [("08:00am", "04:00pm")],  # Thursday
    [("08:00am", "04:00pm")],  # Friday
    [],  # Saturday
    [],  # Sunday
]
bad_windows = ["vesktop"]

now = datetime.now()
if work_times[now.weekday()]:
    start_str, end_str = work_times[now.weekday()][0]
    start_time = datetime.strptime(start_str, "%I:%M%p").replace(
        year=now.year, month=now.month, day=now.day
    )
    end_time = datetime.strptime(end_str, "%I:%M%p").replace(
        year=now.year, month=now.month, day=now.day
    )

    if now < start_time:
        time_until = int((start_time - now).total_seconds() / 60)
        if time_until < 60:
            status = f"󰃖 in {time_until:02d}m"
        else:
            status = f"󰃖 in {time_until//60:02d}:{time_until%60:02d}"
    elif now > end_time:
        status = ""
    else:
        instance = Hyprland()
        window = instance.get_active_window()
        if window.wm_class in bad_windows:
            print(json.dumps({"text": "󰃖 GET BACK TO WORK!", "class": "red-flash"}))
            exit(0)

        time_left = int((end_time - now).total_seconds() / 60)
        if time_left < 60:
            status = f"󰃖 -{time_left+1:02d}m"
        else:
            status = f"󰃖 -{time_left//60:02d}:{time_left%60:02d}"
else:
    status = ""

print(json.dumps({"text": f"{status}", "class": "" if status == "" else "red"}))
