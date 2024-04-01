from django.urls import path
from unicodedata import name
from . import views
from django.contrib.auth import views as auth_views

# accounts/profile/

urlpatterns = [
    path('', views.index, name='index'),
    # path('accounts/profile/', views.index, name='index'),
    path('accounts/profile/register', views.register, name='register'),
    path('accounts/profile/reset_password', views.reset_password, name='reset_password'),
    path('accounts/profile/set_password', views.set_password, name='set_password'),
    path('accounts/profile/logout', views.logout, name='logout'),
    path('accounts/profile/how', views.how, name='how'),
    path('accounts/profile/about', views.about, name='about'),
    path('accounts/profile/wallet', views.wallet, name='wallet'),
    path('accounts/profile/view_profile', views.view_profile, name='view_profile'),
    path('accounts/profile/invest', views.invest, name='invest'),

    path('accounts/profile/dashboard', views.dashboard, name='dashboard'),
    path('accounts/profile/login/', auth_views.LoginView.as_view(), name='login'),
    # path('accounts/profile/logout', auth_views.LogoutView.as_view(), name='logout'),

    # password change
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/ done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]