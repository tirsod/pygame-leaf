import time

class TimeManager():
    def update(self):
        """future"""
    def get_time_12hour(self):
        return time.strftime("%I:%M:%S %p", time.localtime())