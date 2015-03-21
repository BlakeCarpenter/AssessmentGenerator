from django.conf.urls import patterns, url
from assessmentgenerator import views

urlpatterns = patterns('',
        url(r'^dashboard/', views.dashboard, name='dashboard'),
    )
