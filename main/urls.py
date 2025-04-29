from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('help/', views.help_page, name='help'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('api/accidents/', views.accident_list_api, name='accident_list_api'),
    path('add_accident/', views.add_accident, name='add_accident'),
    path('accident/delete/<int:accident_id>/', views.delete_accident, name='delete_accident'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('help/', views.help_page, name='help'),
]
