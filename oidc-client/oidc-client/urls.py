from core.oidc_service import create_oidc_session
from core.oidc_service import get_access_token
from core.oidc_service import get_userinfo
from core.oidc_service import index
from core.oidc_service import receive_callback
from django.urls import path

urlpatterns = [
    path('', index),
    path('create-session', create_oidc_session),
    path('callback', receive_callback),
    path('get-access-token', get_access_token),
    path('get-userinfo', get_userinfo),
]
