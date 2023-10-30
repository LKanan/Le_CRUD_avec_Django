from django.shortcuts import render
from .forms import StudentRegistration
from .models import Student


def add_and_show_view(request):
    if request.method == 'POST':
        # Ici on recupère les informations dans les différents champs du formulaire
        form = StudentRegistration(request.POST)
        # On test la validité du formulaire par rapport aux types de champs prédéfini
        if form.is_valid():
            nm = form.cleaned_data['name']#effacage du champ du nom
            em = form.cleaned_data['email']#effacage du champ de l'email
            pw = form.cleaned_data['password']#effacage du champ du password
            reg = Student(name=nm, email=em, password=pw)
            reg.save()
            form = StudentRegistration()
    else:
        form = StudentRegistration()
        stud = Student.objects.all()
    return render(request, 'etudiants_app/add_and_show_student.html', {'form': form, 'stu': stud})
