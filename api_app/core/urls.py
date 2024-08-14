from django.urls import path
from .views import send_text, webhook


urlpatterns = [
    path("send-text/", send_text, name="send_text"),
    path("webhook/", webhook, name="webhook"),
]
