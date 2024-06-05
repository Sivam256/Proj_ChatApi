from django.db import models

class Chat(models.Model):
    userid = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50, blank=True, null=True)
    emailid = models.CharField(max_length=50)
    password = models.CharField(max_length=512)
    defaultorgid = models.CharField(max_length=50)
    defaultroleid = models.CharField(max_length=50)
    defaultorgaccessrights = models.IntegerField()
    status = models.IntegerField()
    enablepasswordexpiry = models.IntegerField()
    daypasswordset = models.DateTimeField()
    dayspasswordexpiresin = models.IntegerField()
    lastpasswordused = models.CharField(max_length=50, blank=True, null=True)
    passwordhint = models.CharField(max_length=255, blank=True, null=True)
    lastlogindate = models.DateTimeField(blank=True, null=True)
    security_pfx_key = models.ImageField(blank=True, null=True)
    security_pfx_password = models.CharField(max_length=512)
    security_key_type = models.CharField(max_length=50)
    usertypeid = models.IntegerField()
    alertenabled = models.IntegerField()
    alertemailid = models.TextField(blank=True, null=True)
    alertsmsid = models.TextField(blank=True, null=True)
    alertoptions = models.IntegerField()
    security_certificatestatus = models.IntegerField()
    TimeZoneID = models.CharField(max_length=100)
    directemail_ref = models.UUIDField(unique=True)
    PreferredLanguage = models.CharField(max_length=50)
    externalapiconfig = models.TextField(blank=True, null=True)
    failedattempts = models.IntegerField()
    islocked = models.IntegerField()
    lockunlockdatetime = models.DateTimeField(blank=True, null=True)
    istwofactorauthenticationenabled = models.IntegerField()
    isresetpassword = models.IntegerField()
    HIPAAStatus = models.IntegerField()
    TCStatus = models.IntegerField()
    TCADate = models.DateTimeField(blank=True, null=True)
    createdby = models.CharField(max_length=50)
    createddate = models.DateTimeField()
    lastupdatedby = models.CharField(max_length=50)
    lastupdateddate = models.DateTimeField()
    rememberme = models.CharField(max_length=100, blank=True, null=True)
    OTPCode = models.IntegerField()
    OTPAttempt = models.IntegerField()

    def __str__(self):
        return self.userid




class Message(models.Model):
    # Define your model fields here
    MsgID = models.CharField(max_length=50)
    SessionGUID = models.CharField(max_length=128)
    eTXPatientGUID = models.CharField(max_length=128)
    MsgFrom = models.CharField(max_length=20)
    MsgTo = models.CharField(max_length=20)
    SourceType = models.CharField(max_length=50)
    MsgText = models.CharField(max_length=1600)
    DocMIMEType = models.CharField(max_length=255, blank=True, null=True)
    DocSize = models.FloatField(blank=True, null=True)
    DocURL = models.CharField(max_length=255, blank=True, null=True)
    DocBLOB = models.BinaryField(blank=True, null=True)
    Direction = models.CharField(max_length=50)
    Status = models.CharField(max_length=50)
    ReadStatus = models.IntegerField()
    MsgHistory = models.TextField(blank=True, null=True)
    IntegrationFlag = models.IntegerField()
    IsDeleted = models.IntegerField()
    CreatedBy = models.CharField(max_length=50)
    CreatedDate = models.DateTimeField()
    LastUpdatedBy = models.CharField(max_length=50)
    LastUpdatedDate = models.DateTimeField()

    def __str__(self):
        return self.MsgID