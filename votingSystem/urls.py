from django.contrib import admin
from django.urls import path
from votingSystem import views

admin.site.site_header = "UOH Admin"
admin.site.site_title = "UOH Admin Portal"
admin.site.index_title = "Welcome to UOH Online Voting System"


urlpatterns = [
    path('', views.index, name="home"),
    path('register', views.register, name="register"),
    path('vote', views.vote, name='vote'),
    path('info', views.info, name='about')
]
