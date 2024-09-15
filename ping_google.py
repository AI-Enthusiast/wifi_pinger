# this scrip pings google.com and returns
import datetime
import time
import winsound
import requests


def ping_google(connected=True, lost_pings=0, alert_played=False):
    try:
        requests.get('http://www.google.com', timeout=5)
        if not connected:
            print("Internet connection re-established at\t\t\t", datetime.datetime.now(), '\n')
        connected = True
        time.sleep(20)
        ping_google(connected)
    except requests.ConnectionError:
        if connected:
            print("Lost internet connection, attempting to reconnect at", datetime.datetime.now())
        if lost_pings > 2 and not alert_played:
            freq = 600
            dur = 400
            winsound.Beep(freq, dur)
            winsound.Beep(freq - 100, dur)
            winsound.Beep(freq, dur)
            winsound.Beep(freq - 200, dur)
            dur = 300
            winsound.Beep(freq, dur)
            winsound.Beep(freq - 100, dur)
            winsound.Beep(freq, dur)
            winsound.Beep(freq - 200, dur)
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
