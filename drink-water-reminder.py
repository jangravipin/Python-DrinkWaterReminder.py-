import time
from plyer import notification

while True:
    print("Please have a glass of water!")
    notification.notify(
        title="Please drink some water",
        message="You need to drink some water"
    )
    time.sleep(60*60)