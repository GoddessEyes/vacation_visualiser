from django.conf.urls import url
from rest_auth.views import (
    LoginView, LogoutView, PasswordChangeView,
    PasswordResetConfirmView, PasswordResetView,
)


urlpatterns = [
    url(r'^password/reset/$', PasswordResetView.as_view(),
        name='rest_password_reset'),
    url(r'^password/reset/confirm/$', PasswordResetConfirmView.as_view(),
        name='rest_password_reset_confirm'),
    url(r'^login/$', LoginView.as_view(), name='rest_login'),
    url(r'^logout/$', LogoutView.as_view(), name='rest_logout'),
    url(r'^password/change/$', PasswordChangeView.as_view(),
        name='rest_password_change'),
]
