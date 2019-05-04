from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class addasset(models.Model):
    Assettype = models.CharField(max_length=50)
    Assetsequence = models.CharField(max_length=50)
    Assetname = models.CharField(max_length=50)
    Assetnumber = models.CharField(max_length=50)
    DateofPurchase = models.DateField()
    AssestWarrentyUpto = models.DateField()


    def __str__(self):
        return self.title

class ProjectDetail(models.Model):
    ProjectNumber = models.CharField(max_length=50)
    ProjectName = models.CharField(max_length=50)
    ProjectContact = models.CharField(max_length=50)
    ProjectAddress = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class AddProjectDocument(models.Model):
    DocumentType = models.CharField(max_length=50)
    DocumentSequence = models.CharField(max_length=50)
    DocumentNumber = models.CharField(max_length=50)
    DocumentName = models.CharField(max_length=50)
    Attachment = models.FileField(upload_to='documents/')
    IssueDate = models.DateField()

    def __str__(self):
        return self.title

class AddTechDocument(models.Model):
    DocumentType = models.CharField(max_length=50)
    DocumentSequence = models.CharField(max_length=50)
    DocumentNumber = models.CharField(max_length=50)
    DocumentName = models.CharField(max_length=50)
    Attachment = models.FileField(upload_to='documents/')
    IssueDate = models.DateField()

    def __str__(self):
        return self.title

class AssetSpecification(models.Model):
    AssetNumber = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    Brand = models.CharField(max_length=50)
    Specifications = models.CharField(max_length=50)



    def __str__(self):
        return self.title

class AssetCorrespondance(models.Model):
    AssetNumber = models.CharField(max_length=50)
    UserGuide = models.CharField(max_length=50)
    WarrentyCard = models.CharField(max_length=50)
    BillNumber = models.CharField(max_length=50)
    PaymentMode = models.CharField(max_length=50)


    def __str__(self):
        return self.title

class Investment(models.Model):
    Date = models.DateField()
    CashRecived = models.CharField(max_length=50)
    Paid = models.CharField(max_length=50)
    Amount = models.IntegerField(max_length=50)


    def __str__(self):
        return self.title

class Installment(models.Model):
    AssetNumber = models.CharField(max_length=50)
    DueDate = models.DateField()
    Payment = models.CharField(max_length=50)
    EnterAmt = models.CharField(max_length=50)
    RemBal = models.CharField(max_length=50)
    PaymentRecpt = models.FileField(upload_to='documents/')


    def __str__(self):
        return self.title


class InvestmentInfo(models.Model):
    DocumentType = models.CharField(max_length=50)
    InvestmentNum = models.CharField(max_length=50)
    DocumentNumber = models.CharField(max_length=50)
    DocumentName = models.CharField(max_length=50)
    DueDate = models.DateField()
    Attachment = models.FileField(upload_to='documents/')


    def __str__(self):
        return self.title


class LegalDocu(models.Model):
    DocumentType = models.CharField(max_length=50)
    DocumentSequence = models.CharField(max_length=50)
    DocumentNumber = models.CharField(max_length=50)
    DocumentName = models.CharField(max_length=50)
    IssueDate = models.DateField()
    Attachment = models.FileField(upload_to='documents/')


    def __str__(self):
        return self.title

class ReferanceDoc(models.Model):
    DocumentType = models.CharField(max_length=50)
    DocumentSequence = models.CharField(max_length=50)
    DocumentNumber = models.CharField(max_length=50)
    DocumentName = models.CharField(max_length=50)
    IssueDate = models.DateField()
    Attachment = models.FileField(upload_to='documents/')


    def __str__(self):
        return self.title


class WarrentyDetail(models.Model):
    AssetNum = models.CharField(max_length=50)
    WarrentyStart = models.DateField()
    ServiceAddrs = models.CharField(max_length=50)
    ServiceCentre = models.CharField(max_length=50)



    def __str__(self):
        return self.title


