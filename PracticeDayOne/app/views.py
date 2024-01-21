from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,UserCreationForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages




# Create your views here.

def authentication(request):
    return render(request,'authentication.html')


class CreateSignupView(generic.CreateView):

    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='common_form.html'
    
    def form_valid(self,form):
        response=super().form_valid(form)
        messages.success(self.request, 'User created successfully')
        return response


class CreateLoginView(LoginView):
    template_name='common_form.html'

    def form_valid(self,form):
        messages.success(self.request,'Login successful')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,'Login failed')
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('home')
    
@method_decorator(login_required,name='dispatch')

class CreateLogout(generic.View):
    def get(self,request):
        logout(request)
        messages.warning(request,'Logout Successfully')
        return redirect('home')
    
def password_change(request):
    form=PasswordChangeForm(user=request.user)
    if request.method=='POST':
        form=PasswordChangeForm(user=request.user,data=request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('home')
   
    return render(request, 'common_form.html', {'form':form,'type':'Change Password with Previous Password'})

def ChangePasswordWithoutOld(request):
    form=SetPasswordForm(user=request.user)

    if request.method=='POST':
        form=SetPasswordForm(user=request.user,data=request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('home')

    return render(request, 'common_form.html',{'form':form,'type':'Change Password without Previous Password'})            



