from django.urls import path

from django.contrib.auth.views import (
    PasswordResetDoneView, 
)
from .views import (
    Login,
    Logout,
    Registation,
    ChangePassword,
    ResetPasswordView,
    ResetConfirmPasswordView
)

urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('registation/', Registation.as_view(), name="registation"),
    path('change_password/', ChangePassword.as_view(), name="change_password"),
    
    path('password_reset/', ResetPasswordView.as_view(), name="password_reset"),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', ResetConfirmPasswordView.as_view(), name="password_reset_confirm"),
]

