from django import template
from schoolcalendar.models import SchoolCalendarEvent
from django.db.models import Q
from django.utils.safestring import mark_safe


register = template.Library()

@register.filter
def is_global_event(value):
    
    calendar_events = SchoolCalendarEvent.objects.filter(
                Q(start_date__lte=value) & 
                Q(end_date__gte=value)
                )
    if calendar_events:
        #do spme
        return True
    else:
        #do another
        return False

