from collections import deque
import time

timeline = deque(maxlen=50)


def add_event(ip):

    timestamp = time.strftime("%H:%M:%S")

    timeline.appendleft((timestamp, ip))


def get_timeline():

    return list(timeline)