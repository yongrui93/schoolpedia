from django import forms
from app.models import Enquiry
import pdb

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ('email', 'description')
