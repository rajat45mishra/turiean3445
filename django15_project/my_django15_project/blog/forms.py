from django.forms import ModelForm
from .models import *
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class addassetForm(ModelForm):
    class Meta:
        model = addasset
        fields = ['Assettype','Assetsequence','Assetname','Assetnumber','DateofPurchase','AssestWarrentyUpto']

class addProjectDetailform(ModelForm):
    class Meta:
        model = ProjectDetail
        fields = ['ProjectNumber','ProjectName','ProjectContact','ProjectAddress']

class AddProjectDocumentForm(ModelForm):
    class Meta:
        model = AddProjectDocument
        fields = ['DocumentType','DocumentSequence','DocumentNumber','DocumentName','Attachment']

class AddTechDocumentForm(ModelForm):
    class Meta:
        model = AddTechDocument
        fields = ['DocumentType','DocumentSequence','DocumentNumber','DocumentName','Attachment']

class LegalDocuForm(ModelForm):
    class Meta:
        model = LegalDocu
        fields = ['DocumentType','DocumentSequence','DocumentNumber','DocumentName','Attachment']

class ReferanceDocForm(ModelForm):
    class Meta:
        model = ReferanceDoc
        fields = ['DocumentType','DocumentSequence','DocumentNumber','DocumentName','Attachment']

class InvestmentInfoForm(ModelForm):
    class Meta:
        model = InvestmentInfo
        fields = ['DocumentType','InvestmentNum','DocumentNumber','DocumentName','DueDate','Attachment']

class WarrentyDetailForm(ModelForm):
    class Meta:
        model = WarrentyDetail
        fields = ['AssetNum','WarrentyStart','ServiceAddrs','ServiceCentre']

class InstallmentForm(ModelForm):
    class Meta:
        model = Installment
        fields = ['AssetNumber','DueDate','Payment','EnterAmt','RemBal','PaymentRecpt']

class InvestmentForm(ModelForm):
    class Meta:
        model = Investment
        fields = ['Date','CashRecived','Paid','Amount']

class AssetCorrespondanceForm(ModelForm):
    class Meta:
        model = AssetCorrespondance
        fields = ['AssetNumber','UserGuide','WarrentyCard','BillNumber','PaymentMode']

class AssetSpecificationForm(ModelForm):
    class Meta:
        model = AssetSpecification
        fields = ['AssetNumber','Model','Brand','Specifications']



