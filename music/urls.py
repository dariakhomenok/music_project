from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('genre/', views.genre),
    path('add_genre/', views.add_genre),
    path('edit_genre/<int:id_genre>', views.edit_genre),
    path('delete_genre/<int:id_genre>/', views.delete_genre),
    path('tracks/', views.tracks),
    path('add_track/', views.add_track),
    path('edit_track/<int:id_track>', views.edit_track),
    path('delete_track/<int:id_track>/', views.delete_track),
]

