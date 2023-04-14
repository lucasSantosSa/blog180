from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views

class CustomLogoutView(auth_views.LogoutView):
    next_page = '/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
]
