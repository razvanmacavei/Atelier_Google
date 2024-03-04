from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls'), {'next_page': '/'}, name='login'),
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('locations/', include('aplicatie1.urls')),
    path('companies/', include('aplicatie2.urls')),
    path('profile/', include('user_profile.urls')),
    path('api/', include('myapi.urls')),
]
