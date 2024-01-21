from django.shortcuts import render,redirect
from  . import forms 
from . import models 
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView,LogoutView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from  django.views import generic
from django.contrib import messages 
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def musician(request):
    musician_form=forms.MusicianForm(request.POST)

    if request.method=='POST':
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home')
    
    else:
        musician_form=forms.MusicianForm()

    return render(request, 'add_musicain.html',{'form':musician_form})


def edit_musician(request,id):

    musician_id=models.MusicianModel.objects.get(pk=id)
    musician_instance=forms.MusicianForm(instance=musician_id)

    if request.method=='POST':
        musician_instance=forms.MusicianForm(request.POST,instance=musician_id)
        if musician_instance.is_valid():
            musician_instance.save()
            return redirect('home')

    return render(request,'add_musicain.html',{'form':musician_instance})

# Create Registration form using class based views

class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url=reverse_lazy('login')
    template_name='LoginSignUp.html'


#Create login using  Classs Based View
class CreateLoginView(LoginView):
    template_name='LoginSignUp.html'

    def form_valid(self,form):
         messages.success(self.request,'Login Successfully')
         return super().form_valid(form)
    def form_invalid(self,form):
        messages.error(self.request,'login Not succcessfully')
        return super().form_invalid(form)
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Log In'
        return context 
    def get_success_url(self):
        return reverse_lazy('home')
    

# Update musician data using Class Based View 
    
class UpdateMusician(UpdateView):
    model=models.MusicianModel
    form_class=forms.MusicianForm

    template_name='add_musicain.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('home')


@method_decorator(login_required,name='dispatch')
class CreateLogOut(generic.View):

    def get(self,request):
        logout(request)
        return redirect('home')
    

