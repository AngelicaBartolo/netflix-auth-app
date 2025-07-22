# backend/urls.py
#from django.contrib import admin
#from django.urls import path, include
#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('api/', include('users.urls')),
#]
# backend/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import RegisterView
from .views import LoginView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
#    path('api/', include('users.urls')),
]