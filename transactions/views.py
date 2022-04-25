from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Withdrawal, MTN_AIRTIME,GLO_AIRTIME,AIRTEL_AIRTIME,MTN_AWUF_AIRTIME,MTN_SHARE_AIRTIME,MTN_500MB_SME,MTN_2GB_SME,MTN_1GB_SME,MTN_3GB_SME,MTN_4GB_SME,MTN_5GB_SME,MTN_10GB_SME,MTN_1GB_WD,MTN_1P5GB_MD,MTN_2GB_MD,MTN_20GB_WD,GLO_50MB,GLO_150MB,GLO_350MB,GLO_2P9GB,GLO_4P1GB,GLO_5P8GB,GLO_7P7GB,GLO_13P75GB,GLO_18P25GB,AIRTEL_750MB,AIRTEL_1GB,AIRTEL_2GB,AIRTEL_3GB,AIRTEL_6GB,AIRTEL_10GB,AIRTEL_20GB,DSTV_PADI,DSTV_XTRAVIEW,DSTV_ASIAN_ADDON,DSTV_FRENCH_BOUGUET,DSTV_COMPACT_PLUS_F,DSTV_CONFAM,DSTV_YANGA, DSTV_PREMIUM,DSTV_COMPACT_PLUS,DSTV_COMPACT_PLUS_ASIAN_ADDON,GOTV_JOLLI,GOTV_SMALLIE,GOTV_LITE_QUART,GOTV_LITE_YEAR, GOTV_MAX,GOTV_JINJA,STARTIME_SMART_M,STARTIME_BASIC_M,STARTIME_CLASSIC_M,STARTIME_NOVA_M,STARTIME_SMART_W,STARTIME_BASIC_W,STARTIME_CLASSIC_W,STARTIME_NOVA_W,STARTIME_SMART_D,STARTIME_NOVA_D,STARTIME_BASIC_D,STARTIME_CLASSIC_D,ELECT_EKO_PRE,ELECT_IKEJA_PRE,ELECT_IBADAN_PRE,ELECT_ENUGU_PRE,ELECT_IKEJA_POST, ELECT_IBADAN_POST,ELECT_EKO_POST,ELECT_ENUGU_POST,WAEC,NECO

from transactions.models import MTN,GLO,AIRTEL,DSTV,DSTV,GOTV,STARTIMES,ELECTRICITY,EXAM
from mycompany.models import UserProfileInfo, User
from .forms import  WithdrawalForm, Airtime1Form,Airtime2Form,Airtime4Form,Airtime5Form,Airtime6Form,Mtn1Form,Mtn1Form,Mtn2Form,Mtn3Form,Mtn4Form,Mtn5Form,Mtn6Form,Mtn7Form,Mtn8Form,Mtn9Form,Mtn10Form,Mtn11Form,Glo1Form,Glo1Form,Glo2Form,Glo3Form,Glo4Form,Glo5Form,Glo6Form,Glo7Form,Glo8Form,Glo9Form,Airtel1Form,Airtel2Form,Airtel3Form,Airtel4Form,Airtel5Form,Airtel6Form,Airtel7Form,Dstv1Form,Dstv2Form,Dstv3Form,Dstv4Form,Dstv5Form,Dstv6Form,Dstv7Form,Dstv8Form,Dstv9Form,Dstv10Form,Startime1Form,Startime2Form,Startime3Form,Startime4Form,Startime5Form,Startime6Form,Startime7Form,Startime8Form,Startime9Form,Startime9Form,Startime10Form,Startime11Form,Startime12Form,Elect1Form,Elect2Form,Elect3Form,Elect4Form,Elect5Form,Elect6Form,Elect7Form,Elect8Form,Gotv1Form,Gotv2Form,Gotv3Form,Gotv4Form,Gotv5Form,Gotv6Form,WaecForm,NecoForm




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


class order1_view(TemplateView):
    template_name = 'transactions/order1.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mtns = MTN.objects.all()
        glos = GLO.objects.all()
        airtels = AIRTEL.objects.all()
        dstvs = DSTV.objects.all()
        gotvs = GOTV.objects.all()
        exams = EXAM.objects.all()
        startimes = STARTIMES.objects.all()
        mtnairtimes = MTN_AIRTIME.objects.all()
        gloairtimes = GLO_AIRTIME.objects.all()
        airtelairtimes = AIRTEL_AIRTIME.objects.all()
        mtnawufairtimes = MTN_AWUF_AIRTIME.objects.all()
        mtnshareairtimes = MTN_SHARE_AIRTIME.objects.all()
        mtn1s = MTN_500MB_SME.objects.all()
        mtn2s = MTN_2GB_SME.objects.all()
        mtn3s = MTN_1GB_SME.objects.all()
        mtn4s = MTN_3GB_SME.objects.all()
        mtn5s  = MTN_4GB_SME.objects.all()
        mtn6s = MTN_5GB_SME.objects.all()
        mtn7s = MTN_10GB_SME.objects.all()
        mtn8s  = MTN_1GB_WD.objects.all()
        mtn9s = MTN_1P5GB_MD.objects.all()
        mtn10s  = MTN_2GB_MD.objects.all()
        mtn11s = MTN_20GB_WD.objects.all()
        glo1s = GLO_50MB.objects.all()
        glo2s  = GLO_150MB.objects.all()
        glo3s  = GLO_350MB.objects.all()
        glo4s  = GLO_2P9GB.objects.all()
        glo5s  = GLO_4P1GB.objects.all()
        glo6s = GLO_5P8GB.objects.all()
        glo7s = GLO_7P7GB.objects.all()
        glo8s  = GLO_13P75GB.objects.all()
        glo9s  = GLO_18P25GB.objects.all()
        airtel1s  = AIRTEL_750MB.objects.all()
        airtel2s = AIRTEL_1GB.objects.all()
        airtel3s = AIRTEL_2GB.objects.all()
        airtel4s = AIRTEL_3GB.objects.all()
        airtel5s  = AIRTEL_6GB.objects.all()
        airtel6s = AIRTEL_10GB.objects.all()
        airtel7s = AIRTEL_20GB.objects.all()
        dstv1s = DSTV_PADI.objects.all()
        dstv2s = DSTV_XTRAVIEW.objects.all()
        dstv3s = DSTV_ASIAN_ADDON.objects.all()
        dstv4s = DSTV_FRENCH_BOUGUET.objects.all()
        dstv5s = DSTV_COMPACT_PLUS_F.objects.all()
        dstv6s = DSTV_CONFAM.objects.all()
        dstv7s = DSTV_YANGA.objects.all()
        dstv8s = DSTV_PREMIUM.objects.all()
        dstv9s = DSTV_COMPACT_PLUS.objects.all()
        dstv10s = DSTV_COMPACT_PLUS_ASIAN_ADDON.objects.all()
        gotv1s = GOTV_JOLLI.objects.all()
        gotv2s = GOTV_SMALLIE.objects.all()
        gotv3s = GOTV_LITE_QUART.objects.all()
        gotv4s = GOTV_LITE_YEAR.objects.all()
        gotv5s = GOTV_MAX.objects.all()
        gotv6s = GOTV_JINJA.objects.all()
        start1s = STARTIME_SMART_M.objects.all()
        start2s = STARTIME_BASIC_M.objects.all()
        start3s = STARTIME_CLASSIC_M.objects.all()
        start4s = STARTIME_NOVA_M.objects.all()
        start5s = STARTIME_SMART_W.objects.all()
        start6s = STARTIME_BASIC_W.objects.all()
        start7s = STARTIME_CLASSIC_W.objects.all()
        start8s  = STARTIME_NOVA_W.objects.all()
        start9s = STARTIME_SMART_D.objects.all()
        start10s = STARTIME_NOVA_D.objects.all()
        start11s = STARTIME_BASIC_D.objects.all()
        start12s = STARTIME_CLASSIC_D.objects.all()
        elect1s = ELECT_EKO_PRE.objects.all()
        elect2s = ELECT_IKEJA_PRE.objects.all()
        elect3s = ELECT_IBADAN_PRE.objects.all()
        elect4s  = ELECT_ENUGU_PRE.objects.all()
        elect5s = ELECT_IKEJA_POST.objects.all()
        elect6s = ELECT_IBADAN_POST.objects.all()
        elect7s = ELECT_EKO_POST.objects.all()
        elect8s = ELECT_ENUGU_POST.objects.all()
        waecs = WAEC.objects.all()
        necos = NECO.objects.all()   
    
        context['mtns'] = mtns
        context['glos'] = glos
        context['airtels'] = airtels
        context['startimes'] = startimes
        context['dstvs'] = dstvs
        context['gotvs'] = gotvs
        context['exams'] = exams  
        context['necos'] = necos
        context['waecs'] = waecs
        context['elect1s'] = elect1s
        context['elect2s'] = elect2s
        context['elect3s'] = elect3s
        context['elect4s'] = elect4s
        context['elect5s'] = elect5s
        context['elect6s'] = elect6s  
        context['elect7s'] = elect7s
        context['elect8s'] = elect8s
        context['start1s'] = start1s
        context['start2s'] = start2s
        context['start3s'] = start3s
        context['start4s'] = start4s
        context['start5s'] = start5s
        context['start6s'] = start6s
        context['start7s'] = start7s  
        context['start8s'] = start8s
        context['start9s'] = start9s
        context['start10s'] = start10s
        context['start11s'] = start11s
        context['start12s'] = start12s
        context['gotv1s'] = gotv1s
        context['gotv2s'] = gotv2s
        context['gotv3s'] = gotv3s
        context['gotv4s'] = gotv4s  
        context['gotv5s'] = gotv5s
        context['gotv6s'] = gotv6s
        context['dstv1s'] = dstv1s
        context['dstv2s'] = dstv2s
        context['dstv3s'] = dstv3s
        context['dstv4s'] = dstv4s
        context['dstv5s'] = dstv5s
        context['dstv6s'] = dstv6s
        context['dstv7s'] = dstv7s  
        context['dstv8s'] = dstv8s
        context['dstv9s'] = dstv9s
        context['dstv10s'] = dstv10s
        context['mtn1s'] = mtn1s
        context['mtn2s'] = mtn2s
        context['mtn3s'] = mtn3s
        context['mtn4s'] = mtn4s
        context['mtn5s'] = mtn5s
        context['mtn6s'] = mtn6s  
        context['mtn7s'] = mtn7s
        context['mtn8s'] = mtn8s
        context['mtn9s'] = mtn9s
        context['mtn10s'] = mtn10s
        context['mtn11s'] = mtn11s
        context['glo1s'] = glo1s
        context['glo2s'] = glo2s
        context['glo3s'] = glo3s
        context['glo4s'] = glo4s  
        context['glo5s'] = glo5s
        context['glo6s'] = glo6s
        context['glo7s'] = glo7s
        context['glo8s'] = glo8s
        context['glo9s'] = glo9s
        context['airtel1s'] = airtel1s
        context['airtel2s'] = airtel2s
        context['airtel3s'] = airtel3s
        context['airtel4s'] = airtel4s  
        context['airtel5s'] = airtel5s
        context['airtel6s'] = airtel6s
        context['airtel7s'] = airtel7s
        context['mtnairtimes'] = mtnairtimes
        context['gloairtimes'] = gloairtimes
        context['airtelairtimes'] = airtelairtimes
        context['mtnawufairtimes'] = mtnawufairtimes
        context['mtnshareairtimes'] = mtnshareairtimes
                    
        return context
   

    
class order2_view(TemplateView):
    template_name = 'transactions/order2.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        mtn1s = MTN_500MB_SME.objects.all()
        mtn2s = MTN_2GB_SME.objects.all()
        mtn3s = MTN_1GB_SME.objects.all()
        mtn4s = MTN_3GB_SME.objects.all()
        mtn5s  = MTN_4GB_SME.objects.all()
        mtn6s = MTN_5GB_SME.objects.all()
        mtn7s = MTN_10GB_SME.objects.all()
        mtn8s  = MTN_1GB_WD.objects.all()
        mtn9s = MTN_1P5GB_MD.objects.all()
        mtn10s  = MTN_2GB_MD.objects.all()
        mtn11s = MTN_2GB_MD.objects.all()
        
        context['mtn1s'] = mtn1s
        context['mtn2s'] = mtn2s
        context['mtn3s'] = mtn3s
        context['mtn4s'] = mtn4s
        context['mtn5s'] = mtn5s
        context['mtn6s'] = mtn6s  
        context['mtn7s'] = mtn7s
        context['mtn8s'] = mtn8s
        context['mtn9s'] = mtn9s
        context['mtn10s'] = mtn10s
        context['mtn11s'] = mtn11s
       
        return context

class deposit_view(TemplateView):
    template_name = 'transactions/deposit.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        mtn1s = MTN_500MB_SME.objects.all()
        mtn2s = MTN_2GB_SME.objects.all()
        mtn3s = MTN_1GB_SME.objects.all()
        mtn4s = MTN_3GB_SME.objects.all()
        mtn5s  = MTN_4GB_SME.objects.all()
        mtn6s = MTN_5GB_SME.objects.all()
        mtn7s = MTN_10GB_SME.objects.all()
        mtn8s  = MTN_1GB_WD.objects.all()
        mtn9s = MTN_1P5GB_MD.objects.all()
        mtn10s  = MTN_2GB_MD.objects.all()
        mtn11s = MTN_2GB_MD.objects.all()
        
        context['mtn1s'] = mtn1s
        context['mtn2s'] = mtn2s
        context['mtn3s'] = mtn3s
        context['mtn4s'] = mtn4s
        context['mtn5s'] = mtn5s
        context['mtn6s'] = mtn6s  
        context['mtn7s'] = mtn7s
        context['mtn8s'] = mtn8s
        context['mtn9s'] = mtn9s
        context['mtn10s'] = mtn10s
        context['mtn11s'] = mtn11s
       
        return context




class order3_view(TemplateView):
    template_name = 'transactions/order3.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        glo1s = GLO_50MB.objects.all()
        glo2s  = GLO_150MB.objects.all()
        glo3s  = GLO_350MB.objects.all()
        glo4s  = GLO_2P9GB.objects.all()
        glo5s  = GLO_4P1GB.objects.all()
        glo6s = GLO_5P8GB.objects.all()
        glo7s = GLO_7P7GB.objects.all()
        glo8s  = GLO_13P75GB.objects.all()
        glo9s  = GLO_18P25GB.objects.all()
        
        context['glo1s'] = glo1s
        context['glo2s'] = glo2s
        context['glo3s'] = glo3s
        context['glo4s'] = glo4s  
        context['glo5s'] = glo5s
        context['glo6s'] = glo6s
        context['glo7s'] = glo7s
        context['glo8s'] = glo8s
        context['glo9s'] = glo9s
                          
        return context



class order4_view(TemplateView):
    template_name = 'transactions/order4.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        airtel2s = AIRTEL_750MB.objects.all()
        airtel2s = AIRTEL_1GB.objects.all()
        airtel3s = AIRTEL_2GB.objects.all()
        airtel4s = AIRTEL_3GB.objects.all()
        airtel5s  = AIRTEL_6GB.objects.all()
        airtel6s = AIRTEL_10GB.objects.all()
        airtel7s = AIRTEL_20GB.objects.all()
        
        context['airtel1s'] = airtel1s
        context['airtel2s'] = airtel2s
        context['airtel3s'] = airtel3s
        context['airtel4s'] = airtel4s  
        context['airtel5s'] = airtel5s
        context['airtel6s'] = airtel6s
        context['airtel7s'] = airtel7s
   
          
        return context



class order5_view(TemplateView):
    template_name = 'transactions/order5.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        dstv1s = DSTV_PADI.objects.all()
        dstv2s = DSTV_XTRAVIEW.objects.all()
        dstv3s = DSTV_ASIAN_ADDON.objects.all()
        dstv4s = DSTV_FRENCH_BOUGUET.objects.all()
        dstv5s = DSTV_COMPACT_PLUS_F.objects.all()
        dstv6s = DSTV_CONFAM.objects.all()
        dstv7s = DSTV_YANGA.objects.all()
        dstv8s = DSTV_PREMIUM.objects.all()
        dstv9s = DSTV_COMPACT_PLUS.objects.all()
        dstv10s = DSTV_COMPACT_PLUS_ASIAN_ADDON.objects.all()
        
        context['dstv1s'] = dstv1s
        context['dstv2s'] = dstv2s
        context['dstv3s'] = dstv3s
        context['dstv4s'] = dstv4s
        context['dstv5s'] = dstv5s
        context['dstv6s'] = dstv6s
        context['dstv7s'] = dstv7s  
        context['dstv8s'] = dstv8s
        context['dstv9s'] = dstv9s
        context['dstv10s'] = dstv10s
                           
        return context



class order6_view(TemplateView):
    template_name = 'transactions/order6.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        gotv1s = GOTV_JOLLI.objects.all()
        gotv2s = GOTV_SMALLIE.objects.all()
        gotv3s = GOTV_LITE_QUART.objects.all()
        gotv4s = GOTV_LITE_YEAR.objects.all()
        gotv5s = GOTV_MAX.objects.all()
        gotv6s = GOTV_JINJA.objects.all()
        
        context['gotv1s'] = gotv1s
        context['gotv2s'] = gotv2s
        context['gotv3s'] = gotv3s
        context['gotv4s'] = gotv4s  
        context['gotv5s'] = gotv5s
        context['gotv6s'] = gotv6s
                       
        return context



class order7_view(TemplateView):
    template_name = 'transactions/order1.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        start1s = STARTIME_SMART_M.objects.all()
        start2s = STARTIME_BASIC_M.objects.all()
        start3s = STARTIME_CLASSIC_M.objects.all()
        start4s = STARTIME_NOVA_M.objects.all()
        start5s = STARTIME_SMART_W.objects.all()
        start6s = STARTIME_BASIC_W.objects.all()
        start7s = STARTIME_CLASSIC_W.objects.all()
        start8s  = STARTIME_NOVA_W.objects.all()
        start9s = STARTIME_SMART_D.objects.all()
        start10s = STARTIME_NOVA_D.objects.all()
        start11s = STARTIME_BASIC_D.objects.all()
        start12s = STARTIME_CLASSIC_D.objects.all()
        
        context['start1s'] = start1s
        context['start2s'] = start2s
        context['start3s'] = start3s
        context['start4s'] = start4s
        context['start5s'] = start5s
        context['start6s'] = start6s
        context['start7s'] = start7s  
        context['start8s'] = start8s
        context['start9s'] = start9s
        context['start10s'] = start10s
        context['start11s'] = start11s
        context['start12s'] = start12s


                   
        return context



class order8_view(TemplateView):
    template_name = 'transactions/order8.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        elect1s = ELECT_EKO_PRE.objects.all()
        elect2s = ELECT_IKEJA_PRE.objects.all()
        elect3s = ELECT_IBADAN_PRE.objects.all()
        elect4s  = ELECT_ENUGU_PRE.objects.all()
        elect5s = ELECT_IKEJA_POST.objects.all()
        elect6s = ELECT_IBADAN_POST.objects.all()
        elect7s = ELECT_EKO_POST.objects.all()
        elect8s = ELECT_ENUGU_POST.objects.all()
        
        context['elect1s'] = elect1s
        context['elect2s'] = elect2s
        context['elect3s'] = elect3s
        context['elect4s'] = elect4s
        context['elect5s'] = elect5s
        context['elect6s'] = elect6s  
        context['elect7s'] = elect7s
        context['elect8s'] = elect8s
                                            
        return context



class order9_view(TemplateView):
    template_name = 'transactions/order9.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        waecs = WAEC.objects.all()
        necos = NECO.objects.all()
        
        context['necos'] = necos
        context['waecs'] = waecs
                         
        return context


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
       
        	#email()
        	mtn1.user.userprofileinfo.balance -= Amount
        	mtn1.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Mtn SME Data to this number {}.'.format(Plan, mtn1.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "MTN 500MB SME DATA",
        "cost": "NGN 160",
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
        			
        	#email()
        	mtn2.user.userprofileinfo.balance -= Amount
        	mtn2.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Mtn SME Data to this number {}.'.format(Plan, mtn1.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "MTN 1GB SME DATA",
        "cost": "NGN 260",
    
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
        	        	#email()
        	mtn3.user.userprofileinfo.balance -= Amount
        	mtn3.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Mtn SME Data to this number {}.'.format(Plan, mtn1.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "MTN 2GB SME DATA",
        "cost": "NGN 520",
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
        		
        	#email()
        	mtn4.user.userprofileinfo.balance -= Amount
        	mtn4.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Mtn SME Data to this number {}.'.format(Plan, mtn4.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "MTN 3GB SME DATA",
        "cost": "NGN 780",
    
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
        
        	#email()
        	mtn5.user.userprofileinfo.balance -= Amount
        	mtn5.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Mtn SME Data to this number {}.'.format(Plan, mtn5.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "MTN 4GB SME DATA",
        "cost": "NGN 1040",    
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
        			
        	#email()
        	mtn6.user.userprofileinfo.balance -= Amount
        	mtn6.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Mtn SME Data to this number {}.'.format(Plan, mtn6.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "MTN 5GB SME DATA",
        "cost": "NGN 1300",    
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
        	
        	#email()
        	mtn7.user.userprofileinfo.balance -= Amount
        	mtn7.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Mtn SME Data to this number {}.'.format(Plan, mtn7.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "MTN 10GB SME DATA",
        "cost": "NGN 2600",
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
        
        	#email()
        	mtn8.user.userprofileinfo.balance -= Amount
        	mtn8.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Mtn SME Data to this number {}.'.format(Plan, mtn8.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "MTN 1GB WEEKLY DATA",
        "cost": "NGN 800",    
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
        	
        	#email()
        	mtn9.user.userprofileinfo.balance -= Amount
        	mtn9.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Mtn SME Data to this number {}.'.format(Plan, mtn9.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "MTN 2GB 30DAYS DIRECT DATA",
        "cost": "NGN 1160",
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
        	
        	#email()
        	mtn10.user.userprofileinfo.balance -= Amount
        	mtn10.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Mtn SME Data to this number {}.'.format(Plan, mtn10.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "MTN 10GB WEEKLY DIRECT DATA",
        "cost": "NGN 10000",
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
        	
        	#email()
        	glo1.user.userprofileinfo.balance -= Amount
        	glo1.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Glo SME Data to this number {}.'.format(Plan, glo1.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Glo 50MB  DATA",
        "cost": "NGN 50",
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
        
        	#email()
        	glo2.user.userprofileinfo.balance -= Amount
        	glo2.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Glo SME Data to this number {}.'.format(Plan, glo2.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Glo 150MB  DATA",
        "cost": "NGN 100",
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
        
        	#email()
        	glo3.user.userprofileinfo.balance -= Amount
        	glo3.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Glo SME Data to this number {}.'.format(Plan, glo3.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Glo 350MB  DATA",
        "cost": "NGN 200",     
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
        
        	#email()
        	glo4.user.userprofileinfo.balance -= Amount
        	glo4.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Glo SME Data to this number {}.'.format(Plan, glo4.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Glo 2.9GB  DATA",
        "cost": "NGN 1000",
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
        		
        	#email()
        	glo5.user.userprofileinfo.balance -= Amount
        	glo5.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Glo SME Data to this number {}.'.format(Plan, glo5.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Glo 4.1GB  DATA",
        "cost": "NGN 1450",
     
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
        
        	#email()
        	glo6.user.userprofileinfo.balance -= Amount
        	glo6.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Glo SME Data to this number {}.'.format(Plan, glo6.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Glo 5.8GB  DATA",
        "cost": "NGN 1950",
     
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
        
        	#email()
        	glo7.user.userprofileinfo.balance -= Amount
        	glo7.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Glo SME Data to this number {}.'.format(Plan, glo7.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Glo 7.7GB  DATA",
        "cost": "NGN 2400",     
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
        		
        	#email()
        	glo8.user.userprofileinfo.balance -= Amount
        	glo8.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Glo SME Data to this number {}.'.format(Plan, glo8.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Glo 10GB  DATA",
        "cost": "NGN 2900",
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
        
        	#email()
        	glo9.user.userprofileinfo.balance -= Amount
        	glo9.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Glo SME Data to this number {}.'.format(Plan, glo9.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Glo 13.29GB  DATA",
        "cost": "NGN 3850",     
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
        
        	#email()
        	glo10.user.userprofileinfo.balance -= Amount
        	glo10.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Glo SME Data to this number {}.'.format(Plan, glo10.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Glo 18.25GB  DATA",
        "cost": "NGN 5000",     
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
        		
        	#email()
        	airtel1.user.userprofileinfo.balance -= Amount
        	airtel1.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Airtel SME Data to this number {}.'.format(Plan, airtel1.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Airtel 750MB  DATA",
        "cost": "NGN 500",
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
        
        	#email()
        	airtel2.user.userprofileinfo.balance -= Amount
        	airtel2.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Airtel SME Data to this number {}.'.format(Plan, airtel2.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
       "table": "Airtel 2GB  DATA",
        "cost": "NGN 1180",
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
        		
        	#email()
        	airtel3.user.userprofileinfo.balance -= Amount
        	airtel3.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Airtel SME Data to this number {}.'.format(Plan, airtel3.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
       "table": "Airtel 3GB  DATA",
        "cost": "NGN 1480",
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
        		
        	#email()
        	airtel4.user.userprofileinfo.balance -= Amount
        	airtel4.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Airtel SME Data to this number {}.'.format(Plan, airtel4.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Airtel 4GB  DATA",
        "cost": "NGN 1950",
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
        
        	#email()
        	airtel5.user.userprofileinfo.balance -= Amount
        	airtel5.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Airtel SME Data to this number {}.'.format(Plan, airtel5.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Airtel 6GB  DATA",
        "cost": "NGN 2450",
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
        
        	#email()
        	airtel6.user.userprofileinfo.balance -= Amount
        	airtel6.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Airtel SME Data to this number {}.'.format(Plan, airtel6.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Airtel 10GB  DATA",
        "cost": "NGN 2950",
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
        		
        	#email()
        	airtel7.user.userprofileinfo.balance -= Amount
        	airtel7.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Airtel SME Data to this number {}.'.format(Plan, airtel7.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Airtel 20GB  DATA",
        "cost": "NGN 5800",
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
        		#email()
        	airtel8.user.userprofileinfo.balance -= Amount
        	airtel8.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase {} Airtel SME Data to this number {}.'.format(Plan, airtel8.Mobile_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Airtel 40B  DATA",
        "cost": "NGN 11000",  
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
        	
        	#email()
        	dstv1.user.userprofileinfo.balance -= Amount
        	dstv1.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, dstv1.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Dstv PADI",
        "cost": "NGN 2200",
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
        		
        	#email()
        	dstv2.user.userprofileinfo.balance -= Amount
        	dstv2.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, dstv2.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Dstv XTRAVIEW",
        "cost": "NGN 2950",
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
        
        	#email()
        	dstv3.user.userprofileinfo.balance -= Amount
        	dstv3.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, dstv3.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Dstv ASIAN ADD ON",
        "cost": "NGN 7150",
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
        	
        	#email()
        	dstv4.user.userprofileinfo.balance -= Amount
        	dstv4.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, dstv4.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
       "table": "Dstv FRENCH BOUGUET",
        "cost": "NGN 4150",
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
        	
        	#email()
        	dstv5.user.userprofileinfo.balance -= Amount
        	dstv5.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, dstv5.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Dstv COMPACT PLUS FRENCH",
        "cost": "NGN 11700",
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
        	
        	#email()
        	dstv6.user.userprofileinfo.balance -= Amount
        	dstv6.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, dstv6.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Dstv CONFAM",
        "cost": "NGN 5350",
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
        		#email()
        	dstv7.user.userprofileinfo.balance -= Amount
        	dstv7.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, dstv7.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Dstv YANGA",
        "cost": "NGN 3000",
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
        	
        	#email()
        	dstv8.user.userprofileinfo.balance -= Amount
        	dstv8.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, dstv8.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Dstv PREMIUM",
        "cost": "NGN 21050",
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
        	
		
        	#email()
        	dstv9.user.userprofileinfo.balance -= Amount
        	dstv9.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, dstv9.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Dstv COMPACT PLUS",
        "cost": "NGN 14300",
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
        	
        	#email()
        	dstv10.user.userprofileinfo.balance -= Amount
        	dstv10.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, dstv10.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Dstv COMPACT PLUS ASIAN ADD ON",
        "cost": "NGN 7150",
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
        
        	#email()
        	startime1.user.userprofileinfo.balance -= Amount
        	startime1.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime {} Package to this IUC {}.'.format(Plan, startime1.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Startime SMART 1MONTH",
        "cost": "NGN 2250",
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
        	
        	#email()
        	startime2.user.userprofileinfo.balance -= Amount
        	startime1.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime {} Package to this IUC {}.'.format(Plan, startime2.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Startime BASIC 1MONTH",
        "cost": "NGN 1750",
     
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
        		
        	#email()
        	startime3.user.userprofileinfo.balance -= Amount
        	startime3.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime {} Package to this IUC {}.'.format(Plan, startime3.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Startime CLASSIC 1MONTH",
        "cost": "NGN 2550",
     
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
        	        	#email()
        	startime4.user.userprofileinfo.balance -= Amount
        	startime4.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime  {} Package to this IUC {}.'.format(Plan, startime4.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Startime NOVA 1MONTH",
        "cost": "NGN 950",
     
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
        			
        	#email()
        	startime5.user.userprofileinfo.balance -= Amount
        	startime5.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime {} Package to this IUC {}.'.format(Plan, startime5.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Startime SMART 1WEEK",
        "cost": "NGN 750",
     
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
        	
		
        	#email()
        	startime6.user.userprofileinfo.balance -= Amount
        	startime6.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime  {} Package to this IUC {}.'.format(Plan, startime6.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Startime BASIC 1WEEK",
        "cost": "NGN 650",
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
        Plan= str("CLASSIC 1WEEK")
                       
        if startime7.user.userprofileinfo.                 	        balance < Amount :
            messages.success(
            request, 'Your account balance is too low, please deposit or top up your account! '
        )
        else:
        
        	#email()
        	startime7.user.userprofileinfo.balance -= Amount
        	startime7.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime {} Package to this IUC {}.'.format(Plan, startime7.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Startime CLASSIC 1WEEK",
        "cost": "NGN 1250",
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
        
        	#email()
        	startime8.user.userprofileinfo.balance -= Amount
        	startime8.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime {} Package to this IUC {}.'.format(Plan, startime8.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Startime NOVA 1WEEK",
        "cost": "NGN 350",
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
        	
        	#email()
        	startime9.user.userprofileinfo.balance -= Amount
        	startime9.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime {} Package to this IUC {}.'.format(Plan, startime9.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Startime SUPER 1DAY",
        "cost": "NGN 450",
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
        	
        	#email()
        	startime10.user.userprofileinfo.balance -= Amount
        	startime10.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime {} Package to this IUC {}.'.format(Plan, startime10.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
         "table": "Startime SMART 1DAY",
        "cost": "NGN 250",
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
        	
        	#email()
        	startime11.user.userprofileinfo.balance -= Amount
        	startime1q.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime {} Package to this IUC {}.'.format(Plan, startime11.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Startime BASIC 1DAY",
        "cost": "NGN 200",
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
        		
        	#email()
        	startime12.user.userprofileinfo.balance -= Amount
        	startime12.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Dstv {} Package to this IUC {}.'.format(Plan, startime12.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Startime CLASSIC 1DAY",
        "cost": "NGN 370",
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
        	
        	#email()
        	startime13.user.userprofileinfo.balance -= Amount
        	startime13.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Startime {} Package to this IUC {}.'.format(Plan, startime13.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Startime NOVA 1DAY",
        "cost": "NGN 150",
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
        
        	#email()
        	gotv1.user.userprofileinfo.balance -= Amount
        	gotv1.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Gotv {} Package to this IUC {}.'.format(Plan, gotv1.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Gotv JOLLI",
        "cost": "NGN 2850",
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
        	
        	#email()
        	gotv2.user.userprofileinfo.balance -= Amount
        	gotv2.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Gotv {} Package to this IUC {}.'.format(Plan, gotv2.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Gotv SMALLIE",
        "cost": "NGN 950",
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
        
        	#email()
        	gotv3.user.userprofileinfo.balance -= Amount
        	gotv3.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Gotv {} Package to this IUC {}.'.format(Plan, gotv3.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Gotv LITE QUARTERLY",
        "cost": "NGN 2450",
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
        		
        	#email()
        	gotv4.user.userprofileinfo.balance -= Amount
        	gotv4.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Gotv {} Package to this IUC {}.'.format(Plan, gotv4.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Gotv LITE YEARLY",
        "cost": "NGN 7050",
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
        
        	#email()
        	gotv5.user.userprofileinfo.balance -= Amount
        	gotv5.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Gotv {} Package to this IUC {}.'.format(Plan, gotv5.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Gotv MAX",
        "cost": "NGN 4200",
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
        		
        	#email()
        	gotv6.user.userprofileinfo.balance -= Amount
        	gotv6.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Gotv {} Package to this IUC {}.'.format(Plan, gotv6.Smart_Card_Number_or_IUC)
        )
                
        	return redirect("index")

    context = {
        "table": "Gotv JINJA",
        "cost": "NGN 1950",
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
        
        	#email()
        	elect1.user.userprofileinfo.balance -= elect1.Amount
        	elect1.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase #{} Eko Prepaid to this Meter Number {}.'.format(elect1.Amount, elect1.Meter_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Eko Prepaid",
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
        		
        	#email()
        	elect1.user.userprofileinfo.balance -= elect1.Amount
        	elect1.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase #{} Ikeja Prepaid to this Meter Number {}.'.format(elect2.Amount, elect2.Meter_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Ikeja Prepaid",
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
              	#email()
        	elect3.user.userprofileinfo.balance -= elect1.Amount
        	elect3.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase #{} Ibadan Prepaid to this Meter Number {}.'.format(elect3.Amount, elect3.Meter_Number)
        )
                
        	return redirect("index")

    context = {
        "table": " Ibadan Prepaid",
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
        		
        	#email()
        	elect4.user.userprofileinfo.balance -= elect4.Amount
        	elect4.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase #{} Enugu Prepaid to this Meter Number {}.'.format(elect4.Amount, elect4.Meter_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Enugu Prepaid",
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
        		
        	#email()
        	elect5.user.userprofileinfo.balance -= elect1.Amount
        	elect5.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase #{} Eko Postpaid to this Meter Number {}.'.format(elect5.Amount, elect5.Meter_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Eko Postpaid",
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
              	#email()
        	elect6.user.userprofileinfo.balance -= elect6.Amount
        	elect6.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase #{} Ibadan Postpaid to this Meter Number {}.'.format(elect6.Amount, elect6.Meter_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Ibadan Postpaid",
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
        	      	#email()
        	elect7.user.userprofileinfo.balance -= elect1.Amount
        	elect7.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase #{} Ikeja Postpaid to this Meter Number {}.'.format(elect7.Amount, elect7.Meter_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Ikeja Postpaid",
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
        	
        	#email()
        	elect8.user.userprofileinfo.balance -= elect8.Amount
        	elect8.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase #{} Enugu Postpaid to this Meter Number {}.'.format(elect8.Amount, elect8.Meter_Number)
        )
                
        	return redirect("index")

    context = {
        "table": "Enugu Postpaid",
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
        "table": "Waec",
        "cost": "NGN 2000",
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
        
        	#email()
        	neco.user.userprofileinfo.balance -= Amount
        	neco.user.userprofileinfo.save()
        	messages.success(
            request, 'You have purchase Neco Pin to this Email {}.'.format(neco.Email)
        )
                
        	return redirect("index")

    context = {
        "table": "Neco",
        "cost": "NGN 1000",
        "title": "Purchase",
        "form": form
    }
    return render(request, "transactions/form.html", context)

							