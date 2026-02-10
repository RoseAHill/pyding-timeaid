from time import strftime, sleep
from playsound3 import playsound

DING_TEXT = "Ding @ {time}"
DING_CONFIG = {
    0: "sounds/current/hour_00.mp3",
    15: "sounds/current/quarter_15.mp3",
    30: "sounds/current/half_30.mp3",
    45: "sounds/current/quarter_45.mp3"
}

NOTIFICATION_TEXT = "Hey! It's {time}"
MINUTE_INTERVAL_NOTIFY = {
    4: "sounds/current/notification.mp3"
}

START_TIME = 800
END_TIME = 2200
NIGHT_OWL = START_TIME > END_TIME

CHECK_RANGE = range(START_TIME, END_TIME, 2)

def notify(interval):
    if interval in MINUTE_INTERVAL_NOTIFY.keys():
        playsound(MINUTE_INTERVAL_NOTIFY[interval])
        print(NOTIFICATION_TEXT.format(time=strftime("%I:%M%p")))
    pass

def ding(min):
    if min in DING_CONFIG.keys():
            playsound(DING_CONFIG[min])
            print(DING_TEXT.format(time=strftime("%I:%M%p")))

def compare_time():
    current_hour = int(strftime("%H"))
    current_min = int(strftime("%M"))
    current_time = (current_hour * 100) + current_min
    sleeping = (NIGHT_OWL and current_time in CHECK_RANGE) or not current_time in CHECK_RANGE
    if not sleeping:
        if current_min in DING_CONFIG.keys():
            ding(current_min)
        if current_min % 10 in MINUTE_INTERVAL_NOTIFY:
             notify(current_min % 10)

def update_time():
    if int(strftime("%S")) == 0:
        compare_time()
    sleep(1)

def main():
    while True:
        update_time()

if __name__ == "__main__":
    main()