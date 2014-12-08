'''
@author: nshearer
'''

class CalendarEvent(object):
    '''Represents a single event on the calendar'''

    def __init__(self, start_date, title, time=None, end_date=None, css_class=None):
        '''Init
        
        @param start_date: Date that the event should be placed on
        @param end_date: If creating a multi-day event, specify end of date
        @param title: Text to be placed for the event
        @param time: Time of event (formatted as a string)
        @param css_class: Option css class to place on the event in the HTML
        '''
        self.__start_date = start_date
        self.__end_date = end_date
        self.title = title
        self.time = time
        self.css_class = css_class
        
    
    @property
    def start_date(self):
        return self.__start_date
    
    
    @property
    def end_date(self):
        return self.__end_date
    
    
    def __repr__(self):
        rpr = 'CalendarEvent(start_date=%s' % (self.start_date)
        if self.end_date is not None:
            rpr += ', end_date=%s' % (self.end_date)
        rpr += ', title=%s' % (self.title)
        return rpr + ')'