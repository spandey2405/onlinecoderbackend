from django.conf.urls import url
from src.api.v1.views.userview import UserView
from src.api.v1.views.tokenview import TokenView

urlpatterns = [
     url(r'^v1/user/$', UserView.as_view()),
     url(r'^v1/login/$', TokenView.as_view()),
     ]

