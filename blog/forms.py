from django import forms
from .models import Parking , Reserve


class ParkingForm(forms.ModelForm):

    class Meta:
        model = Parking
        fields = ('title', 'text',)

class ReserveForm(forms.ModelForm):


    class Meta:
        model = Reserve
        fields = ('author', 'text','start','end')
