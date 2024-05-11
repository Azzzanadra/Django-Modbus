from django.urls import path
from . import views

#URL should be music/fans
urlpatterns=[
    path('', views.index, name='index'),
    path('<int:album_id>/', views.detail, name='detail'),
    path('fans',views.fans, name= 'fans'),
]