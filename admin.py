from school.schoolcalendar.models import *
from django.contrib import admin

class SchoolCalendarCategoryAdmin(admin.ModelAdmin):
    exclude = ('slug')
    list_display = ('english_name','arabic_name')
    list_display_links = ('english_name',)
    ordering = ['english_name',]

class SchoolCalendarEventAdmin(admin.ModelAdmin):
    list_display = ('english_title','arabic_title', 'category','start_date')
    ordering = ['category','-start_date']
    list_filter = ('start_date','category',)
    search_fields = ['english_title','arabic_title']


admin.site.register(SchoolCalendarCategory,SchoolCalendarCategoryAdmin)
admin.site.register(SchoolCalendarEvent, SchoolCalendarEventAdmin)
