

class HtmlCalendarBand(object):
    """A single HTML Table row of the calendar to be rendered"""
    
    def __init__(self):
        pass
        
        
    @property
    def cells(self):
        raise NotImplementedError()