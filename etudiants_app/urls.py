from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_and_show_view, name="gestions_informations_etudiants"),
    # <int:id> permet de recuperer l'élement se trouvant juste apres la barre de delete/ et le mettre dans la variable id
    # et cet élément doit etre de type integer, cet élément est l'id ajouté à l'url dans l'action du formulaire du bouton
    # supprimer
    path('delete/<int:id>', views.delete_data, name="suppression_données"),
    path('update/<int:id>', views.update_data, name='modification_données')
]
