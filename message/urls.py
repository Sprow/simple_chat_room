from django.conf.urls import url

from message.views import GetAllMessagesView, GetSingleMessageView, CreateMessageView


urlpatterns = [
    url(r'^api/(?P<message_id>[\d]+)$', GetSingleMessageView.as_view()),
    url(r'^messages/page/$', GetAllMessagesView.as_view()),
    url(r'^message/create$', CreateMessageView.as_view()),
]

