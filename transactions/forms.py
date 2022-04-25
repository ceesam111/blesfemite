from django import forms
from mycompany.models import UserProfileInfo, User
from .models import Withdrawal, MTN_AIRTIME,GLO_AIRTIME,AIRTEL_AIRTIME,MTN_AWUF_AIRTIME,MTN_SHARE_AIRTIME,MTN_500MB_SME,MTN_2GB_SME,MTN_1GB_SME,MTN_3GB_SME,MTN_4GB_SME,MTN_5GB_SME,MTN_10GB_SME,MTN_1GB_WD,MTN_1P5GB_MD,MTN_2GB_MD,MTN_20GB_WD,GLO_50MB,GLO_150MB,GLO_350MB,GLO_2P9GB,GLO_4P1GB,GLO_5P8GB,GLO_7P7GB,GLO_13P75GB,GLO_18P25GB,AIRTEL_750MB,AIRTEL_1GB,AIRTEL_2GB,AIRTEL_3GB,AIRTEL_6GB,AIRTEL_10GB,AIRTEL_20GB,DSTV_PADI,DSTV_XTRAVIEW,DSTV_ASIAN_ADDON,DSTV_FRENCH_BOUGUET,DSTV_COMPACT_PLUS_F,DSTV_CONFAM,DSTV_YANGA, DSTV_PREMIUM,DSTV_COMPACT_PLUS,DSTV_COMPACT_PLUS_ASIAN_ADDON,GOTV_JOLLI,GOTV_SMALLIE,GOTV_LITE_QUART,GOTV_LITE_YEAR, GOTV_MAX,GOTV_JINJA,STARTIME_SMART_M,STARTIME_BASIC_M,STARTIME_CLASSIC_M,STARTIME_NOVA_M,STARTIME_SMART_W,STARTIME_BASIC_W,STARTIME_CLASSIC_W,STARTIME_NOVA_W,STARTIME_SMART_D,STARTIME_NOVA_D,STARTIME_BASIC_D,STARTIME_CLASSIC_D,ELECT_EKO_PRE,ELECT_IKEJA_PRE,ELECT_IBADAN_PRE,ELECT_ENUGU_PRE,ELECT_IKEJA_POST, ELECT_IBADAN_POST,ELECT_EKO_POST,ELECT_ENUGU_POST,WAEC,NECO




class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields = ["amount","wallet_address","phone_number", "bank_details"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(WithdrawalForm, self).__init__(*args, **kwargs)

    def clean_amount(self):
        amount = self.cleaned_data['amount']

        return amount

class Airtime1Form(forms.ModelForm):
    class Meta:
        model = MTN_AIRTIME
        fields = ["Mobile_Number","Amount"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Airtime1Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Airtime2Form(forms.ModelForm):
    class Meta:
        model = GLO_AIRTIME
        fields = ["Mobile_Number","Amount"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Airtime2Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Airtime4Form(forms.ModelForm):
    class Meta:
        model = AIRTEL_AIRTIME
        fields = ["Mobile_Number","Amount"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Airtime4Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Airtime5Form(forms.ModelForm):
    class Meta:
        model = MTN_AWUF_AIRTIME
        fields = ["Mobile_Number","Amount"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Airtime5Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Airtime6Form(forms.ModelForm):
    class Meta:
        model = MTN_SHARE_AIRTIME
        fields = ["Mobile_Number","Amount"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Airtime6Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Mtn1Form(forms.ModelForm):
    class Meta:
        model = MTN_500MB_SME
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Mtn1Form, self).__init__(*args, **kwargs)

    #def clean_amount(self):
  #      Amount = self.cleaned_data['Amount']

        #return Amount

class Mtn2Form(forms.ModelForm):
    class Meta:
        model = MTN_1GB_SME
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Mtn2Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Mtn3Form(forms.ModelForm):
    class Meta:
        model = MTN_2GB_SME
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Mtn3Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount




class Mtn4Form(forms.ModelForm):
    class Meta:
        model = MTN_3GB_SME
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Mtn4Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Mtn5Form(forms.ModelForm):
    class Meta:
        model = MTN_4GB_SME
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Mtn5Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Mtn6Form(forms.ModelForm):
    class Meta:
        model = MTN_5GB_SME
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Mtn6Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Mtn7Form(forms.ModelForm):
    class Meta:
        model = MTN_10GB_SME
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Mtn7Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Mtn8Form(forms.ModelForm):
    class Meta:
        model = MTN_1GB_WD
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Mtn8Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Mtn9Form(forms.ModelForm):
    class Meta:
        model = MTN_1P5GB_MD
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Mtn9Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Mtn10Form(forms.ModelForm):
    class Meta:
        model = MTN_2GB_MD
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Mtn10Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount


class Mtn11Form(forms.ModelForm):
    class Meta:
        model = MTN_20GB_WD
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Mtn11Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Glo1Form(forms.ModelForm):
    class Meta:
        model = GLO_50MB
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Glo1Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Glo2Form(forms.ModelForm):
    class Meta:
        model = GLO_150MB
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Glo2Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Glo3Form(forms.ModelForm):
    class Meta:
        model = GLO_350MB
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Glo3Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Glo4Form(forms.ModelForm):
    class Meta:
        model = GLO_2P9GB
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Glo4Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Glo5Form(forms.ModelForm):
    class Meta:
        model = GLO_4P1GB
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Glo5Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Glo6Form(forms.ModelForm):
    class Meta:
        model = GLO_5P8GB
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Glo6Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount


class Glo7Form(forms.ModelForm):
    class Meta:
        model = GLO_7P7GB
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Glo7Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Glo8Form(forms.ModelForm):
    class Meta:
        model = GLO_13P75GB
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Glo8Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Glo9Form(forms.ModelForm):
    class Meta:
        model = GLO_18P25GB
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Glo9Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Airtel1Form(forms.ModelForm):
    class Meta:
        model = AIRTEL_750MB
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Airtel1Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Airtel2Form(forms.ModelForm):
    class Meta:
        model = AIRTEL_1GB
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Airtel2Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Airtel3Form(forms.ModelForm):
    class Meta:
        model = AIRTEL_2GB
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Airtel3Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Airtel4Form(forms.ModelForm):
    class Meta:
        model = AIRTEL_3GB
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Airtel4Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount


class Airtel5Form(forms.ModelForm):
    class Meta:
        model = AIRTEL_6GB
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Airtel5Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Airtel6Form(forms.ModelForm):
    class Meta:
        model = AIRTEL_10GB
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Airtel6Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Airtel7Form(forms.ModelForm):
    class Meta:
        model = AIRTEL_20GB
        fields = ["Mobile_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Airtel7Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Dstv1Form(forms.ModelForm):
    class Meta:
        model = DSTV_PADI
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Dstv1Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Dstv1Form(forms.ModelForm):
    class Meta:
        model = DSTV_PADI
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Dstv1Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Dstv1Form(forms.ModelForm):
    class Meta:
        model = DSTV_PADI
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Dstv1Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Dstv1Form(forms.ModelForm):
    class Meta:
        model = DSTV_PADI
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Dstv1Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Dstv1Form(forms.ModelForm):
    class Meta:
        model = DSTV_PADI
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Dstv1Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Dstv1Form(forms.ModelForm):
    class Meta:
        model = DSTV_PADI
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Dstv1Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount


class Dstv1Form(forms.ModelForm):
    class Meta:
        model = DSTV_PADI
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Dstv1Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount



class Dstv1Form(forms.ModelForm):
    class Meta:
        model = DSTV_PADI
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Dstv1Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Dstv1Form(forms.ModelForm):
    class Meta:
        model = DSTV_PADI
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Dstv1Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Dstv1Form(forms.ModelForm):
    class Meta:
        model = DSTV_PADI
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Dstv1Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Dstv2Form(forms.ModelForm):
    class Meta:
        model = DSTV_XTRAVIEW
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Dstv2Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Dstv3Form(forms.ModelForm):
    class Meta:
        model = DSTV_ASIAN_ADDON
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Dstv3Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Dstv4Form(forms.ModelForm):
    class Meta:
        model = DSTV_FRENCH_BOUGUET
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Dstv4Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount


class Dstv5Form(forms.ModelForm):
    class Meta:
        model = DSTV_COMPACT_PLUS_F
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Dstv5Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount


class Dstv6Form(forms.ModelForm):
    class Meta:
        model = DSTV_CONFAM
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Dstv6Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Dstv7Form(forms.ModelForm):
    class Meta:
        model = DSTV_YANGA
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Dstv7Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Dstv8Form(forms.ModelForm):
    class Meta:
        model = DSTV_PREMIUM
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Dstv8Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Dstv9Form(forms.ModelForm):
    class Meta:
        model = DSTV_COMPACT_PLUS
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Dstv9Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Dstv10Form(forms.ModelForm):
    class Meta:
        model = DSTV_COMPACT_PLUS_ASIAN_ADDON
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Dstv10Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Gotv1Form(forms.ModelForm):
    class Meta:
        model = GOTV_JOLLI
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Gotv1Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount


class Gotv2Form(forms.ModelForm):
    class Meta:
        model = GOTV_SMALLIE
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Gotv2Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount



class Gotv3Form(forms.ModelForm):
    class Meta:
        model = GOTV_LITE_QUART
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Gotv3Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Gotv4Form(forms.ModelForm):
    class Meta:
        model = GOTV_LITE_YEAR
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Gotv4Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Gotv5Form(forms.ModelForm):
    class Meta:
        model = GOTV_MAX
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Gotv5Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Gotv6Form(forms.ModelForm):
    class Meta:
        model = GOTV_JINJA
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Gotv6Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Startime1Form(forms.ModelForm):
    class Meta:
        model = STARTIME_SMART_M
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Startime1Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Startime2Form(forms.ModelForm):
    class Meta:
        model = STARTIME_BASIC_M
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Startime2Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount


class Startime3Form(forms.ModelForm):
    class Meta:
        model = STARTIME_CLASSIC_M
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Startime3Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount


class Startime4Form(forms.ModelForm):
    class Meta:
        model = STARTIME_NOVA_M
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Startime4Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Startime5Form(forms.ModelForm):
    class Meta:
        model = STARTIME_SMART_W
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Startime5Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Startime6Form(forms.ModelForm):
    class Meta:
        model = STARTIME_BASIC_W
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Startime6Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Startime7Form(forms.ModelForm):
    class Meta:
        model = STARTIME_CLASSIC_W
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Startime7Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Startime8Form(forms.ModelForm):
    class Meta:
        model = STARTIME_NOVA_W
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Startime8Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Startime9Form(forms.ModelForm):
    class Meta:
        model = STARTIME_SMART_D
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Startime9Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount


class Startime10Form(forms.ModelForm):
    class Meta:
        model = STARTIME_NOVA_D
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Startime10Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount


class Startime11Form(forms.ModelForm):
    class Meta:
        model = STARTIME_BASIC_D
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Startime11Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Startime12Form(forms.ModelForm):
    class Meta:
        model = STARTIME_CLASSIC_D
        fields = ["Smart_Card_Number_or_IUC"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Startime12Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Elect1Form(forms.ModelForm):
    class Meta:
        model = ELECT_EKO_PRE
        fields = ["Amount", "Meter_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Elect1Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Elect2Form(forms.ModelForm):
    class Meta:
        model = ELECT_IKEJA_PRE
        fields = ["Amount", "Meter_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Elect2Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Elect3Form(forms.ModelForm):
    class Meta:
        model = ELECT_IBADAN_PRE
        fields = ["Amount", "Meter_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Elect3Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Elect4Form(forms.ModelForm):
    class Meta:
        model = ELECT_ENUGU_PRE
        fields = ["Amount", "Meter_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Elect4Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Elect5Form(forms.ModelForm):
    class Meta:
        model = ELECT_IKEJA_POST
        fields = ["Amount", "Meter_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Elect5Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Elect6Form(forms.ModelForm):
    class Meta:
        model = ELECT_IBADAN_POST
        fields = ["Amount", "Meter_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Elect6Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount

class Elect7Form(forms.ModelForm):
    class Meta:
        model = ELECT_EKO_POST
        fields = ["Amount", "Meter_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Elect7Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount


class Elect8Form(forms.ModelForm):
    class Meta:
        model = ELECT_ENUGU_POST
        fields = ["Amount", "Meter_Number"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Elect8Form, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount


class WaecForm(forms.ModelForm):
    class Meta:
        model = WAEC
        fields = ["Email"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(WaecForm, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount


class NecoForm(forms.ModelForm):
    class Meta:
        model = NECO
        fields = ["Email"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(NecoForm, self).__init__(*args, **kwargs)

    def clean_amount(self):
        Amount = self.cleaned_data['Amount']

        return Amount


