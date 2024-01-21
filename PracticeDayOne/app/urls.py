from django.urls import path 
from . import views


urlpatterns = [
    path('',views.authentication,name='authentication'),
    path('signup/',views.CreateSignupView.as_view(),name='signup'),
    path('login/',views.CreateLoginView.as_view(),name='login'),
    path('logout/',views.CreateLogout.as_view(),name='logout'),
    path('changePassword/',views.password_change,name='pass_change'),
    path('changePassword2/',views.ChangePasswordWithoutOld,name='pass_change2'),
]
