from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_view, name='base'),
    url(r'^game_view/$', views.game_view, name='game_view'),
    url(r'^letter_submission/$', views.letter_submission, name='letter_submission'),
]
