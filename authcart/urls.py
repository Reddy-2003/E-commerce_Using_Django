from django.urls import path
from authcart import views

urlpatterns = [
    path('signup/',views.SignUp,name='SignUp'),
    path('login/',views.LogIn,name='LogIn'),
    path('logout/',views.LogOut,name='LogOut'),
    path('activate/<uidb64>/<token>/',views.ActivateAccountView.as_view(),name="activate"),
    path('request-reset-email/',views.RequestResetEmailView.as_view(),name='request-reset-email'),
    path('set-new-password/<uidb64>/<token>',views.SetNewPasswordView.as_view(),name='set-new-password'),
]
