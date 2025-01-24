from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.shortcuts import render
from .models import ChatMessage
from .forms import ChatMessageForm
from .utils import get_ai_response


class ChatView(LoginRequiredMixin, FormView):
    template_name = 'chatbot/chat.html'
    form_class = ChatMessageForm

    def form_valid(self, form):
        user_input = self.request.POST.get('user_input')
        prompt = "내가 하는 말이랑 최대한 연관지어서 오늘 하루 힘낼 수 있는 명언해줘"

        ai_response, _ = get_ai_response(user_input, [{"role": "system", "content": prompt}])

        # db 저장
        ChatMessage.objects.create(
            user_input=self.request.user,
            user_text=user_input,
            bot_response=ai_response
        )

        return render(self.request, self.template_name, {
            "form": form,
            "ai_response": ai_response,
            "user_input": user_input,
        })
