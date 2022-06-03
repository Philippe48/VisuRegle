from django.shortcuts import render,redirect
from django.db.models import Q
from .forms import RegleForm

# Create your views here.
from .models import Regle, Abonne, RegleAbonne

def listeRegle(request):
    regles=Regle.objects.all()
    context = {'regles': regles}
    return render(request, 'listeregle.html', context)

def listeAbonne(request):
    abonnes=Abonne.objects.filter(Q(codeabonne="6320"))
    abonnes=Abonne.objects.all()
    context = {'abonnes': abonnes}
    return render(request, 'listeabonne.html', context)

def valeurParam(RegleAbo, indParam):
    if indParam == 1:
        return RegleAbo.valparam1
    if indParam == 2:
        return RegleAbo.valparam2
    if indParam == 3:
        return RegleAbo.valparam3
    if indParam == 4:
        return RegleAbo.valparam4
    if indParam == 5:
        return RegleAbo.valparam5
    if indParam == 6:
        return RegleAbo.valparam6
    if indParam == 7:
        return RegleAbo.valparam7
    if indParam == 8:
        return RegleAbo.valparam8
    if indParam == 9:
        return RegleAbo.valparam9
    if indParam == 10:
        return RegleAbo.valparam10

def NomRegle(RegleAbo):
    regle = Regle.objects.get(pk=RegleAbo.idregle)
    chaine = regle.nom
    indParam = 0
    deb = chaine.find('{')
    while deb != -1:
        fin = chaine.find('}')
        indParam += 1
        val = valeurParam(RegleAbo, indParam)
        chaine = chaine.replace(chaine[deb:fin+1],val)
        deb = chaine.find('{')
    return chaine

def listeRegleAbonne(request,pk):
    regleabonnes=RegleAbonne.objects.filter(idabonne=pk).order_by('ordre')
    query = []
    for regleabo in regleabonnes:
        ch = NomRegle(regleabo)
        query.append({'id':regleabo.id, 'nom': ch})
    context = {'regleabonnes': query }
    return render(request, 'listeregleabonne.html', context)
