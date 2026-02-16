from time import strftime, sleep
from playsound3 import playsound

MUTE_DING = False
MUTE_NOTIFY = False

TO_DING = True
DING_TEXT = "Ding! It's {time}"
DING_CONFIG = {
    0: "sounds/current/hour_00.mp3",
    15: "sounds/current/quarter_15.mp3",
    30: "sounds/current/half_30.mp3",
    45: "sounds/current/quarter_45.mp3"
}

TO_NOTIFY = True
NOTIFICATION_TEXT = " ...  It's {time}"
NOTIFICATION_SOUND = "sounds/current/notification.mp3"
INTERVAL_NOTIFY = lambda current_min: bool(current_min % 5 == 0)

START_TIME = 800
END_TIME = 2200
NIGHT_OWL = START_TIME > END_TIME

def notify(sleeping, min):
    if not MUTE_NOTIFY and not sleeping:
        playsound(NOTIFICATION_SOUND)
    if not min in DING_CONFIG.keys():
        print(NOTIFICATION_TEXT.format(time=strftime("%I:%M%p")))

def ding(sleeping, min):
    if not MUTE_DING and not sleeping:
        playsound(DING_CONFIG[min])
    print(DING_TEXT.format(time=strftime("%I:%M%p")))

def is_sleeping(current_time):
    sleeping = current_time < START_TIME
    if NIGHT_OWL:
        sleeping = sleeping and current_time < END_TIME
    else:
        sleeping = sleeping or current_time > END_TIME
    return sleeping

def compare_time():
    current_hour = int(strftime("%H"))
    current_min = int(strftime("%M"))
    current_time = (current_hour * 100) + current_min
    sleeping = is_sleeping(current_time)
    if TO_DING and current_min in DING_CONFIG.keys():
        ding(sleeping, current_min)
    if TO_NOTIFY and INTERVAL_NOTIFY(current_min):
        notify(sleeping, current_min)

def update_time():
    if int(strftime("%S")) == 0:
        compare_time()
    sleep(1)

def main():
    while True:
        update_time()

if __name__ == "__main__":
    main()