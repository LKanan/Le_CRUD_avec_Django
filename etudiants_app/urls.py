from django.urls import path
from . import views

urlpatterns = [
    path('addnshow/', views.add_and_show_view, name="gestions_informations_etudiants"),
]
