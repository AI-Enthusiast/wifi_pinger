import datetime
import time
import requests
from playsound import playsound

def ping_google(connected=True, lost_pings=0, alert_played=False):
    try:
        requests.get('http://www.google.com', timeout=5)
        if not connected:
            print("Internet connection re-established at\t\t\t", datetime.datetime.now(), '\n')
            playsound('alert_sound.mp3')
        connected = True
        time.sleep(20)
        ping_google(connected)
    except requests.ConnectionError:
        if connected:
            print("Lost internet connection, attempting to reconnect at", datetime.datetime.now())
        if lost_pings > 1 and not alert_played:
            playsound('alert_sound.mp3')
            alert_played = True
        connected = False
        time.sleep(10)
        ping_google(connected, lost_pings + 1, alert_played)

if __name__ == '__main__':
    while True:
        try:
            ping_google()
        except RecursionError:
            pass