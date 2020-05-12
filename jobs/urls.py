from django.urls import path
from . import views

urlpatterns = [
    path('<int:jid>/',views.detail, name='jobdetail')
]