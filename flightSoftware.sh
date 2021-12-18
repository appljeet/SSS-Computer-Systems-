#!/bin/bash
# execute all async programs and main.py on pi startup
python3 asyncBattery.py & python3 asyncBeacon.py & python3 asyncHealthFile.py & python3 asyncScheduleTimer.py & python3 main.py