from time import strftime, sleep
from playsound3 import playsound

DING_CONFIG = {
    0: "sounds/current/hour_00.mp3",
    15: "sounds/current/quarter_15.mp3",
    30: "sounds/current/half_30.mp3",
    45: "sounds/current/quarter_45.mp3"
}

START_TIME = 800
END_TIME = 2200
NIGHT_OWL = START_TIME > END_TIME

CHECK_RANGE = range(START_TIME, END_TIME, 5)

def ding(min):
    if min in DING_CONFIG.keys():
            playsound(DING_CONFIG[min])

def compare_time():
    current_hour = int(strftime("%H"))
    current_min = int(strftime("%M"))
    current_time = (current_hour * 100) + current_min
    if ((NIGHT_OWL and not (current_time in CHECK_RANGE)) or current_time in CHECK_RANGE) and (current_min in DING_CONFIG.keys()):
            ding(current_min)
            print(f"Ding @ {strftime("%I:%M%p")}")

def update_time():
    if int(strftime("%S")) == 0:
        if int(strftime("%M")) % 5 == 0:
            print(f"It's {strftime("%I:%M%p")}")
        compare_time()
    sleep(1)

def main():
    while True:
        update_time()

if __name__ == "__main__":
    main()