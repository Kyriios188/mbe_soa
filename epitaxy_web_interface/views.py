from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import ExperimentForm

# Create your views here.

def index(request: HttpRequest):
    return render(request, 'epitaxy_web_interface/index.html', {})


def upload_files(request: HttpRequest):

    context = {
        'form': ExperimentForm(
            request.POST or None,
            request.FILES or None
        )
    }

    if request.method == "POST":

        print(context['form'].errors)

        if context['form'].is_valid():
            created_object = context['form'].save()

            messages.success(request, "Changements sauvegardés")
            return redirect('/')

    return render(request, 'epitaxy_web_interface/form.html', context)


def predict(request: HttpRequest):
    return HttpResponse("Prédiction du résultat final")
