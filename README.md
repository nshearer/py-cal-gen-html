py-cal-gen-html
===============

Python HTML Calendar Generator

Summary
-------

This project is to create a K.I.S.S. Python module for generating a HTML calendar month showing both single day and multi day events.


Output Example
--------------

*TODO*


Example
-------

The included example application is provided to generate a calendar from a YAML file.

Usage:

	gen_cal.py input_file.yml output_file.html

The YAML structure is:

	---
	Year:	2014
	Month:	12
	Events:

      - StartDate:	2014-12-22
        EndDate:	2014-12-26
        Title:		Christmas Vacation
        
	  - Date:		2014-12-24
	    Time:		12:00pm
        Title:		Christmas Eve Lunch

	  - Date:		2014-12-25
	    Title:		Christmas Day


Object Model
------------

To use the Python modules directly, use the classes:

  -  **CalendarMonth**: To represent the output to be generated
  -  **CalendarEvent**: To hold properties for a single event to be placed on the calendar

Basic Usage is:

	---
	from datetime import date
	from cal_gen_html.CalendarMonth import CalendarMonth
	from cal_gen_html.CalendarEvent import CalendarEvent

	if __name__ == '__main__':
		dec = CalendarMonth(2014, 12)
		dec.add(CalendarEvent(
			start_date: date(2014, 12, 22),
			end_date:   date(2014, 12, 26),
			title:		"Christmas Vacation"))
		dec.add(CalendarEvent(
			start_date: date(2014, 12, 24),
			event_time:	'12p',
			title:		"Christmas Eve Lunch"))
		dec.add(CalendarEvent(
			start_date: date(2014, 12, 25),
			title:		"Christmas Eve Lunch",
			css_clasS:	'my_class'))
		
		with open('December.html', 'wt') as fh:
			fh.write(dec.render())
