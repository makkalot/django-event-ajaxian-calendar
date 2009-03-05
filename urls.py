from django.conf.urls.defaults import *

urlpatterns = patterns('',
        (r'^(?P<lang>en|ara?)/calendar/small/(?P<year>\d+)/(?P<month>\d+)/$','schoolcalendar.views.global_school_calendar_ajax',{},'global_calendar_school_ajax'),
        (r'^(?P<lang>en|ara?)/calendar/small/event/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$','schoolcalendar.views.global_pull_calendar_events',{},'global_pull_calendar_events_name'),
        (r'^(?P<lang>en|ara?)/calendar/$','schoolcalendar.views.school_calendar_main',{},'big_calendar_school'),
        (r'^(?P<lang>en|ara?)/calendar/(?P<year>\d+)/(?P<month>\d+)/$','schoolcalendar.views.school_calendar_ajax',{},'big_calendar_school_ajax'),
        (r'^(?P<lang>en|ara?)/calendar/event/(?P<event_id>\d+)/$','schoolcalendar.views.pull_event_detail',{},'big_pull_event_ajax'),
    )

