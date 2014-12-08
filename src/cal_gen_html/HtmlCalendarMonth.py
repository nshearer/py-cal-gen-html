
class HtmlCalendarMonth(object):
    """Calendar representation structured for iterating while generating html
    
    The calendar is going to be represented as a table (if I was smarter with
    CSS, I'd do that instead ;-) ).  To support the concept of multi-day event
    boxes, each week is rendered as a set of "bands" which related to HTML
    table rows.  A single week, then, can be made up of multiple HTML table
    rows.
    
    HtmlCalendarMonth                    
       +                                 
       |                                 
       +->HtmlCalendarWeek               
            +                            
            |                            
            +----->HtmlCalendarBand      
                     +                   
                     |                   
                     +-->HtmlCalendarCell
                                     
    """
    
    def __init__(self, month):
        '''Init
        
        @param month: CalendarMonth to render
        '''
        self.__month = month
        
        
    @property
    def month(self):
        return self.__month
    
    
    @property
    def weeks(self):
        raise NotImplementedError()