# Generated by Django 5.0.6 on 2024-06-05 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('middlename', models.CharField(blank=True, max_length=50, null=True)),
                ('emailid', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=512)),
                ('defaultorgid', models.CharField(max_length=50)),
                ('defaultroleid', models.CharField(max_length=50)),
                ('defaultorgaccessrights', models.IntegerField()),
                ('status', models.IntegerField()),
                ('enablepasswordexpiry', models.IntegerField()),
                ('daypasswordset', models.DateTimeField()),
                ('dayspasswordexpiresin', models.IntegerField()),
                ('lastpasswordused', models.CharField(blank=True, max_length=50, null=True)),
                ('passwordhint', models.CharField(blank=True, max_length=255, null=True)),
                ('lastlogindate', models.DateTimeField(blank=True, null=True)),
                ('security_pfx_key', models.ImageField(blank=True, null=True, upload_to='')),
                ('security_pfx_password', models.CharField(max_length=512)),
                ('security_key_type', models.CharField(max_length=50)),
                ('usertypeid', models.IntegerField()),
                ('alertenabled', models.IntegerField()),
                ('alertemailid', models.TextField(blank=True, null=True)),
                ('alertsmsid', models.TextField(blank=True, null=True)),
                ('alertoptions', models.IntegerField()),
                ('security_certificatestatus', models.IntegerField()),
                ('TimeZoneID', models.CharField(max_length=100)),
                ('directemail_ref', models.UUIDField(unique=True)),
                ('PreferredLanguage', models.CharField(max_length=50)),
                ('externalapiconfig', models.TextField(blank=True, null=True)),
                ('failedattempts', models.IntegerField()),
                ('islocked', models.IntegerField()),
                ('lockunlockdatetime', models.DateTimeField(blank=True, null=True)),
                ('istwofactorauthenticationenabled', models.IntegerField()),
                ('isresetpassword', models.IntegerField()),
                ('HIPAAStatus', models.IntegerField()),
                ('TCStatus', models.IntegerField()),
                ('TCADate', models.DateTimeField(blank=True, null=True)),
                ('createdby', models.CharField(max_length=50)),
                ('createddate', models.DateTimeField()),
                ('lastupdatedby', models.CharField(max_length=50)),
                ('lastupdateddate', models.DateTimeField()),
                ('rememberme', models.CharField(blank=True, max_length=100, null=True)),
                ('OTPCode', models.IntegerField()),
                ('OTPAttempt', models.IntegerField()),
            ],
        ),
    ]
