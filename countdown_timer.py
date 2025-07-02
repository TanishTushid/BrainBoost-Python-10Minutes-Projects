#*****************Countdown Timer*****************
import time

def count_down_timer():
    seconds = int(input("Enter timer in second: "))
    print("countdown start")

    while seconds > 0:
        mins,sec = divmod(seconds,60)
        time_format = f"{mins:02d} : {sec:02d}"
        print(time_format, end = "\r")
        time.sleep(1)
        seconds -=1
    print("times up")

if __name__=="__main__":
    count_down_timer()
