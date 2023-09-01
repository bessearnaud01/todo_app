from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TacheForm

def index(request):
    form = TacheForm(request.POST or None) # ça veut dire on envoye le formulaire remplit ou vide 
    if form.is_valid():# On teste si notre formulaire est valide
        form.save()
    list = Task.objects.all()
    context ={
        'form': form,
        'taches':list
    }
    return render(request, 'home.html', context )


def update(request,my_id):
    obj = get_object_or_404(Task, id=my_id) # On recupere l'id
   # states, the instance keyword argument is passed the model whose relations that the formset will edit
    form = TacheForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/') # Elle permet de nous rediriger à la
    return render(request, 'update.html', {'form': form })




def delete(request, my_id):
    obj = get_object_or_404(Task, id=my_id)
    obj.delete()
    return redirect('/')                         
     