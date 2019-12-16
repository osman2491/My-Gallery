from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^photos/$',views.display_photos,name='photos')
]