import time
def count_down(user_time):
    while user_time>=0:
        mins,sec=divmod(user_time,60)
        timer='{:02d}:{:02d}'.format(mins,sec)
        print(timer,end='\r')
        time.sleep(1)
        user_time-=1
    print("Lift off!")
if __name__ == '__main__':
  user_time = int(input("Enter a time in seconds: "))
  count_down(user_time)