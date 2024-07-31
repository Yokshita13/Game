from email import message
import time
import time
from plyer import notification

if __name__== "__main__":
    notification.notify(
        title = "Please Drink water",
        message = "About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
        app_icon = "C:\Users\Prakhyat\Downloads\icon.ico.ico",
        timeout = 5
        #app_icon = "C:\Users\Prakhyat\Desktop\icon.ico",
        #timeout=5
    )
