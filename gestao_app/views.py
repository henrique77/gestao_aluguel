from django.shortcuts import render, redirect
from gestao_app.forms import EdificioForm, ApartamentoForm
from gestao_app.models import Edificio, Apartamento


# Create your views here.
def addnewAp(request):
    if request.method == "POST":
        form = ApartamentoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = ApartamentoForm()
    return render(request, 'index.html', {'form': form})

def addnewEd(request):
    if request.method == "POST":
        form = EdificioForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = EdificioForm()
    return render(request, 'indexed.html', {'form': form})


def indexAp(request):
    apartamento = Apartamento.objects.all()
    # edificio = Edificio.objects.all()
    # for ed in edificio:
    #     ed.edificio_name = "Morada da lua"
    #     print(ed.edificio_name)
    return render(request, "show.html", {'apartamento': apartamento})

def indexEd(request):
    edificio = Edificio.objects.all()
    return render(request, "edificio.html", {'edificio': edificio})

def alugarAp(request, id):
    apartamento = Apartamento.objects.get(id=id)
    return render(request, 'alugar.html', {'apartamento': apartamento})

def liberarAp(request, id):
    apartamento = Apartamento.objects.get(id=id)
    return render(request, 'liberar.html', {'apartamento': apartamento})

def infoAp(request, id):
    apartamento = Apartamento.objects.get(id=id)
    return render(request, 'info.html', {'apartamento': apartamento})

def updateAp(request, id):
    apartamento = Apartamento.objects.get(id=id)
    form = ApartamentoForm(request.POST, instance=apartamento)
    print(form.is_valid())
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'alugar.html', {'apartamento': apartamento})


def deleteAp(request, id):
    apartamento = Apartamento.objects.get(id=id)
    apartamento.delete()
    return redirect("/")