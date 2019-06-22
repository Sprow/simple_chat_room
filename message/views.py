from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination

from message.models import Message
from message.serializers import MessageSerializer


class GetSingleMessageView(APIView):
    """
    return message by pk
    """
    serializer_class = MessageSerializer

    def get_object(self, obj_id):
        try:
            return Message.objects.get(pk=obj_id)
        except Message.DoesNotExist:
            raise Http404

    def get(self, request, message_id):
        message = self.get_object(message_id)
        return Response(self.serializer_class(message).data)


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 500


class GetAllMessagesView(ListAPIView):
    """
    return list of messages (10 per page by default or x per page where x is page_size)
    """
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    pagination_class = Pagination


class CreateMessageView(CreateAPIView):
    """
    create new message
    """
    serializer_class = MessageSerializer
