import time  
# pip install plyer   
from plyer import notification


if __name__ == '__main__':
    while True:            
        notification.notify(
            title = "Reminder",
            message = "Meeting at 12pm",
            
            timeout = 10 
        )
        time.sleep(60*60)      #intervals after which you want to remind again