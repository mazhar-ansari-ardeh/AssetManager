from django.urls import path
from . import views

urlpatterns = [
    path('', views.allAssets, name="assets"),
    path('<int:id>', views.detail, name="detail"),
    path('new', views.new, name="new"),
]
