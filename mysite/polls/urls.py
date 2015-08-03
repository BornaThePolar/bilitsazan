from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^register/$', views.register, name='register'),
    url(r'^eventsubmit/$', views.eventSubmit, name='eventSubmit'),
    url(r'^buy/$', views.buy, name='buy'),
    url(r'^about/$', views.about, name='about'),
    url(r'^login/$', views.login, name='login'),
    url(r'^main/$', views.main, name='main'),
    url(r'^home/$', views.home, name='home'),
    url(r'^event/$', views.event, name='event'),
    url(r'^report/$', views.report, name='report'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^eventreport/$', views.event_report, name='contact'),
    url(r'^manage/$', views.manage, name='manage'),
    url(r'^addSubCategory/(?P<subcategory_name>\w+)/(?P<subcategory_id>\d+)/$', views.AddSubCategory, name='AddSubCategory'),
    url(r'^addCategory/(?P<category_name>\w+)/$', views.AddCategory, name='AddCategory')




]