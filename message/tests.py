from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status

from message.models import Message
from message.serializers import MessageSerializer


client = Client()


class MessageTests(TestCase):

    def setUp(self):
        self.message1 = Message.objects.create(email='asd@asd.com', message_text='asdasdas')
        self.message2 = Message.objects.create(email='as33sd@asd.com', message_text='123123123')

    def test_get_valid_single_message(self):
        response = client.get(
            reverse('single_msg', kwargs={'message_id': self.message1.pk}))
        message = Message.objects.get(pk=self.message1.pk)
        serializer = MessageSerializer(message)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_message(self):
        response = client.get(
            reverse('single_msg', kwargs={'message_id': 50}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_valid__messages(self):
        response = client.get(
            reverse('list_of_msg_with_pagination', kwargs={'page': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid__messages(self):
        response = client.get(
            reverse('list_of_msg_with_pagination', kwargs={'page': 555}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)





