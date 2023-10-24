from typing import Any
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout
from django.views import generic
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetConfirmView
)

from .forms import (
    LoginForms, 
    RegistationForms, 
    ChangePasswordForm, 
    SendEmailForm,
    CustomSetPasswordForm
)
from .mixins import LogoutRequiredMixin


@method_decorator(never_cache, name="dispatch")
class Login(LogoutRequiredMixin ,generic.View):
    def get(self, *args, **kwargs):
        form = LoginForms()
        context = { 'form' : form }
        return render(self.request, "account/login.html", context)

    def post(self, *args, **kwargs):
        form = LoginForms(self.request.POST)

        if form.is_valid():
            user = authenticate(
                self.request,
                username = form.cleaned_data.get('username'),
                password = form.cleaned_data.get('password')
            )
            if user:
                login(self.request, user)
                return redirect('home')
            
            else:
                messages.warning(self.request, 'Worng credentials')
                return redirect('login')

        return render(self.request, "account/login.html", {'form':form})

class Logout(generic.View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('login')
    

@method_decorator(never_cache, name="dispatch")
class Registation(LogoutRequiredMixin, generic.CreateView):
    template_name = 'account/registation.html'
    success_url = reverse_lazy('login')
    form_class = RegistationForms

    def form_valid(self, form):
        messages.success(self.request, 'Registation Successfull!')
        return super().form_valid(form)
    
@method_decorator(never_cache, name="dispatch")
class ChangePassword(LoginRequiredMixin, generic.FormView):
    template_name = 'account/change_password.html'
    form_class = ChangePasswordForm
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('login')
    
    def get_form_kwargs(self):
        context = super().get_form_kwargs()
        context["user"] = self.request.user
        return context

    def form_valid(self, form):
        new_password = form.cleaned_data.get("new_password1")
        user = self.request.user
        user.set_password(new_password)
        user.save()
        messages.success(self.request, 'Password Change Successfully!')
        return super().form_valid(form)
    

class ResetPasswordView(PasswordResetView):
    template_name = 'account/reset_password.html'
    form_class = SendEmailForm

class ResetConfirmPasswordView(PasswordResetConfirmView):
    template_name = "account/password_reset_confirm.html"
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "Your Password Reset Succeesfully!")
        return super().form_valid(form)
    

