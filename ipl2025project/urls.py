
from django.contrib import admin
from django.urls import path
from iplapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
    path('create/', create_view),
    path('register/', signup_view, name="signup"),
    path('login/', login_view, name="loginup"),
    path('display/', display_view),
    path('update/<int:n>/', update_view),
    path('delete/<int:n>/', delete_view),
]
