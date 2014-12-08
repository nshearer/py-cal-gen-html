

class HtmlCalendarWeek(object):
    """A single week of the calendar to be rendered"""
    
    def __init__(self):
        pass
        
        
    @property
    def multi_day_bands(self):
        raise NotImplementedError()
    
    
    @property
    def single_day_bands(self):
        raise NotImplementedError()    