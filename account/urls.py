from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('', views.Home.as_view(), name="Home"),
#    path('accounts/verify/', views.Verify_Code.as_view(), name="Verify"),
    path('login/', views.Login.as_view(),name='Login'),
    path('logout/', views.Logout.as_view(), name="Logout"),
    path('signup/', views.Register.as_view(),name='Signup'),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='account/password_change.html',success_url = 'done/'),name='password_change'),    
    path('password_change/done/',auth_views.PasswordChangeView.as_view(template_name='account/password_change_done.html',success_url = 'password_change_done'),name='password_change_done'),    
    path("password_reset/", views.password_reset_request.as_view(), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),      
    # path('accounts/verification/', include('verify_email.urls')),
]
