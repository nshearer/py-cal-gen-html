

class HtmlCalendarWeek(object):
    """A single week of the calendar to be rendered"""
    
    def __init__(self):
        pass
        
        
    @property
    def bands(self):
        raise NotImplementedError()