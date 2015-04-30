from django.conf.urls import patterns, url
from assessmentgenerator import views

urlpatterns = patterns('',
        url(r'^$', views.generator_home, name='generator_home'),
        url(r'^dashboard/$', views.dashboard, name='dashboard'),
        url(r'^generator/$', views.generator_main, name='generator'),
        url(r'^add_question/$', views.add_question, name='add_question'),
        url(r'^gen_test/$', views.generate_test, name='generate_test'),
    )
