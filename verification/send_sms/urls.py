from django.urls import path
from . import views


urlpatterns = [
    path("send_sms/", views.send_sms_view, name="send-sms"),
    path(
        "success-page/<str:phone_number>/", views.success_page_view, name="success-page"
    ),
]
