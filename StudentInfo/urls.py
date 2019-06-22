from django.urls import path

from StudentInfo.views import sendmail
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
# post views
                path('login/', auth_views.LoginView.as_view(), name='login'),
                path('logout/', auth_views.LogoutView.as_view(), name='logout'),
                path('', views.dashboard, name='dashboard'),
                path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
                path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
                path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
                path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
                path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
                path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
                path('sendmail', sendmail, name='sendmail'),
                path('register/', views.register, name='register'),
                path('studentdetails/', views.IndexView.as_view(), name='studentdetails'),
                path('additems/', views.CreateItemsas_view(), name='add_items')
]