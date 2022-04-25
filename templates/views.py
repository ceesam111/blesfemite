from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import Http404
from django.shortcuts import render, redirect
import smtplib
from transactions.models import MTN,GLO,AIRTEL,DSTV,DSTV,GOTV,STARTIMES,ELECTRICITY,EXAM
from mycompany.models import UserProfileInfo, User
from .forms import  WithdrawalForm, Airtime1Form,Airtime2Form,Airtime4Form,Airtime5Form,Airtime6Form,Mtn1Form,Mtn1Form,Mtn2Form,Mtn3Form,Mtn4Form,Mtn5Form,Mtn6Form,Mtn7Form,Mtn8Form,Mtn9Form,Mtn10Form,Mtn11Form,Glo1Form,Glo1Form,Glo2Form,Glo3Form,Glo4Form,Glo5Form,Glo6Form,Glo7Form,Glo8Form,Glo9Form,Airtel1Form,Airtel2Form,Airtel3Form,Airtel4Form,Airtel5Form,Airtel6Form,Airtel7Form,Dstv1Form,Dstv2Form,Dstv3Form,Dstv4Form,Dstv5Form,Dstv6Form,Dstv7Form,Dstv8Form,Dstv9Form,Dstv10Form,Startime1Form,Startime2Form,Startime3Form,Startime4Form,Startime5Form,Startime6Form,Startime7Form,Startime8Form,Startime9Form,Startime9Form,Startime10Form,Startime11Form,Startime12Form,Elect1Form,Elect2Form,Elect3Form,Elect4Form,Elect5Form,Elect6Form,Elect7Form,Elect8Form,Gotv1Form,Gotv2Form,Gotv3Form,Gotv4Form,Gotv5Form,Gotv6Form,WaecForm,NecoForm

import smtplib, ssl

def amount():
	mtns = MTN.objects.all()
	for mtn in mtns:
	    Amount = mtn.A_500MB_SME
     


#@login_required()
def deposit_view(request):
	deposit.user.userprofileinfo.balance += 10
	deposit.user.userprofileinfo.save()
	return redirect("index")

#@login_required()
def withdrawal_view(request):
    form = WithdrawalForm(request.POST or None)

    if form.is_valid():
        withdrawal = form.save(commit=False)
        withdrawal.user = request.user
        withdrawal.save()
        # subtracts users withdrawal from balance.
        
        if withdrawal.user.userprofileinfo.balance < withdrawal.amount:
            messages.success(
            request, 'Your minimum withdrawal is {} Shiba coin.'.format(withdrawal.user.userprofileinfo.balance)
        )
        
        else:
        	withdrawal.user.userprofileinfo.balance -= withdrawal.amount
        	withdrawal.user.userprofileinfo.save()
        	messages.success(
            request, 'You have withdraw {} Shiba coin. This can take up to a few minutes to appear in your wallet.'.format(withdrawal.amount)
        )        
        	return redirect("index")

    context = {
        "title": "Withdraw",
        "form": form
    }
    return render(request, "transactions/form.html", context)

#@login_required()
def airtime1_view(request):
    form = Airtime1Form(request.POST or None)

    if form.is_valid():
        airtime1 = form.save(commit=False)
        airtime1.user = request.user
        airtime1.save()
        # subtracts users withdrawal from balance.
        
        if airtime1.user.userprofileinfo.balance < airtime1.Amount:
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	#{} mtn vtu airtime to this number
        	{} .""".format(airtime1.Amount
        	, airtime1.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	airtime1.user.userprofileinfo.balance -= airtime1.Amount
        	airtime1.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase #{} Mtn vtu airtime to this number {}.'.format(airtime1.Amount, airtime1.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

               
        
        	
def airtime2_view(request):
    form = Airtime2Form(request.POST or None)

    if form.is_valid():
        airtime2 = form.save(commit=False)
        airtime2.user = request.user
        airtime2.save()
        # subtracts users withdrawal from balance.
        
        if airtime2.user.userprofileinfo.balance < airtime2.Amount:
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	#{} glo vtu airtime to this number
        	{} .""".format(airtime2.Amount
        	, airtime1.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	airtime2.user.userprofileinfo.balance -= airtime2.Amount
        	airtime2.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase #{} Mtn vtu airtime to this number {}.'.format(airtime1.Amount, airtime2.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

    
    
    
def airtime4_view(request):
    form = Airtime4Form(request.POST or None)

    if form.is_valid():
        airtime4 = form.save(commit=False)
        airtime4.user = request.user
        airtime4.save()
        # subtracts users withdrawal from balance.
        
        if airtime4.user.userprofileinfo.balance < airtime4.Amount:
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	#{} airtel vtu airtime to this number
        	{} .""".format(airtime4.Amount
        	, airtime4.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	airtime4.user.userprofileinfo.balance -= airtime4.Amount
        	airtime4.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase #{} Mtn vtu airtime to this number {}.'.format(airtime4.Amount, airtime4.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

    
    
 
def airtime5_view(request):
    form = Airtime5Form(request.POST or None)

    if form.is_valid():
        airtime5 = form.save(commit=False)
        airtime5.user = request.user
        airtime5.save()
        # subtracts users withdrawal from balance.
        
        if airtime5.user.userprofileinfo.balance < airtime5.Amount:
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	#{} mtn awuf airtime 
        	to this number
        	{} .""".format(airtime5.Amount
        	, airtime5.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	airtime5.user.userprofileinfo.balance -= airtime5.Amount
        	airtime5.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase #{} Mtn vtu airtime to this number {}.'.format(airtime5.Amount, airtime5.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

    
    
def airtime6_view(request):
    form = Airtime6Form(request.POST or None)

    if form.is_valid():
        airtime6 = form.save(commit=False)
        airtime6.user = request.user
        airtime6.save()
        # subtracts users withdrawal from balance.
        
        if airtime6.user.userprofileinfo.balance < airtime6.Amount:
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	#{} mtn share and sell vtu airtime
        	to this number
        	{} .""".format(airtime6.Amount
        	, airtime6.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	airtime6.user.userprofileinfo.balance -= airtime6.Amount
        	airtime6.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase #{} Mtn vtu airtime to this number {}.'.format(airtime6.Amount, airtime6.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)


def mtn1_view(request):
    form = Mtn1Form(request.POST or None)

    if form.is_valid():
        mtn1 = form.save(commit=False)
        mtn1.user = request.user
        mtn1.save()
        # subtracts users withdrawal from balance.
        Amount = 160
        Plan= str("500MB")
                       
        if mtn1.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} mtn data to this number
        	{} .""".format(Plan
        	, mtn1.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	mtn1.user.userprofileinfo.balance -= Amount
        	mtn1.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Mtn SME Data to this number {}.'.format(Plan, mtn1.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def mtn2_view(request):
    form = Mtn2Form(request.POST or None)

    if form.is_valid():
        mtn2 = form.save(commit=False)
        mtn2.user = request.user
        mtn2.save()
        # subtracts users withdrawal from balance.
        Amount = 260
        Plan= str("1GB")
                       
        if mtn2.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} mtn data to this number
        	{} .""".format(Plan
        	, mtn2.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	mtn2.user.userprofileinfo.balance -= Amount
        	mtn2.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Mtn SME Data to this number {}.'.format(Plan, mtn1.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)


def mtn3_view(request):
    form = Mtn3Form(request.POST or None)

    if form.is_valid():
        mtn3 = form.save(commit=False)
        mtn3.user = request.user
        mtn3.save()
        # subtracts users withdrawal from balance.
        Amount = 520
        Plan= str("2GB")
                       
        if mtn3.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} mtn data to this number
        	{} .""".format(Plan
        	, mtn3.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	mtn3.user.userprofileinfo.balance -= Amount
        	mtn3.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Mtn SME Data to this number {}.'.format(Plan, mtn1.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def mtn4_view(request):
    form = Mtn4Form(request.POST or None)

    if form.is_valid():
        mtn4 = form.save(commit=False)
        mtn4.user = request.user
        mtn4.save()
        # subtracts users withdrawal from balance.
        Amount = 780
        Plan= str("3GB")
                       
        if mtn4.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} mtn data to this number
        	{} .""".format(Plan
        	, mtn4.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	mtn4.user.userprofileinfo.balance -= Amount
        	mtn4.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Mtn SME Data to this number {}.'.format(Plan, mtn4.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)



def mtn5_view(request):
    form = Mtn5Form(request.POST or None)

    if form.is_valid():
        mtn5 = form.save(commit=False)
        mtn5.user = request.user
        mtn5.save()
        # subtracts users withdrawal from balance.
        Amount = 1040
        
        Plan= str("4GB")
                       
        if mtn5.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} mtn data to this number
        	{} .""".format(Plan
        	, mtn5.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	mtn5.user.userprofileinfo.balance -= Amount
        	mtn5.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Mtn SME Data to this number {}.'.format(Plan, mtn5.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)


def mtn6_view(request):
    form = Mtn6Form(request.POST or None)

    if form.is_valid():
        mtn6 = form.save(commit=False)
        mtn6.user = request.user
        mtn6.save()
        # subtracts users withdrawal from balance.
        Amount = 1300
        Plan= str("5GB")
                       
        if mtn6.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} mtn data to this number
        	{} .""".format(Plan
        	, mtn6.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	mtn6.user.userprofileinfo.balance -= Amount
        	mtn6.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Mtn SME Data to this number {}.'.format(Plan, mtn6.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)


def mtn7_view(request):
    form = Mtn7Form(request.POST or None)

    if form.is_valid():
        mtn7 = form.save(commit=False)
        mtn7.user = request.user
        mtn7.save()
        # subtracts users withdrawal from balance.
        Amount = 2600
        Plan= str("10GB")
                       
        if mtn7.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} mtn data to this number
        	{} .""".format(Plan
        	, mtn7.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	mtn7.user.userprofileinfo.balance -= Amount
        	mtn7.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Mtn SME Data to this number {}.'.format(Plan, mtn7.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)


def mtn8_view(request):
    form = Mtn8Form(request.POST or None)

    if form.is_valid():
        mtn8 = form.save(commit=False)
        mtn8.user = request.user
        mtn8.save()
        # subtracts users withdrawal from balance.
        Amount = 800
        Plan= str("1GB")
                       
        if mtn8.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} mtn data to this number
        	{} .""".format(Plan
        	, mtn8.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	mtn8.user.userprofileinfo.balance -= Amount
        	mtn8.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Mtn SME Data to this number {}.'.format(Plan, mtn8.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)


def mtn9_view(request):
    form = Mtn9Form(request.POST or None)

    if form.is_valid():
        mtn9 = form.save(commit=False)
        mtn9.user = request.user
        mtn9.save()
        # subtracts users withdrawal from balance.
        Amount = 1160
        Plan= str("2GB")
                       
        if mtn9.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} mtn data to this number
        	{} .""".format(Plan
        	, mtn9.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	mtn9.user.userprofileinfo.balance -= Amount
        	mtn9.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Mtn SME Data to this number {}.'.format(Plan, mtn9.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)


def mtn10_view(request):
    form = Mtn10Form(request.POST or None)

    if form.is_valid():
        mtn10 = form.save(commit=False)
        mtn10.user = request.user
        mtn10.save()
        # subtracts users withdrawal from balance.
        Amount = 10000
        Plan= str("20GB")
                       
        if mtn10.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} mtn data to this number
        	{} .""".format(Plan
        	, mtn10.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	mtn10.user.userprofileinfo.balance -= Amount
        	mtn10.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Mtn SME Data to this number {}.'.format(Plan, mtn10.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)


def glo1_view(request):
    form = Glo1Form(request.POST or None)

    if form.is_valid():
        glo1 = form.save(commit=False)
        glo1.user = request.user
        glo1.save()
        # subtracts users withdrawal from balance.
        Amount = 50
        Plan= str("50MB")
                       
        if glo1.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} Glo data to this number
        	{} .""".format(Plan
        	, mtn1.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	glo1.user.userprofileinfo.balance -= Amount
        	glo1.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Glo SME Data to this number {}.'.format(Plan, glo1.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)


def glo2_view(request):
    form = Glo2Form(request.POST or None)

    if form.is_valid():
        glo2 = form.save(commit=False)
        glo2.user = request.user
        glo2.save()
        # subtracts users withdrawal from balance.
        Amount = 100
        Plan= str("150MB")
                       
        if glo2.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} Glo data to this number
        	{} .""".format(Plan
        	, mtn2.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	glo2.user.userprofileinfo.balance -= Amount
        	glo2.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Glo SME Data to this number {}.'.format(Plan, glo2.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def glo3_view(request):
    form = Glo3Form(request.POST or None)

    if form.is_valid():
        glo3 = form.save(commit=False)
        glo3.user = request.user
        glo3.save()
        # subtracts users withdrawal from balance.
        Amount = 200
        Plan= str("350MB")
                       
        if glo1.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} Glo data to this number
        	{} .""".format(Plan
        	, mtn3.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	glo3.user.userprofileinfo.balance -= Amount
        	glo3.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Glo SME Data to this number {}.'.format(Plan, glo3.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)


def glo4_view(request):
    form = Glo4Form(request.POST or None)

    if form.is_valid():
        glo4 = form.save(commit=False)
        glo4.user = request.user
        glo4.save()
        # subtracts users withdrawal from balance.
        Amount = 1000
        Plan= str("2.9GB")
                       
        if glo4.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} Glo data to this number
        	{} .""".format(Plan
        	, glo4.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	glo4.user.userprofileinfo.balance -= Amount
        	glo4.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Glo SME Data to this number {}.'.format(Plan, glo4.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)


def glo5_view(request):
    form = Glo5Form(request.POST or None)

    if form.is_valid():
        glo5 = form.save(commit=False)
        glo5.user = request.user
        glo5.save()
        # subtracts users withdrawal from balance.
        Amount = 1450
        Plan= str("4.1GB")
                       
        if glo5.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} Glo data to this number
        	{} .""".format(Plan
        	, glo5.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	glo5.user.userprofileinfo.balance -= Amount
        	glo5.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Glo SME Data to this number {}.'.format(Plan, glo5.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def glo6_view(request):
    form = Glo6Form(request.POST or None)

    if form.is_valid():
        glo6 = form.save(commit=False)
        glo6.user = request.user
        glo6.save()
        # subtracts users withdrawal from balance.
        Amount = 1950
        Plan= str("5.8GB")
                       
        if glo6.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} Glo data to this number
        	{} .""".format(Plan
        	, glo6.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	glo6.user.userprofileinfo.balance -= Amount
        	glo6.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Glo SME Data to this number {}.'.format(Plan, glo6.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)


def glo7_view(request):
    form = Glo7Form(request.POST or None)

    if form.is_valid():
        glo7 = form.save(commit=False)
        glo7.user = request.user
        glo7.save()
        # subtracts users withdrawal from balance.
        Amount = 2400
        Plan= str("7.7GB")
                       
        if glo7.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} Glo data to this number
        	{} .""".format(Plan
        	, glo7.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	glo7.user.userprofileinfo.balance -= Amount
        	glo7.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Glo SME Data to this number {}.'.format(Plan, glo7.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)
          
  
          
def glo8_view(request):
    form = Glo8Form(request.POST or None)

    if form.is_valid():
        glo8 = form.save(commit=False)
        glo8.user = request.user
        glo8.save()
        # subtracts users withdrawal from balance.
        Amount = 2900
        Plan= str("10GB")
                       
        if glo8.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} Glo data to this number
        	{} .""".format(Plan
        	, glo8.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	glo8.user.userprofileinfo.balance -= Amount
        	glo8.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Glo SME Data to this number {}.'.format(Plan, glo8.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)
  
          
def glo9_view(request):
    form = Glo9Form(request.POST or None)

    if form.is_valid():
        glo9 = form.save(commit=False)
        glo9.user = request.user
        glo9.save()
        # subtracts users withdrawal from balance.
        Amount = 3850
        Plan= str("13.25GB")
                       
        if glo9.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} Glo data to this number
        	{} .""".format(Plan
        	, glo9.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	glo9.user.userprofileinfo.balance -= Amount
        	glo9.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Glo SME Data to this number {}.'.format(Plan, glo9.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)
  
def glo10_view(request):
    form = Glo10Form(request.POST or None)

    if form.is_valid():
        glo10 = form.save(commit=False)
        glo10.user = request.user
        glo10.save()
        # subtracts users withdrawal from balance.
        Amount = 5000
        Plan= str("18.25GB")
                       
        if glo10.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} Glo data to this number
        	{} .""".format(Plan
        	, glo10.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	glo10.user.userprofileinfo.balance -= Amount
        	glo10.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Glo SME Data to this number {}.'.format(Plan, glo10.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

          
def airtel1_view(request):
    form = Airtel1Form(request.POST or None)

    if form.is_valid():
        airtel1 = form.save(commit=False)
        airtel1.user = request.user
        airtel1.save()
        # subtracts users withdrawal from balance.
        Amount = 500
        Plan= str("750MB")
                       
        if airtel1.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} Airtel data to this number
        	{} .""".format(Plan
        	, airtel1.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	airtel1.user.userprofileinfo.balance -= Amount
        	airtel1.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Airtel SME Data to this number {}.'.format(Plan, airtel1.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

          
   
def airtel2_view(request):
    form = Airtel2Form(request.POST or None)

    if form.is_valid():
        airtel2 = form.save(commit=False)
        airtel2.user = request.user
        airtel2.save()
        # subtracts users withdrawal from balance.
        Amount = 1180
        Plan= str("2GB")
                       
        if airtel2.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} Airtel data to this number
        	{} .""".format(Plan
        	, airtel2.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	airtel2.user.userprofileinfo.balance -= Amount
        	airtel2.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Airtel SME Data to this number {}.'.format(Plan, airtel2.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)
      
def airtel3_view(request):
    form = Airtel3Form(request.POST or None)

    if form.is_valid():
        airtel3 = form.save(commit=False)
        airtel3.user = request.user
        airtel3.save()
        # subtracts users withdrawal from balance.
        Amount = 1480
        Plan= str("3GB")
                       
        if airtel3.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} Airtel data to this number
        	{} .""".format(Plan
        	, airtel3.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	airtel3.user.userprofileinfo.balance -= Amount
        	airtel3.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Airtel SME Data to this number {}.'.format(Plan, airtel3.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def airtel4_view(request):
    form = Airtel4Form(request.POST or None)

    if form.is_valid():
        airtel4 = form.save(commit=False)
        airtel4.user = request.user
        airtel4.save()
        # subtracts users withdrawal from balance.
        Amount = 1950
        Plan= str("4GB")
                       
        if airtel4.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} Airtel data to this number
        	{} .""".format(Plan
        	, airtel1.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	airtel4.user.userprofileinfo.balance -= Amount
        	airtel4.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Airtel SME Data to this number {}.'.format(Plan, airtel4.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def airtel5_view(request):
    form = Airtel5Form(request.POST or None)

    if form.is_valid():
        airtel5 = form.save(commit=False)
        airtel5.user = request.user
        airtel5.save()
        # subtracts users withdrawal from balance.
        Amount = 2450
        Plan= str("6GB")
                       
        if airtel5.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} Airtel data to this number
        	{} .""".format(Plan
        	, airtel5.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	airtel5.user.userprofileinfo.balance -= Amount
        	airtel5.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Airtel SME Data to this number {}.'.format(Plan, airtel5.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)
    

def airtel6_view(request):
    form = Airtel6Form(request.POST or None)

    if form.is_valid():
        airtel6 = form.save(commit=False)
        airtel6.user = request.user
        airtel6.save()
        # subtracts users withdrawal from balance.
        Amount = 2950
        Plan= str("10GB")
                       
        if airtel6.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} Airtel data to this number
        	{} .""".format(Plan
        	, airtel6.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	airtel6.user.userprofileinfo.balance -= Amount
        	airtel6.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Airtel SME Data to this number {}.'.format(Plan, airtel6.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)
            
def airtel7_view(request):
    form = Airtel7Form(request.POST or None)

    if form.is_valid():
        airtel7 = form.save(commit=False)
        airtel7.user = request.user
        airtel7.save()
        # subtracts users withdrawal from balance.
        Amount = 5800
        Plan= str("20GB")
                       
        if airtel7.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} Airtel data to this number
        	{} .""".format(Plan
        	, airtel7.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	airtel7.user.userprofileinfo.balance -= Amount
        	airtel7.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Airtel SME Data to this number {}.'.format(Plan, airtel7.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)
                                   

def airtel8_view(request):
    form = Airtel8Form(request.POST or None)

    if form.is_valid():
        airtel8 = form.save(commit=False)
        airtel8.user = request.user
        airtel8.save()
        # subtracts users withdrawal from balance.
        Amount = 11000
        Plan= str("40GB")
                       
        if airtel8.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	{} Airtel data to this number
        	{} .""".format(Plan
        	, airtel8.Mobile_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	airtel8.user.userprofileinfo.balance -= Amount
        	airtel8.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Airtel SME Data to this number {}.'.format(Plan, airtel8.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)


def dstv1_view(request):
    form = Dstv1Form(request.POST or None)

    if form.is_valid():
        dstv1 = form.save(commit=False)
        dstv1.user = request.user
        dstv1.save()
        # subtracts users withdrawal from balance.
        Amount = 2200
        Plan= str("PADI")
                       
        if dstv1.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Dstv {} Package to this IUC 
        	{} .""".format(Plan
        	, dstv1.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	dstv1.user.userprofileinfo.balance -= Amount
        	dstv1.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, dstv1.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def dstv2_view(request):
    form = Dstv2Form(request.POST or None)

    if form.is_valid():
        dstv2 = form.save(commit=False)
        dstv2.user = request.user
        dstv2.save()
        # subtracts users withdrawal from balance.
        Amount = 2950
        Plan= str("XTRAVIEW")
                       
        if dstv2.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Dstv {} Package to this IUC 
        	{} .""".format(Plan
        	, dstv2.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	dstv2.user.userprofileinfo.balance -= Amount
        	dstv2.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, dstv2.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def dstv3_view(request):
    form = Dstv3Form(request.POST or None)

    if form.is_valid():
        dstv3 = form.save(commit=False)
        dstv3.user = request.user
        dstv3.save()
        # subtracts users withdrawal from balance.
        Amount = 7150
        Plan= str("Asian Add On")
                       
        if dstv3.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Dstv {} Package to this IUC 
        	{} .""".format(Plan
        	, dstv3.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	dstv3.user.userprofileinfo.balance -= Amount
        	dstv3.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, dstv3.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def dstv4_view(request):
    form = Dstv4Form(request.POST or None)

    if form.is_valid():
        dstv4 = form.save(commit=False)
        dstv4.user = request.user
        dstv4.save()
        # subtracts users withdrawal from balance.
        Amount = 4150
        Plan= str("FRENCH BOUGUET")
                       
        if dstv4.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Dstv {} Package to this IUC 
        	{} .""".format(Plan
        	, dstv4.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	dstv4.user.userprofileinfo.balance -= Amount
        	dstv4.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, dstv4.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def dstv5_view(request):
    form = Dstv5Form(request.POST or None)

    if form.is_valid():
        dstv5 = form.save(commit=False)
        dstv5.user = request.user
        dstv5.save()
        # subtracts users withdrawal from balance.
        Amount = 11700
        Plan= str("CONPACT PLUS FRENCH")
                       
        if dstv5.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Dstv {} Package to this IUC 
        	{} .""".format(Plan
        	, dstv5.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	dstv5.user.userprofileinfo.balance -= Amount
        	dstv5.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, dstv5.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def dstv6_view(request):
    form = Dstv6Form(request.POST or None)

    if form.is_valid():
        dstv6 = form.save(commit=False)
        dstv6.user = request.user
        dstv6.save()
        # subtracts users withdrawal from balance.
        Amount = 5350
        Plan= str("CONFAM")
                       
        if dstv6.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Dstv {} Package to this IUC 
        	{} .""".format(Plan
        	, dstv6.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	dstv6.user.userprofileinfo.balance -= Amount
        	dstv6.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, dstv6.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def dstv7_view(request):
    form = Dstv7Form(request.POST or None)

    if form.is_valid():
        dstv7 = form.save(commit=False)
        dstv7.user = request.user
        dstv7.save()
        # subtracts users withdrawal from balance.
        Amount = 3000
        Plan= str("YANGA")
                       
        if dstv7.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Dstv {} Package to this IUC 
        	{} .""".format(Plan
        	, dstv7.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	dstv7.user.userprofileinfo.balance -= Amount
        	dstv7.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, dstv7.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def dstv8_view(request):
    form = Dstv8Form(request.POST or None)

    if form.is_valid():
        dstv8 = form.save(commit=False)
        dstv8.user = request.user
        dstv8.save()
        # subtracts users withdrawal from balance.
        Amount = 21050
        Plan= str("PREMIUM")
                       
        if dstv8.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Dstv {} Package to this IUC 
        	{} .""".format(Plan
        	, dstv8.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	dstv8.user.userprofileinfo.balance -= Amount
        	dstv8.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, dstv8.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def dstv9_view(request):
    form = Dstv9Form(request.POST or None)

    if form.is_valid():
        dstv9 = form.save(commit=False)
        dstv9.user = request.user
        dstv9.save()
        # subtracts users withdrawal from balance.
        Amount = 14300
        Plan= str("CONPACT PLUS")
                       
        if dstv9.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Dstv {} Package to this IUC 
        	{} .""".format(Plan
        	, dstv9.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	dstv9.user.userprofileinfo.balance -= Amount
        	dstv9.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, dstv9.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def dstv10_view(request):
    form = Dstv10Form(request.POST or None)

    if form.is_valid():
        dstv10 = form.save(commit=False)
        dstv10.user = request.user
        dstv10.save()
        # subtracts users withdrawal from balance.
        Amount = 7150
        Plan= str("COMPACT PLUS ASIAN ADD ON")
                       
        if dstv10.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Dstv {} Package to this IUC 
        	{} .""".format(Plan
        	, dstv10.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	dstv10.user.userprofileinfo.balance -= Amount
        	dstv10.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, dstv10.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)


def startime1_view(request):
    form = Startime1Form(request.POST or None)

    if form.is_valid():
        startime1 = form.save(commit=False)
        startime1.user = request.user
        startime1.save()
        # subtracts users withdrawal from balance.
        Amount = 2250
        Plan= str("SMART 1MONTH")
                       
        if startime1.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Startime  {} Package to this IUC 
        	{} .""".format(Plan
        	, startime1.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	startime1.user.userprofileinfo.balance -= Amount
        	startime1.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime {} Package to this IUC {}.'.format(Plan, startime1.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def startime2_view(request):
    form = Startime2Form(request.POST or None)

    if form.is_valid():
        startime2 = form.save(commit=False)
        startime2.user = request.user
        startime2.save()
        # subtracts users withdrawal from balance.
        Amount = 1750
        Plan= str("BASIC 1MONTH")
                       
        if startime2.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Startime  {} Package to this IUC 
        	{} .""".format(Plan
        	, startime2.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	startime2.user.userprofileinfo.balance -= Amount
        	startime1.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime {} Package to this IUC {}.'.format(Plan, startime2.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)



def startime3_view(request):
    form = Startime3Form(request.POST or None)

    if form.is_valid():
        startime3 = form.save(commit=False)
        startime3.user = request.user
        startime3.save()
        # subtracts users withdrawal from balance.
        Amount = 2550
        Plan= str("CLASSIC 1MONTH")
                       
        if startime3.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Startime {} Package to this IUC 
        	{} .""".format(Plan
        	, startime3.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	startime3.user.userprofileinfo.balance -= Amount
        	startime3.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime {} Package to this IUC {}.'.format(Plan, startime3.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def startime4_view(request):
    form = Startime4Form(request.POST or None)

    if form.is_valid():
        startime4 = form.save(commit=False)
        startime4.user = request.user
        startime4.save()
        # subtracts users withdrawal from balance.
        Amount = 950
        Plan= str("Nova 1Month")
                       
        if startime1.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Startime  {} Package to this IUC 
        	{} .""".format(Plan
        	, startime4.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	startime4.user.userprofileinfo.balance -= Amount
        	startime4.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime  {} Package to this IUC {}.'.format(Plan, startime4.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def startime5_view(request):
    form = Startime5Form(request.POST or None)

    if form.is_valid():
        startime5 = form.save(commit=False)
        startime5.user = request.user
        startime5.save()
        # subtracts users withdrawal from balance.
        Amount = 750
        Plan= str("SMART 1WEEK")
                       
        if startime5.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Startime  {} Package to this IUC 
        	{} .""".format(Plan
        	, startime5.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	startime5.user.userprofileinfo.balance -= Amount
        	startime5.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime {} Package to this IUC {}.'.format(Plan, startime5.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def startime6_view(request):
    form = Startime6Form(request.POST or None)

    if form.is_valid():
        startime6 = form.save(commit=False)
        startime6.user = request.user
        startime6.save()
        # subtracts users withdrawal from balance.
        Amount = 650
        Plan= str("BASIC 1WEEK")
                       
        if startime1.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Startime {} Package to this IUC 
        	{} .""".format(Plan
        	, startime6.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	startime6.user.userprofileinfo.balance -= Amount
        	startime6.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime  {} Package to this IUC {}.'.format(Plan, startime6.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

                    
def startime7_view(request):
    form = Startime7Form(request.POST or None)

    if form.is_valid():
        startime7 = form.save(commit=False)
        startime7.user = request.user
        startime7.save()
        # subtracts users withdrawal from balance.
        Amount = 1250
        Plan= str("CLAASIC 1WEEK")
                       
        if startime7.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Startime  {} Package to this IUC 
        	{} .""".format(Plan
        	, startime7.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	startime7.user.userprofileinfo.balance -= Amount
        	startime7.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime {} Package to this IUC {}.'.format(Plan, startime7.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def startime8_view(request):
    form = Startime8Form(request.POST or None)

    if form.is_valid():
        startime8 = form.save(commit=False)
        startime8.user = request.user
        startime8.save()
        # subtracts users withdrawal from balance.
        Amount = 350
        Plan= str("NOVA 1WEEK")
                       
        if startime8.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Startime  {} Package to this IUC 
        	{} .""".format(Plan
        	, startime8.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	startime8.user.userprofileinfo.balance -= Amount
        	startime8.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime {} Package to this IUC {}.'.format(Plan, startime8.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def startime9_view(request):
    form = Startime9Form(request.POST or None)

    if form.is_valid():
        startime9 = form.save(commit=False)
        startime9.user = request.user
        startime9.save()
        # subtracts users withdrawal from balance.
        Amount = 450
        Plan= str("SUPER 1DAY")
                       
        if startime9.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Dstv {} Package to this IUC 
        	{} .""".format(Plan
        	, startime9.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	startime9.user.userprofileinfo.balance -= Amount
        	startime9.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime {} Package to this IUC {}.'.format(Plan, startime9.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def startime10_view(request):
    form = Startime10Form(request.POST or None)

    if form.is_valid():
        startime10 = form.save(commit=False)
        startime10.user = request.user
        startime10.save()
        # subtracts users withdrawal from balance.
        Amount = 250
        Plan= str("SMART 1DAY")
                       
        if startime10.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Startime {} Package to this IUC 
        	{} .""".format(Plan
        	, startime10.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	startime10.user.userprofileinfo.balance -= Amount
        	startime10.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime {} Package to this IUC {}.'.format(Plan, startime10.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def startime11_view(request):
    form = Startime11Form(request.POST or None)

    if form.is_valid():
        startime11 = form.save(commit=False)
        startime11.user = request.user
        startime11.save()
        # subtracts users withdrawal from balance.
        Amount = 200
        Plan= str("BASIC 1DAY")
                       
        if startime11.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Startime  {} Package to this IUC 
        	{} .""".format(Plan
        	, startime11.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	startime11.user.userprofileinfo.balance -= Amount
        	startime1q.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime {} Package to this IUC {}.'.format(Plan, startime11.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def startime12_view(request):
    form = Startime12Form(request.POST or None)

    if form.is_valid():
        startime12 = form.save(commit=False)
        startime12.user = request.user
        startime12.save()
        # subtracts users withdrawal from balance.
        Amount = 370 
        Plan= str("CLASSIC  1DAY")
                       
        if startime12.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Startime {} Package to this IUC 
        	{} .""".format(Plan
        	, startime12.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	startime12.user.userprofileinfo.balance -= Amount
        	startime12.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, startime12.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def startime13_view(request):
    form = Startime13Form(request.POST or None)

    if form.is_valid():
        startime13 = form.save(commit=False)
        startime13.user = request.user
        startime13.save()
        # subtracts users withdrawal from balance.
        Amount = 150
        Plan= str("NOVA 1DAY")
                       
        if startime13.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Startime {} Package to this IUC 
        	{} .""".format(Plan
        	, startime13.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	startime13.user.userprofileinfo.balance -= Amount
        	startime13.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime {} Package to this IUC {}.'.format(Plan, startime13.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

                                    
def gotv1_view(request):
    form = Gotv1Form(request.POST or None)

    if form.is_valid():
        gotv1 = form.save(commit=False)
        gotv1.user = request.user
        gotv1.save()
        # subtracts users withdrawal from balance.
        Amount = 2850
        Plan= str("JOLLI")
                       
        if gotv1.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Gotv {} Package to this IUC 
        	{} .""".format(Plan
        	, gotv1.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	gotv1.user.userprofileinfo.balance -= Amount
        	gotv1.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Gotv {} Package to this IUC {}.'.format(Plan, gotv1.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def gotv2_view(request):
    form = Gotv2Form(request.POST or None)

    if form.is_valid():
        gotv2 = form.save(commit=False)
        gotv2.user = request.user
        gotv2.save()
        # subtracts users withdrawal from balance.
        Amount = 950
        Plan= str("SMALLIE")
                       
        if gotv2.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Gotv {} Package to this IUC 
        	{} .""".format(Plan
        	, gotv2.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	gotv2.user.userprofileinfo.balance -= Amount
        	gotv2.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Gotv {} Package to this IUC {}.'.format(Plan, gotv2.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def gotv3_view(request):
    form = Gotv3Form(request.POST or None)

    if form.is_valid():
        gotv3 = form.save(commit=False)
        gotv3.user = request.user
        gotv3.save()
        # subtracts users withdrawal from balance.
        Amount = 2450
        Plan= str("LITE QUARTERLY")
                       
        if gotv3.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Gotv {} Package to this IUC 
        	{} .""".format(Plan
        	, gotv3.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	gotv3.user.userprofileinfo.balance -= Amount
        	gotv3.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Gotv {} Package to this IUC {}.'.format(Plan, gotv3.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def gotv4_view(request):
    form = Gotv4Form(request.POST or None)

    if form.is_valid():
        gotv4 = form.save(commit=False)
        gotv4.user = request.user
        gotv4.save()
        # subtracts users withdrawal from balance.
        Amount = 7050
        Plan= str("LITE YEARLY")
                       
        if gotv4.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Gotv {} Package to this IUC 
        	{} .""".format(Plan
        	, gotv4.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	gotv4.user.userprofileinfo.balance -= Amount
        	gotv4.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Gotv {} Package to this IUC {}.'.format(Plan, gotv4.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def gotv5_view(request):
    form = Gotv5Form(request.POST or None)

    if form.is_valid():
        gotv5 = form.save(commit=False)
        gotv5.user = request.user
        gotv5.save()
        # subtracts users withdrawal from balance.
        Amount = 4200
        Plan= str("MAX")
                       
        if gotv5.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Gotv {} Package to this IUC 
        	{} .""".format(Plan
        	, gotv5.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	gotv5.user.userprofileinfo.balance -= Amount
        	gotv5.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Gotv {} Package to this IUC {}.'.format(Plan, gotv5.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)
 
def gotv6_view(request):
    form = Gotv6Form(request.POST or None)

    if form.is_valid():
        gotv6 = form.save(commit=False)
        gotv6.user = request.user
        gotv6.save()
        # subtracts users withdrawal from balance.
        Amount = 1950
        Plan= str("JINJA")
                       
        if gotv6.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Gotv {} Package to this IUC 
        	{} .""".format(Plan
        	, gotv6.Smart_Card_Number_or_IUC)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	gotv6.user.userprofileinfo.balance -= Amount
        	gotv6.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Gotv {} Package to this IUC {}.'.format(Plan, gotv6.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)
        
                      
def elect1_view(request):
    form = Elect1Form(request.POST or None)

    if form.is_valid():
        elect1 = form.save(commit=False)
        elect1.user = request.user
        elect1.save()
        # subtracts users withdrawal from balance.
        
        if elect1.user.userprofileinfo.balance < elect1.Amount:
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	#{} Eko Prepaid to this meter number
        	{} .""".format(elect1.Amount
        	, elect1.Meter_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	elect1.user.userprofileinfo.balance -= elect1.Amount
        	elect1.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase #{} Eko Prepaid to this Meter Number {}.'.format(elect1.Amount, elect1.Meter_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def elect2_view(request):
    form = Elect2Form(request.POST or None)

    if form.is_valid():
        elect2 = form.save(commit=False)
        elect2.user = request.user
        elect2.save()
        # subtracts users withdrawal from balance.
        
        if elect2.user.userprofileinfo.balance < elect2.Amount:
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	#{} Ikeja Prepaid to this meter number
        	{} .""".format(elect2.Amount
        	, elect2.Meter_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	elect1.user.userprofileinfo.balance -= elect1.Amount
        	elect1.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase #{} Ikeja Prepaid to this Meter Number {}.'.format(elect2.Amount, elect2.Meter_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)
        
def elect3_view(request):
    form = Elect3Form(request.POST or None)

    if form.is_valid():
        elect3 = form.save(commit=False)
        elect3.user = request.user
        elect3.save()
        # subtracts users withdrawal from balance.
        
        if elect3.user.userprofileinfo.balance < elect3.Amount:
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	#{} Ibadan Prepaid to this meter number
        	{} .""".format(elect3.Amount
        	, elect3.Meter_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	elect3.user.userprofileinfo.balance -= elect1.Amount
        	elect3.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase #{} Eko Prepaid to this Meter Number {}.'.format(elect3.Amount, elect3.Meter_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def elect4_view(request):
    form = Elect4Form(request.POST or None)

    if form.is_valid():
        elect4 = form.save(commit=False)
        elect4.user = request.user
        elect4.save()
        # subtracts users withdrawal from balance.
        
        if elect4.user.userprofileinfo.balance < elect4.Amount:
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	#{} Enugu Prepaid to this meter number
        	{} .""".format(elect4.Amount
        	, elect4.Meter_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	elect4.user.userprofileinfo.balance -= elect4.Amount
        	elect4.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase #{} Enugu Prepaid to this Meter Number {}.'.format(elect4.Amount, elect4.Meter_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def elect5_view(request):
    form = Elect5Form(request.POST or None)

    if form.is_valid():
        elect5 = form.save(commit=False)
        elect5.user = request.user
        elect5.save()
        # subtracts users withdrawal from balance.
        
        if elect5.user.userprofileinfo.balance < elect5.Amount:
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	#{} Eko Postpaid to this meter number
        	{} .""".format(elect5.Amount
        	, elect5.Meter_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	elect5.user.userprofileinfo.balance -= elect1.Amount
        	elect5.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase #{} Eko Postpaid to this Meter Number {}.'.format(elect5.Amount, elect5.Meter_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def elect6_view(request):
    form = Elect6Form(request.POST or None)

    if form.is_valid():
        elect6 = form.save(commit=False)
        elect6.user = request.user
        elect6.save()
        # subtracts users withdrawal from balance.
        
        if elect6.user.userprofileinfo.balance < elect6.Amount:
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	#{} Ibadan Postpaid to this meter number
        	{} .""".format(elect6.Amount
        	, elect6.Meter_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	elect6.user.userprofileinfo.balance -= elect6.Amount
        	elect6.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase #{} Ibadan Postpaid to this Meter Number {}.'.format(elect6.Amount, elect6.Meter_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def elect7_view(request):
    form = Elect7Form(request.POST or None)

    if form.is_valid():
        elect7 = form.save(commit=False)
        elect7.user = request.user
        elect7.save()
        # subtracts users withdrawal from balance.
        
        if elect7.user.userprofileinfo.balance < elect7.Amount:
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	#{} Ikeja Postpaid to this meter number
        	{} .""".format(elect7.Amount
        	, elect7.Meter_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	elect7.user.userprofileinfo.balance -= elect1.Amount
        	elect7.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase #{} Ikeja Postpaid to this Meter Number {}.'.format(elect7.Amount, elect7.Meter_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def elect8_view(request):
    form = Elect8Form(request.POST or None)

    if form.is_valid():
        elect8 = form.save(commit=False)
        elect8.user = request.user
        elect8.save()
        # subtracts users withdrawal from balance.
        
        if elect8.user.userprofileinfo.balance < elect1.Amount:
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	#{} Enugu Postpaid to this meter number
        	{} .""".format(elect8.Amount
        	, elect8.Meter_Number)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	elect8.user.userprofileinfo.balance -= elect8.Amount
        	elect8.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase #{} Enugu Postpaid to this Meter Number {}.'.format(elect8.Amount, elect8.Meter_Number)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)


def waec_view(request):
    form = WaecForm(request.POST or None)

    if form.is_valid():
        waec = form.save(commit=False)
        waec.user = request.user
        waec.save()
        # subtracts users withdrawal from balance.
        Amount = 2000
        
        if waec.user.userprofileinfo.balance < Amount:
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Waec Pin to this  Email
        	{} .""".format(
        	waec.Email)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	waec.user.userprofileinfo.balance -= Amount
        	waec.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Waec Pin to this Email {}.'.format(waec.Email)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

def neco_view(request):
    form = NecoForm(request.POST or None)

    if form.is_valid():
        neco = form.save(commit=False)
        neco.user = request.user
        neco.save()
        # subtracts users withdrawal from balance.
        Amount = 1000
        
        if neco.user.userprofileinfo.balance < Amount:
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        	sender_email = "blesfem7@gmail.com"
        	receiver_email = "sampepper.tech@gmail.com"
        	message = """\
        	From: "blesfem7@gmail.com"    
        	To: "sampepper.tech@gmail.com"
        	Subject: Hello Sampepper!
        	You have a new order to purchase
        	Neco Pin to this  Email
        	{} .""".format(
        	neco.Email)
        	port = 465  
        	context = ssl.create_default_context()
        	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        		server.login("blesfem7@gmail.com", 'BlesfemSw00rd')
        		server.sendmail(sender_email, receiver_email, message)
		
        	#email()
        	neco.user.userprofileinfo.balance -= Amount
        	neco.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Neco Pin to this Email {}.'.format(neco.Email)
        )
                
        	return redirect("index")

    context = {
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

							