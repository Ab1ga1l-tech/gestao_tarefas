from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tarefas/', include('tarefas.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # 🔹 Adicionando login padrão do Django
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]




