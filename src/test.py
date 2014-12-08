from datetime import date
from cal_gen_html.CalendarMonth import CalendarMonth
from cal_gen_html.CalendarEvent import CalendarEvent

if __name__ == '__main__':
    dec = CalendarMonth(2014, 12)
    dec.add(CalendarEvent(
        start_date= date(2014, 12, 22),
        end_date=   date(2014, 12, 26),
        title=        "Christmas Vacation"))
    dec.add(CalendarEvent(
        start_date= date(2014, 12, 24),
        event_time=    '12p',
        title=        "Christmas Eve Lunch"))
    dec.add(CalendarEvent(
        start_date= date(2014, 12, 25),
        title=        "Christmas Eve Lunch",
        css_class=    'my_class'))
    
    with open('December.html', 'wt') as fh:
        fh.write(dec.render())