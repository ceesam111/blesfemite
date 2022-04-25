from decimal import Decimal
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


User = settings.AUTH_USER_MODEL

class Withdrawal(models.Model):
	user = models.ForeignKey(
        User,
        related_name='withdrawals',
        on_delete=models.CASCADE,)
        
	amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[
            MinValueValidator(Decimal('3000.00'))])
                
	timestamp = models.DateTimeField(auto_now_add=True)
	
	wallet_address = models.TextField(max_length=500, blank= True)
	
	phone_number = models.IntegerField(blank= True)
	
	bank_details = models.TextField(max_length=500, blank=True)
		
	def __str__(self):
		return str(self.user)

class MTN_AIRTIME(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='mtn_airtimes',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=False)
	
	Amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[
            MinValueValidator(Decimal('50.00'))])
	
	
	Confirmation= models.TextField(blank=True)

       
	timestamp = models.DateTimeField(auto_now_add=True)
	
	    	
	def __str__(self):
		return str(self.user)

	
class GLO_AIRTIME(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='glo_airtimes',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=False)
	
	Amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[
            MinValueValidator(Decimal('50.00'))])
	
	
	Confirmation= models.TextField(blank=True)

       
	timestamp = models.DateTimeField(auto_now_add=True)
	
	    	
	def __str__(self):
		return str(self.user)

	
	
class AIRTEL_AIRTIME(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='airtel_airtimes',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=False)
	
	Amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[
            MinValueValidator(Decimal('50.00'))])
		
	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)	
	    	
	def __str__(self):
		return str(self.user)
	
class MTN_AWUF_AIRTIME(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='mtn_awuf_airtimes',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
	
	Amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[
            MinValueValidator(Decimal('50.00'))])
		
	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

	
class MTN_SHARE_AIRTIME(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='mtn_share_airtimes',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
	
	
	Amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[
            MinValueValidator(Decimal('50.00'))])
	
	
	Confirmation= models.IntegerField(blank=True)

       
	timestamp = models.DateTimeField(auto_now_add=True)
	
	    	
	def __str__(self):
		return str(self.user)

class MTN_500MB_SME(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='mtn_500mb_smes',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
	#Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class MTN_1GB_SME(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='mtn2',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
	#Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class MTN_2GB_SME(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='mtn3',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
	#Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)


class MTN_3GB_SME(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='mtn4',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
	#Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class MTN_4GB_SME(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='mtn5',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
	#Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class MTN_5GB_SME(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='mtn6',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
	#Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class MTN_10GB_SME(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='mtn7',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
	#Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class MTN_1GB_WD(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='mtn8',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
	#Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class MTN_1P5GB_MD(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='mtn10',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
	#Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)
		
class MTN_2GB_MD(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='mtn11',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
	#Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class MTN_20GB_WD(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='mtn12',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
	#Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class GLO_50MB(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='glo1',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
	#Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class GLO_150MB(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='glo2',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
	#Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class GLO_350MB(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='glo3',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
	#Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class GLO_2P9GB(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='glo4',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
	#Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class GLO_4P1GB(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='glo5',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
	#Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class GLO_5P8GB(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='glo6',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class GLO_7P7GB(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='glo7',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class GLO_13P75GB(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='glo8',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class GLO_18P25GB(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='glo9',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
	#Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class AIRTEL_750MB(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='airtel1',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class AIRTEL_1GB(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='airtel2',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)


class AIRTEL_2GB(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='airtel3',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)


class AIRTEL_3GB(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='airtel4',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)


class AIRTEL_6GB(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='airtel5',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)


class AIRTEL_10GB(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='airtel6',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)


class AIRTEL_20GB(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='airtel7',
        on_delete=models.CASCADE,)
   		
	Mobile_Number= models.IntegerField(blank=True)
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)


class DSTV_PADI(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='dstv1',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class DSTV_XTRAVIEW(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='dstv2',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class DSTV_ASIAN_ADDON(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='dstv3',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class DSTV_FRENCH_BOUGUET(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='dstv4',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class DSTV_COMPACT_PLUS_F(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='dstv5',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class DSTV_CONFAM(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='dstv6',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)        
		
#	Confirmation= models.IntegerField(max_length=50,blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)

class DSTV_YANGA(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='dstv7',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)
		
class DSTV_PREMIUM(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='dstv8',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)		

class DSTV_COMPACT_PLUS(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='dstv9',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)		

class DSTV_COMPACT_PLUS_ASIAN_ADDON(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='dstv10',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)						

class GOTV_JOLLI(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='gotv1',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)								

class GOTV_SMALLIE(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='gotv2',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)													

class GOTV_LITE_QUART(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='gotv3',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)																


class GOTV_LITE_YEAR(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='gotv4',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)																
class GOTV_MAX(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='gotv5',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)																
class GOTV_JINJA(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='gotv6',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)																
class STARTIME_SMART_M(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='startime1',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)																

class STARTIME_BASIC_M(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='startime2',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)															
class STARTIME_CLASSIC_M(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='startime3',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)															
class STARTIME_NOVA_M(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='startime4',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)															

class STARTIME_SMART_W(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='startime5',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.CharField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)																

class STARTIME_BASIC_W(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='startime6',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)															
class STARTIME_CLASSIC_W(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='startime7',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)															
class STARTIME_NOVA_W(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='startime8',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)															

class STARTIME_SMART_D(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='startime9',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)																

class STARTIME_BASIC_D(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='startime10',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)															
class STARTIME_CLASSIC_D(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='startime11',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)															
class STARTIME_NOVA_D(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='startime12',
        on_delete=models.CASCADE,)
   
	Smart_Card_Number_or_IUC = models.CharField(max_length=50,blank=True)
        
		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)															
														
class ELECT_EKO_PRE(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='elect1',
        on_delete=models.CASCADE,)
	
	Amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[
            MinValueValidator(Decimal('500.00'))
        ]
    ) 
	
	Meter_Number= models.CharField(max_length=50,blank=True)
 		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)															
    
class ELECT_IKEJA_PRE(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='elect2',
        on_delete=models.CASCADE,)
	
	Amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[
            MinValueValidator(Decimal('500.00'))
        ]
    ) 
	
	Meter_Number= models.CharField(max_length=50,blank=True)
 		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)											
class ELECT_IBADAN_PRE(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='elect3',
        on_delete=models.CASCADE,)
	
	Amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[
            MinValueValidator(Decimal('500.00'))
        ]
    ) 
	
	Meter_Number= models.CharField(max_length=50,blank=True)
 		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)											

class ELECT_ENUGU_PRE(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='elect4',
        on_delete=models.CASCADE,)
	
	Amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[
            MinValueValidator(Decimal('500.00'))
        ]
    ) 
	
	Meter_Number= models.CharField(max_length=50,blank=True)
 		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)											

class ELECT_EKO_POST(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='elect5',
        on_delete=models.CASCADE,)
	
	Amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[
            MinValueValidator(Decimal('500.00'))
        ]
    ) 
	
	Meter_Number= models.CharField(max_length=50,blank=True)
 		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)															
    
class ELECT_IKEJA_POST(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='elect6',
        on_delete=models.CASCADE,)
	
	Amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[
            MinValueValidator(Decimal('500.00'))
        ]
    ) 
	
	Meter_Number= models.CharField(max_length=50,blank=True)
 		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)											
class ELECT_IBADAN_POST(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='elect7',
        on_delete=models.CASCADE,)
	
	Amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[
            MinValueValidator(Decimal('500.00'))
        ]
    ) 
	
	Meter_Number= models.CharField(max_length=50,blank=True)
 		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)											

class ELECT_ENUGU_POST(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='elect8',
        on_delete=models.CASCADE,)
	
	Amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[
            MinValueValidator(Decimal('500.00'))
        ]
    ) 
	
	Meter_Number= models.CharField(max_length=50,blank=True)
 		
#	Confirmation= models.IntegerField(blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)											
							

class WAEC(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='waec',
        on_delete=models.CASCADE,)
   	
	Email = models.CharField(max_length=50, blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	def __str__(self):
		return str(self.user)
		
class NECO(models.Model):
	
	user = models.ForeignKey(
        User,
        related_name='neco',
        on_delete=models.CASCADE,)
   	
	Email = models.CharField(max_length=50, blank=True)
       
	timestamp = models.DateTimeField(auto_now_add=True)
		    	
	
		
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

class GOTV(models.Model):
    JOLLI= models.IntegerField(blank = True)
    SMALLIE= models.IntegerField(blank = True)
    LITE_QUARTERLY= models.IntegerField(blank = True)
    LITE_YEARLY= models.IntegerField(blank = True)
    MAX= models.IntegerField(blank = True)
    JINJA= models.IntegerField(blank = True)
    
 

        

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
  

        
																																																																																					
																																																																																																																																																																																																																																																											