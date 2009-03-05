from django import template
from schoolcalendar.models import SchoolCalendarEvent
from django.db.models import Q
from django.utils.safestring import mark_safe


register = template.Library()

@register.filter
def is_event(value):

    #print "The value : ",value
    c = SchoolCalendarEvent.objects.filter(
                Q(start_date__lte=value) & 
                Q(end_date__gte=value)
                )
    if c :
        return mark_safe('<td class="datebox_event">')
    else:
        return mark_safe('<td class="datebox_white">')

