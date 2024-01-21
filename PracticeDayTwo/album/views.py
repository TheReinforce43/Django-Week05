from django.shortcuts import render,redirect
from . import forms 
from . import models 
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views import generic 
from django.contrib.auth import login,logout
from django.views.generic import DeleteView
from django.contrib import messages
# Create your views here.


def album(request):

    album_form=forms.AlbumForm(request.POST)

    if request.method=='POST':

        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    else:
        album_form=forms.AlbumForm()
    return render(request, 'add_album.html',{'form':album_form})

def edit_album(request,id):
    album_id=models.AlbumModel.objects.get(pk=id)
    album_instance=forms.AlbumForm(instance=album_id)

    if request.method=='POST':

        album_instance=forms.AlbumForm(request.POST,instance=album_id)
        if album_instance.is_valid():
            album_instance.save()
            return redirect('home')
    return render(request, 'add_album.html',{'form':album_instance})

def delete_album(request,id):
    album_id=models.AlbumModel.objects.get(pk=id)
    album_id.delete()
    return redirect('home')


# Class Based Views 

class AddAlbumCreateView(CreateView):

    model=models.AlbumModel
    form_class=forms.AlbumForm
    template_name='add_album.html'
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        form.instance.album=self.request.user 
        return super().form_valid(form)
    

class EditAlbumView(UpdateView):
    model=models.AlbumModel
    form_class=forms.AlbumForm
    template_name='add_album.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('home')


class DeleteAlbum(DeleteView):

    model=models.AlbumModel
    template_name='confirm_delete.html'
    success_url=reverse_lazy('home')
    context_object_name='value'
    pk_url_kwarg='id'
    
    
        