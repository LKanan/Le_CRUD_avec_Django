# Dans ce fichier on va défiir nos champs qui seront utilisés dans le formulaire sur notre page web
# Django.core est une bibliotèque qui permet de créer des validators, ce sont de boutons qui permettrons de valider
from django.core import validators
# forms est une biliotheque qui permet la créarion des formualires
from django import forms
from .models import Student


# Cette classe nous permet d'organiser nos champs qui seron utilisés dans notre formulaire
class StudentRegistration(forms.ModelForm):
    # Meta est un mot clé nom de la classe dans la création du formulaire
    class Meta:
        # model est un mot clé et variable spéciale qui recupere le modele dont il s'agit pour ce formulaire, c'est ce modele qui recoit
        # les données du formulaire
        model = Student
        # fields est aussi un mot clé et variable spéciale qui recupères tous les noms de champs de notre model
        fields = ['name', 'email', 'password']
        # widget est aussi un mot clé et variable spéciale qui permet de stylisé nos champs d'entrée de informations de
        # notre formulaire, il nous permet de donner des attributs comme si on les donnés dans untag html d'un champ
        # donc dans widgets on stylise les champs qui sont generer automatisuement dans le fichier html
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
