# Path: chat/views.py

from django.shortcuts import render

def chat(request):
    return render(request, "chat/chat_form.html", {})

