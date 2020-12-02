from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/NewPlayer/$', consumers.NewPlayer),
    re_path(r'ws/PreparingNews/(?P<game_name>\w+)/$', consumers.PrepareHerald)
    
]