from django.urls import path 
from . import views 


urlpatterns = [
    # path('',views.album,name='album'),
    path('',views.AddAlbumCreateView.as_view(),name='album'),
    # path('edit/<int:id>/',views.edit_album,name='edit_album'),
    path('edit/<int:id>/',views.EditAlbumView.as_view(),name='edit_album'),
    # path('delete/<int:id>/',views.delete_album,name='delete_album'),
    path('delete/<int:id>/',views.DeleteAlbum.as_view(),name='delete_album')
]
