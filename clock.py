from time import strftime, sleep
from playsound3 import playsound

TO_DING = True
DING_TEXT = "Ding @ {time}"
DING_CONFIG = {
    0: "sounds/current/hour_00.mp3",
    15: "sounds/current/quarter_15.mp3",
    30: "sounds/current/half_30.mp3",
    45: "sounds/current/quarter_45.mp3"
}

TO_NOTIFY = True
NOTIFICATION_TEXT = "Hey! It's {time}"
MINUTE_INTERVAL_NOTIFY = {
    3: "sounds/current/notification.mp3"
}

START_TIME = 800
END_TIME = 2200
NIGHT_OWL = START_TIME > END_TIME

def notify(interval):
    if interval in MINUTE_INTERVAL_NOTIFY.keys():
        playsound(MINUTE_INTERVAL_NOTIFY[interval])
        print(NOTIFICATION_TEXT.format(time=strftime("%I:%M%p")))
    pass

def ding(min):
    if min in DING_CONFIG.keys():
            playsound(DING_CONFIG[min])
            print(DING_TEXT.format(time=strftime("%I:%M%p")))

def is_sleeping(current_time):
    sleeping = current_time < START_TIME
    if NIGHT_OWL:
        sleeping = sleeping or current_time < END_TIME
    else:
        sleeping = sleeping or current_time > END_TIME

def compare_time():
    current_hour = int(strftime("%H"))
    current_min = int(strftime("%M"))
    current_time = (current_hour * 100) + current_min
    if not is_sleeping(current_time):
        if TO_DING and current_min in DING_CONFIG.keys():
            ding(current_min)
        if TO_NOTIFY and current_min % 10 in MINUTE_INTERVAL_NOTIFY:
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