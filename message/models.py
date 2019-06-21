from django.db import models


class Message(models.Model):
    email = models.EmailField()
    message_text = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(blank=True, default=None, null=True)
