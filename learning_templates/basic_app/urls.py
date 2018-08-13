from django.conf.urls import url
from basic_app import views

#Template Tagging
app_name = 'basic_app'

urlpatterns = [
    url(r'relative_url_templates/$', views.relative_url_templates, name='relative_url_templates'),
    url(r'others/$', views.others, name='others')
]
