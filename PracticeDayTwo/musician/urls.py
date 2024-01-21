from django.urls import path 

from . import views 


urlpatterns = [
    path('',views.musician,name='musician'),
    # path('edit/<int:id>/',views.edit_musician,name='edit_musician'),
    path('edit/<int:id>/',views.UpdateMusician.as_view(),name='edit_musician'),
    path('signup/',views.SignupView.as_view(),name='signup'),
    path('login/',views.CreateLoginView.as_view(),name='login'),
    path('logout/',views.CreateLogOut.as_view(),name='logout'),
   
]
