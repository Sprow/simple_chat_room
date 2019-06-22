from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView


from message.models import Message
from message.serializers import MessageSerializer, MessageCreateSerializer


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


class GetListOfMessagesView(APIView):
    """
    return list of 10 messages, require page number
    """
    serializer_class = MessageSerializer
    page_size = 10

    def get_list_of_x_object(self, page, page_size):
        messages_list = Message.objects.all()[int(page)*page_size-page_size:int(page)*page_size]
        if len(messages_list):
            return messages_list
        else:
            raise Http404

    def get(self, request, page):
        message = self.get_list_of_x_object(page, self.page_size)
        serializer = self.serializer_class(message, many=True)
        return Response(serializer.data)


class CreateMessageView(CreateAPIView):
    """
    create new message
    """
    serializer_class = MessageCreateSerializer
