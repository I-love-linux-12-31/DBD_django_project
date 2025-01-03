"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),

# Логин.
    path('login/', views.LoginView.as_view(), name='login'),
    # Логаут.
    path('logout/', views.LogoutView.as_view(), name='logout'),

    # Изменение пароля.
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    # Сообщение об успешном изменении пароля.
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Восстановление пароля.
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # Сообщение об отправке ссылки для восстановления пароля.
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # Вход по ссылке для восстановления пароля.
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # Сообщение об успешном восстановлении пароля.
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('', include('projectForDBD.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
