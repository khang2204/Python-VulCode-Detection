from django.conf.urls import url
from realpal.apps.chat.views import ChatRoomView
from realpal.apps.chat.api import MessageCreateAPIView
urlpatterns = [url('^$', ChatRoomView.as_view(), name='chat-room'), url(
    '^(?P<room_id>[0-9]+)/', ChatRoomView.as_view(), name='chat-room'), url
    ('^file/$', MessageCreateAPIView.as_view(), name='chat-file')]
