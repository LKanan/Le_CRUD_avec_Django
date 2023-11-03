# HttpResponseRedirect permet de rediriger à un url défini lorsqu'on appel une vue
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student


# Cette fonction permet d'ajouter et afficher les informations d'un étudiant
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
        # return render(request, 'etudiants_app/add_and_show_student.html', {'form': form, 'stu': stud})
    # return render(request, 'etudiants_app/add_and_show_student.html', {'form': form})
    return render(request, 'etudiants_app/add_and_show_student.html', {'form': form, 'stu': stud})


#Cette fonction permet de supprimer les données d'un étudiant
# cet id est celui ajouté à l'url de cette vue et qui sera recuperé pour permettre la manipulation des enregistrements
def delete_data(request, id):
    if request.method == 'POST':
        # on peut acceder à chaque enregistrement de la base de données moyenant son id qui est une clé primaire du
        # modèl auquel il appartient
        # pk = est une variable indispensabe qui signifie primary key et qui prend comme valeur l'id de l'eregistrement
        # et sans oublier que c'est un nom de variable spécial et dit donc etre écrit de cette facon quand on l'utilise
        enregistrement = Student.objects.get(pk=id)
        # delete est methode qu'herite la classe student qui permet d'effacer un enregistrement
        enregistrement.delete()
        return HttpResponseRedirect('/')


# cette fonction permet de modifier les informations d'un étudiant
def update_data(request, id):
    if request.method == 'POST':
        # On recupere les informations de l'etudiant dans l'objet enregistrement
        enregistrement = Student.objects.get(pk=id)
        # Ici le parametre request.POST est utilisé pour passer les données soumises par l'utilisateur au formulaire, mais
        # instance=enregistrement est utilisé pour préremplir les champs d'un formulaire avec des informations préexistantes
        form = StudentRegistration(request.POST, instance=enregistrement)
        if form.is_valid():
            form.save()
    else:
        enregistrement = Student.objects.get(pk=id)
        form = StudentRegistration(instance=enregistrement)
    return render(request, 'etudiants_app/update_student.html', {'form': form})
