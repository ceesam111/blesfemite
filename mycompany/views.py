from django.shortcuts import render
from mycompany.forms import UserForm, UserProfileInfoForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import  redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from .models import Pricetag
from .models import UserProfileInfo, Contact
from transactions.models import MTN,GLO,AIRTEL,GOTV,DSTV,STARTIMES,ELECTRICITY,EXAM
from transactions.models import Withdrawal, MTN_AIRTIME,GLO_AIRTIME,AIRTEL_AIRTIME,MTN_AWUF_AIRTIME,MTN_SHARE_AIRTIME,MTN_500MB_SME,MTN_2GB_SME,MTN_1GB_SME,MTN_3GB_SME,MTN_4GB_SME,MTN_5GB_SME,MTN_10GB_SME,MTN_1GB_WD,MTN_1P5GB_MD,MTN_2GB_MD,MTN_20GB_WD,GLO_50MB,GLO_150MB,GLO_350MB,GLO_2P9GB,GLO_4P1GB,GLO_5P8GB,GLO_7P7GB,GLO_13P75GB,GLO_18P25GB,AIRTEL_750MB,AIRTEL_1GB,AIRTEL_2GB,AIRTEL_3GB,AIRTEL_6GB,AIRTEL_10GB,AIRTEL_20GB,DSTV_PADI,DSTV_XTRAVIEW,DSTV_ASIAN_ADDON,DSTV_FRENCH_BOUGUET,DSTV_COMPACT_PLUS_F,DSTV_CONFAM,DSTV_YANGA, DSTV_PREMIUM,DSTV_COMPACT_PLUS,DSTV_COMPACT_PLUS_ASIAN_ADDON,GOTV_JOLLI,GOTV_SMALLIE,GOTV_LITE_QUART,GOTV_LITE_YEAR, GOTV_MAX,GOTV_JINJA,STARTIME_SMART_M,STARTIME_BASIC_M,STARTIME_CLASSIC_M,STARTIME_NOVA_M,STARTIME_SMART_W,STARTIME_BASIC_W,STARTIME_CLASSIC_W,STARTIME_NOVA_W,STARTIME_SMART_D,STARTIME_NOVA_D,STARTIME_BASIC_D,STARTIME_CLASSIC_D,ELECT_EKO_PRE,ELECT_IKEJA_PRE,ELECT_IBADAN_PRE,ELECT_ENUGU_PRE,ELECT_IKEJA_POST, ELECT_IBADAN_POST,ELECT_EKO_POST,ELECT_ENUGU_POST,WAEC,NECO

from django.views.generic import CreateView

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT IS DEACTIVATED")
        else:
            return HttpResponse("Please use correct id and password")
            # return HttpResponseRedirect(reverse('register'))

    else:
        return render(request, 'mycompany/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# Create your views here.

def blog(request):
	return render(request,'mycompany/blog.html')
	
def portfolio(request):
	return render(request,'mycompany/portfolio.html')


def index(request):
	return render(request,'mycompany/index.html')
	


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'mycompany/registration.html',
                            {'registered':registered,
                             'user_form':user_form,
                             'profile_form':profile_form})

class HomeView(TemplateView):
    template_name = 'mycompany/index.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mtns = MTN.objects.all()
        glos = GLO.objects.all()
        airtels = AIRTEL.objects.all()
        dstvs = DSTV.objects.all()
        gotvs = GOTV.objects.all()
        exams = EXAM.objects.all()
        startimes = STARTIMES.objects.all()
        pricetags = Pricetag.objects.all()
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
        mtn11s = MTN_2GB_MD.objects.all()
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
        context['pricetags'] = pricetags
        context['glos'] = glos
        context['airtels'] = airtels
        context['startimes'] = startimes
        context['dstvs'] = dstvs
        context['gotvs'] = gotvs
        context['exams'] = exams  
        context['pricetags'] = pricetags
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
        
        
        
           
class ContactView(CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'mycompany/contact.html'


