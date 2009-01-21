from django.db import models
from django.utils.translation import get_language, ugettext_lazy as _
from school.education.models import Education
from school.utils.unique_id import slugify

class SchoolCalendarCategory(models.Model):
    """
    Every event in the calenar should have some category
    which is sth good for sorting and ordering events
    """
    english_name = models.CharField(max_length=50,unique=True,help_text=_("English name of the Gallery Category"))
    arabic_name = models.CharField(max_length=50,unique=True,help_text=_("Arabic name of the Gallery Category"))
    english_description = models.TextField(help_text=_("Intro text for the Gallery Category"),blank=True,null=True)
    arabic_description = models.TextField(help_text=_("Arabic Intro text for that section"),blank=True,null=True)
    slug = models.SlugField(_("Slug"), help_text=_("Used for URLs, auto-generated from name if blank"), blank=True)

    def __unicode__(self):
        return "%s-%s"%(self.english_name,self.arabic_name)
    
    def save(self, force_insert=False, force_update=False):
        """
        Some magic
        """
        if not self.slug:
            self.slug = slugify(self.english_name, instance=self)

        super(SchoolCalendarCategory, self).save(force_insert=force_insert, force_update=force_update)


class SchoolCalendarEvent(models.Model):
    """
    The real event occurs here
    """
    category = models.ForeignKey(SchoolCalendarCategory,related_name='events')
    english_title = models.CharField(max_length=50,help_text=_("English name of the Calendar Event"))
    arabic_title = models.CharField(max_length=50,help_text=_("Arabic name of the Calendar Event"))
    english_description = models.TextField(help_text=_("Description for the Calendar Event"))
    arabic_description = models.TextField(help_text=_("Description text for Calendar Event"))
    start_date = models.DateField(_("Date start"))
    
    #optional fields
    end_date = models.DateField(_("Date End"),blank=True,null=True,help_text=_("Some events may continue for a few days like EID so , if the event last more days let it blank"))
    exact_time = models.CharField(max_length=50,help_text=_("Some events need exact starting time,like school opening at 9pm,use hour numbers here"),blank=True,null=True)
    english_place = models.CharField(max_length=50,help_text=_("Some Events need specific place for the event,the english name"),blank=True,null=True)
    arabic_place = models.CharField(max_length=50,help_text=_("Some Events need specific place for the event,the arabic name"),blank=True,null=True)

    def save(self, force_insert=False, force_update=False):
        """
        Some magic
        """
        if not self.end_date:
            self.end_date = self.start_date
        super(SchoolCalendarEvent, self).save(force_insert=force_insert, force_update=force_update)


