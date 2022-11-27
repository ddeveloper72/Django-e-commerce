from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_change_done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset_done',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete')
]
