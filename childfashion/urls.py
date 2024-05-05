from django.urls import path
from django.contrib.auth import views as auth_views  # import auth_views from django.contrib.auth
from . import views   # call to url_shortener/views.py
# from django.views.generic import TemplateView

urlpatterns = [
    path('Home', views.index, name='index'),
    # path('dstheloai', views.list, name='dstheloai'),
    # path('themloai', views.themloai, name='themloai'),
    # path('BangSP', views.list2, name='bangsp'),
    # path('ThemSP', views.ThemSP, name='themsp'),
]
