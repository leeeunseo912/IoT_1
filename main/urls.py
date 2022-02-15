from django.urls import path
# from .views import index, detail, answer_create
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
  
    path('<int:comment_id>/', views.detail, name = "detail"),
    path('comment/create/', views.comment_create, name='comment_create'),
    # path('comment/modify/<int:comment_id>/', views.comment_modify, name='comment_modify'),
    # path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('campinfo/', views.campinfo, name='campinfo'),
    path('camping_detail', views.camping_detail, name='camping_detail'),   
]
