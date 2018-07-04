from django.conf.urls import url
from . import views

urlpatterns = [
    url (r'^$', views.index, name='index'),
    url(r'^video_streamer/(?P<camPK>\d+)',views.video_streamer, name='video_streamer'),
    url (r'^insert/', views.insertCamera, name='insertCamera'),
    url (r'^preview/', views.previewCamera, name='previewCamera'),
]
