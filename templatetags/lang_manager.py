from django import template

register = template.Library()

@register.tag
def generate_lang_name(parser,token):
    """
    Gets a name and gives the language specific one
    {% generate_lang_name field_name model_object lang %}
    """
    try:
        tag_name,field_name,model_object= token.split_contents()

    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires exactly 2 arguments" % token.contents.split()[0]
    if not (field_name[0] == field_name[-1] and field_name[0] in ('"', "'")):
        raise template.TemplateSyntaxError, "%r tag's argument should be in quotes" % tag_name
    
    return GenerateLangNameNode(field_name[1:-1],model_object)

class GenerateLangNameNode(template.Node):
    """
    The actual work is done here
    """
    def __init__(self,field_name,model_object):
        self.field_name = field_name
        self.model_object = template.Variable(model_object)
        #print "The languga eis ",self.lang
      

    def render(self,context):
        
        if context['language'] == "en":
            tmp_lang = "english"
        elif context['language'] == "ara":
            tmp_lang = "arabic"
        else:
            raise template.TemplateSyntaxError, "There is no language like %s " % self.lang
        try:
            return getattr(self.model_object.resolve(context),"".join([tmp_lang,"_",self.field_name]))
        except Exception,e:
            return ''

