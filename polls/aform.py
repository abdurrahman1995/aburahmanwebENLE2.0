from django import forms
from mysite.polls.models import Adusert
from mysite.polls.models import User_Admin

class adusrform(forms.ModelForm):
    class Meta:
         model = Adusert
         fields = "__all__"

class uadminform(forms.ModelForm):
    class Meta:
        model = User_Admin
        fields = "__all__"