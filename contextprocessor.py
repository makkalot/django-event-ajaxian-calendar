from school.education.contextprocessor import pass_language
from school.schoolcalendar.views import global_school_callendar

def global_calendar_ctx(request):
    """
    Here will have the global calendar variables ...
    """
    language =pass_language(request)['language']
    return global_school_callendar(language)
