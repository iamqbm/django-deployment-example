from django import template

register = template.Library()

@register.filter(name="cut")
#value or variable passed from the basic_app/views.User context_dict
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.replace(arg, '')

# first 'cut' is what we call the function and use it in it template tag
# register.filter("cut", cut)
