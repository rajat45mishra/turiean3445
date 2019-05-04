from django.shortcuts import render,redirect
from .models import *
from .forms import *

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def addasseth(request):
    if request.method == "POST":
        form = addassetForm(request.POST)
        if form.is_valid():
            blog_item = form.save(commit=False)
            blog_item.save()
            return redirect('/blog/addasseth/')
    else:
        form = addassetForm()
    return render(request, 'blog/AddAsset.html', {'form': form})

def ProjectDetailh(request):
    if request.method == "POST":
        form = addProjectDetailform(request.POST)
        if form.is_valid():
            blog_item = form.save(commit=False)
            blog_item.save()
            return redirect('/blog/addasseth/')
    else:
        form = addProjectDetailform()
    return render(request, 'blog/projectdetail.html', {'form': form})

def AddProjectDocumenth(request):
    if request.method == "POST":
        form = AddProjectDocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blog/AddProjectDocumenth/')
    else:
        form = AddProjectDocumentForm()
    return render(request, 'blog/projectdocument.html', {'form': form})

def AddTechDocumenth(request):
    if request.method == "POST":
        form = AddTechDocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blog/AddTechDocumenth/')
    else:
        form = AddTechDocumentForm()
    return render(request, 'blog/AddTechDocument.html', {'form': form})

def LegalDocuh(request):
    if request.method == "POST":
        form = LegalDocuForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blog/LegalDocuh/')
    else:
        form = LegalDocuForm()
    return render(request, 'blog/LegalDocu.html', {'form': form})

def ReferanceDoch(request):
    if request.method == "POST":
        form = ReferanceDocForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blog/ReferanceDoch/')
    else:
        form = ReferanceDocForm()
    return render(request, 'blog/ReferanceDoc.html', {'form': form})

def InvestmentInfoh(request):
    if request.method == "POST":
        form = InvestmentInfoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blog/InvestmentInfoh/')
    else:
        form = InvestmentInfoForm()
    return render(request, 'blog/InvestmentInfo.html', {'form': form})

def WarrentyDetailh(request):
    if request.method == "POST":
        form = WarrentyDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog/WarrentyDetailh/')
    else:
        form = WarrentyDetailForm()
    return render(request, 'blog/WarrentyDetail.html', {'form': form})

def Installmenth(request):
    if request.method == "POST":
        form = InstallmentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blog/Installmenth/')
    else:
        form = InstallmentForm()
    return render(request, 'blog/Installment.html', {'form': form})

def Investmenth(request):
    if request.method == "POST":
        form = InvestmentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blog/Investmenth/')
    else:
        form = InvestmentForm()
    return render(request, 'blog/Investment.html', {'form': form})

def AssetCorrespondanceh(request):
    if request.method == "POST":
        form = AssetCorrespondanceForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blog/AssetCorrespondanceh/')
    else:
        form = AssetCorrespondanceForm()
    return render(request, 'blog/AssetCorrespondance.html', {'form': form})


def AssetSpecificationh(request):
    if request.method == "POST":
        form = AssetSpecificationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blog/AssetSpecificationh/')
    else:
        form = AssetSpecificationForm()
    return render(request, 'blog/AssetSpecification.html', {'form': form})







