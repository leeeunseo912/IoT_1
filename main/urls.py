from django.urls import path
# from .views import index, detail, answer_create
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('camping_detail', views.camping_detail, name='camping_detail'),

]
