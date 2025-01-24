from django import forms
from .models import ChatMessage


class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = []
        widgets = {
            'bot_response': forms.TextInput(attrs={
                'placeholder': '대화를 입력하세요...',
            }),
        }
