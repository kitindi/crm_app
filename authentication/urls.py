from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.login, name='login'),
    path("signup/", views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    # path('profile/',views.profile, name='profile'),
]
