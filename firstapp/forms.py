from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Cluster, Nutzer, Reservation, Datum

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
                
class ClusterForm(ModelForm):
    class Meta:
        model = Cluster
        fields = ('tag_system', 'title', 'Beschreibung', 'availability')

class RegisterForm(UserCreationForm):
#	matrikelnummer = forms.IntegerField(max_value="1000000")

	class Meta:
		model = User
		fields = ("username", "password1", "password2")

	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)
		#user.matrikelnummer = self.cleaned_data['matrikelnummer']
		if commit:
			user.save()
		return user


class DateInput(forms.DateInput):
    input_type = 'date'

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['clus_name', 'date']
        widgets = {
			'date': DateInput(), 
		}
		 