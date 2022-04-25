from django.db import models

# Create your models here
from django.contrib.auth.models import User
import os
from django.urls import reverse



def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)

class UserProfileInfo(models.Model):

    #creating a relationship with user class (not inheriting)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #adding additional attributes

    referral_email =  models.TextField(max_length=50)   
    
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2)
        
    ref_balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2)
        
    bio = models.CharField(max_length=500)
    bonus = models.TextField(max_length=100)
    profile_pic = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Picture", blank=True)
    Creator = 'Creator'
    Vnodite = 'Vnodite'
    Miner = 'Miner'
    user_types = [
        (Creator, 'Creator'),
        (Vnodite, 'Vnodite'),
        (Miner, 'Miner'),
    ]
    user_type = models.CharField(max_length=10, choices=user_types, default=Vnodite)

    def __str__(self):
        return self.user.username

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    feedback = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')


                                       
#class Standard(models.Model):
#    name = models.#CharField(max_length=100, unique=True)
#    description = models.#TextField(max_length=500,blank=True)
    

#    def __str__(self):
       # return self.name

   
        
class Pricetag(models.Model):
    name = models.TextField(max_length=100, unique=True)
    amount = models.CharField(max_length=100, unique=True)  
    tag_one = models.TextField(max_length=100,blank=True)
    tag_two= models.TextField(max_length=100,blank=True)
    tag_three = models.TextField(max_length=100,blank=True)
    tag_four = models.TextField(max_length=100,blank=True)
    tag_five= models.TextField(max_length=100,blank=True)
    overlay = models.TextField(max_length=100,blank=True)
    tag_link = models.TextField(max_length=100,blank=True)
    duration= models.TextField(max_length=100,blank=True)
   
    def __str__(self):
        return self.name

class MTN(models.Model):
    A_500MB_SME = models.IntegerField( blank=True)
    A_1GB_SME= models.IntegerField( blank = True)
    A_2GB_SME= models.IntegerField(blank = True)
    A_3GB_SME= models.IntegerField( blank = True)
    A_4GB_SME= models.IntegerField(blank = True)
    A_5GB_SME= models.IntegerField(blank = True)
    A_10GB_SME= models.IntegerField(blank = True)
    A_1GB_WEEKLY_DIRECT= models.IntegerField(blank = True)
    A_6GB_WEEKLY_DIRECT= models.IntegerField(blank = True)
    A_1_POINT_5GB_MONTHLY_DIRECT= models.IntegerField(blank = True)
    A_2GB_MONTHLY_DIRECT= models.IntegerField(blank = True)
    A_20GB_MONTHLY_DIRECT= models.IntegerField(blank = True)
    
    def __str__(self):
        return self.name

    
   
class GLO(models.Model):
    A_50MB = models.IntegerField(blank = True)
    A_150MB= models.IntegerField(blank = True)
    A_350MB= models.IntegerField(blank = True)
    A_1_POINT_31GB= models.IntegerField(blank = True)
    A_2_POINT_9GB= models.IntegerField(blank = True)
    A_4_POINT_1GB= models.IntegerField(blank = True)
    A_5_POINT_8GB= models.IntegerField(blank = True)
    A_7_POINT_7GB= models.IntegerField(blank = True)
    A_10GB= models.IntegerField(blank = True)
    A_13_POINT_75GB= models.IntegerField(blank = True)
    A_18_POINT_25GB= models.IntegerField(blank = True)
    
    def __str__(self):
        return self.name

    
class DSTV(models.Model):
    PADI = models.IntegerField(blank = True)
    XTRAVIEW= models.IntegerField(blank = True)
    ASIAN_ADDON= models.IntegerField(blank = True)
    FRENCH_BOUQUET= models.IntegerField(blank = True)
    COMPACT_PLUS_FRENCH= models.IntegerField(blank = True)
    CONFAM= models.IntegerField(blank = True)
    YANGA= models.IntegerField(blank = True)
    PREMIUM= models.IntegerField(blank = True)
    COMPACT_PLUS= models.IntegerField(blank = True)
    COMPACT_PLUS_ASIAN_ADDON= models.IntegerField(blank = True)
    
    def __str__(self):
        return self.name


class GOTV(models.Model):
    JOLLI= models.IntegerField(blank = True)
    SMALLIE= models.IntegerField(blank = True)
    LITE_QUARTERLY= models.IntegerField(blank = True)
    LITE_YEARLY= models.IntegerField(blank = True)
    MAX= models.IntegerField(blank = True)
    JINJA= models.IntegerField(blank = True)
    
    def __str__(self):
        return self.name

        

class STARTIMES(models.Model):
    SMART_1MONTH = models.IntegerField(blank = True)
    BASIC_1MONTH= models.IntegerField(blank = True)
    NOVA_1WEEK= models.IntegerField(blank = True)
    NOVA_1MONTH = models.IntegerField(blank = True)
    BASIC_1WEEK= models.IntegerField(blank = True)
    SMART_1WEEK= models.IntegerField(blank = True)
    CLASSIC_1WEEK= models.IntegerField(blank = True)
    CLASSIC_1DAY= models.IntegerField(blank = True)
    SMART_1DAY= models.IntegerField(blank = True)
    BASIC_1DAY= models.IntegerField(blank = True)
    NOVA_1DAY= models.IntegerField(blank = True)
    BASIC_1WEEK= models.IntegerField(blank = True)
    NOVA_1WEEK= models.IntegerField(blank = True)
    SUPER_1WEEK= models.IntegerField(blank = True)
    CLASSIC_1MONTH= models.IntegerField(blank = True)
    
    def __str__(self):
        return self.name

     



class AIRTEL(models.Model):
    A_750MB = models.IntegerField(blank= False)
    A_1_POINT_5GB= models.IntegerField( blank = False)
    A_2GB= models.IntegerField(blank = False)
    A_3GB= models.IntegerField(blank = False)
    A_4_POINT_5GB= models.IntegerField(blank = False)
    A_6GB= models.IntegerField(blank = False)
    A_10GB= models.IntegerField(blank = False)
    A_11GB= models.IntegerField(blank = False)
    A_20GB= models.IntegerField(blank = False)
    A_40GB= models.IntegerField(blank = False)
    
    def __str__(self):
        return self.name

    
class ELECTRICITY(models.Model):
    EKO_PREPAID = models.IntegerField(blank= False)
    IKEJA_PREPAID= models.IntegerField(blank = False)
    IBADAN_PREPAID= models.IntegerField( blank = False)
    ENUGU_PREPAID= models.IntegerField( blank = False)
    ABUJA_PREPAID= models.IntegerField(blank = False)
    EKO_POSTPAID= models.IntegerField(blank = False)
    ENUGU_POSTPAID= models.IntegerField(blank = False)
    ABUJA_POSTPAID= models.IntegerField(blank = False)
    IBADAN_POSTPAID= models.IntegerField(blank = False)
    IKEJA_POSTPAID= models.IntegerField( blank = False)

class EXAM(models.Model):
  WAEC_PIN  = models.IntegerField( blank= False)
  NECO_PIN= models.IntegerField( blank = False)
  
  def __str__(self):
        return self.name

        





from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import AbstractUser
#from .managers import UserManager



class User(models.Model):   
  #  objects = UserManager()
    @property
    def balance(self):
        if hasattr(self, 'account'):
            return self.account.balance
        return None


class AccountDetails(models.Model):
    user = models.OneToOneField(
        User,
        related_name='account',
        on_delete=models.CASCADE,
    )

    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2)
  
                     