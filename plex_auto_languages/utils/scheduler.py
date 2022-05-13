import time
from typing import Callable
from threading import Thread, Event
import schedule


class Scheduler(Thread):

    def __init__(self, time_of_day: str, callback: Callable):
        super().__init__()
        schedule.every().day.at(time_of_day).do(callback)
        self._stop_event = Event()

    def run(self):
        while not self._stop_event.is_set():
            schedule.run_pending()
            time.sleep(5)

    def shutdown(self):
        self._stop_event.set()
