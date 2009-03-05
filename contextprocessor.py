from schoolcalendar.views import global_school_callendar

def get_language(request):
    
    url_path = request.path

    language = "en"
    if url_path.startswith("/ara/"):
        language = "ara"

    #print "The language is : ",language

    return {
            'language':language
            }

def pass_language(request):
    """
    Returns back the language according to url ..
    """
    return get_language(request)


def global_calendar_ctx(request):
    """
    Here will have the global calendar variables ...
    """
    language =pass_language(request)['language']
    return global_school_callendar(language)
