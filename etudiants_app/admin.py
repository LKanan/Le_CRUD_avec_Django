from django.contrib import admin
from .models import Student


# ce decorateur est là pour enregistrer notre modèle Student dans la base de données et le rendre visible dans
# l'interface d'administratio de django
@admin.register(Student)
# Cette classe nous permettra de décider des champs qui seront visibles dans l'interface d'administration pour ce
# modèle
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
