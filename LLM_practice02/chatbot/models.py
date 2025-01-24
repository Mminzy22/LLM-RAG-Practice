from django.db import models
from django.conf import settings


class ChatMessage(models.Model):
    user_input = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    user_text = models.TextField(null=True, blank=True)
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user_text} | Bot: {self.bot_response}"
