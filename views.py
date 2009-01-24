from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from school.education.models import Education
from school.schoolcalendar.models import *
from school.ecalendar.utils import *

import datetime
from school.ecalendar.calendar import Calendar

def global_school_callendar(lang=None,year=None,month=None):
    """
    School Based Event CAlendar view
    """
    if not lang:
        lang = "en"

    #
    #calendar_events = SchoolCalendarEvent.objects.all().order_by('-start_date') 
    
    if not year or not month:
        #it seems that is coming from a main page
        now = datetime.datetime.now()
        next_month = get_next_month_year(now.year,now.month)
        prev_month = get_prev_month_year(now.year,now.month)
        cur_month = {'year':now.year,'month':now.month}
    else:
        next_month = get_next_month_year(int(year),int(month))
        prev_month = get_prev_month_year(int(year),int(month))
        cur_month = {'year':int(year),'month':int(month)}

    c = Calendar(6)
    calendar_iterator = c.itermonthdates(cur_month['year'],cur_month['month'])

    return {
            'global_next_month':next_month,
            'global_prev_month':prev_month,
            'global_cur_month':cur_month,
            'global_calendar_iterator':calendar_iterator
            }

def global_school_calendar_ajax(request,lang,year,month):
    """
    The ajaxian calendar 
    """
    result = global_school_callendar(lang,year,month)
    return render_to_response(
            'calendar/calendar_small_%s.html'%lang,
            result,
            context_instance=RequestContext(request)
            )

from django.db.models import Q
def global_pull_calendar_events(request,lang,year,month,day):

    date_to_pull = datetime.datetime(int(year),int(month),int(day))
    calendar_events = SchoolCalendarEvent.objects.filter(
                Q(start_date__lte=date_to_pull) & 
                Q(end_date__gte=date_to_pull)
                )
    
    return render_to_response(
            'calendar/calendar_event_list_%s.html'%lang,
            {
                'calendar_events':calendar_events
                },
            context_instance=RequestContext(request)
            )

   
