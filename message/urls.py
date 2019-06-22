from django.conf.urls import url

from message.views import GetListOfMessagesView, GetSingleMessageView, CreateMessageView


urlpatterns = [
    url(r'^(?P<message_id>[\d]+)$', GetSingleMessageView.as_view(), name='single_msg'),
    url(r'^messages/(?P<page>[\d]+)$', GetListOfMessagesView.as_view(), name='list_of_msg_with_pagination'),
    # url(r'^messages/$', GetAllMessagesView.as_view(), name='list_of_msg_with_pagination'),
    url(r'^message/create$', CreateMessageView.as_view(), name='create_msg'),
]

