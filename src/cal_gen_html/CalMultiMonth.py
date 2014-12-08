
from CalendarMonth import CalendarMonth

class CalMultiMonth(object):
    '''Organizes events into multiple months
    
    Usage:
        1) Call .add(event) to add CalendarEvent objects
        2) Call .get_months() to generate individual CalendarMonth objects
    '''


    def __init__(self):
        self.__events = list()
        
        
    def __repr__(self):
        return 'CalMultiMonth()' 
        
        
    def add(self, event):
        '''Add an event to the collection'''
        self.__events.add(event)
        
        
    def get_months(self):
        '''Generate month objects for generating output'''
        months = dict()
        for orig_event in self.__events:
            # Slice event date ranges into months
            for start_date, end_date in orig_event.get_event_dates_by_months():
                
                # Create new event just within a month
                event = orig_event.clone(start_date, end_date)

                # Get month
                month_key = event.year, event.month
                if not months.has_key(month_key):
                    months[month_key] = CalendarMonth(event.year, event.month)
                month = months[month_key]
                
                # Add this event to the month
                month.add(event)
                    
        return months.items()
    
    