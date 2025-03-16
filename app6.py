import time

def countdown(t):
    while t:
        mins, secs = divmod(t,60)
        timer =f"{mins:02d}:{secs:02d}"
        print(timer)
        time.sleep(1)
        t -= 1
    print("Timer completed")
t = input("Enter the time in seconds")
6
countdown(int(t))