'''
@author: nshearer
'''
from datetime import date
import calendar

class CalendarMonth(object):
    '''A single month of events renderable to HTML'''

    WEEKDAYS=[
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday']


    def __init__(self, year, month):
        self.__year = year
        self.__month = month
        self.__events = list()
        self.__events_by_day = dict()
        
        for day_num in range(self.end_of_month.day):
            self.__events_by_day[date(year, month, day_num+1)] = list()
        
        
    @property
    def year(self):
        return self.__year
    
    @property
    def month(self):
        return self.__month
    
    @property
    def events(self):
        for event in self.__events:
            yield event
    
    
    @property
    def start_of_month(self):
        return date(self.__year, self.__month, 1)
        
    @property
    def end_of_month(self):
        month_range = calendar.monthrange(self.__year, self.__month)
        return date(self.__year, self.__month, month_range[1])
    
    
    @property
    def days_in_month(self):
        return self.__events_by_day.keys()
    
        
    def add(self, event):
        # Check Dates
        in_month = True
        if event.start_date < self.start_of_month:
            in_month = False
        if event.start_date > self.end_of_month:
            in_month = False
        if event.end_date is not None:
            if event.end_date < self.start_of_month:
                in_month = False
            if event.end_date > self.end_of_month:
                in_month = False
        if not in_month:
            msg = "%s not in month %s -> %s"
            msg = msg % (event, self.start_of_month, self.end_of_month)
            raise Exception(msg)
        
        
        self.__events.append(event)
        
        for day in event.days_of_event:
            self.__events_by_day[day].append(event)
            
            
    def _generate_cal_struct(self):
        '''Create a representation of the calendar tailored for creating HTML'''
        
        
    