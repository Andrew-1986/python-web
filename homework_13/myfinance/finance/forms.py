from django import forms

from django.core.exceptions import ValidationError
from django.core.validators import validate_comma_separated_integer_list
from django.forms.widgets import Widget
from django.utils.translation import ugettext_lazy as _
from datetime import datetime, timedelta

from .models import Category

class NewOpExpenseForm(forms.Form):

    expense_cat = forms.ModelChoiceField(queryset=Category.objects.filter(type__contains='expense'))
    val = forms.DecimalField(max_digits=10, decimal_places=2)

    def clean_val(self):
        v = self.cleaned_data['val']

        if v <= 0:
            raise ValidationError(_('Sorry, you must pay...'))
        
        if v >= 10000:
            raise ValidationError(_('Sorry, you not Rocfeller'))
        
        return v

class NewOpProfitForm(forms.Form):

    profit_cat = forms.ModelChoiceField(queryset=Category.objects.filter(type__contains='profit'))
    val = forms.DecimalField(max_digits=10, decimal_places=2)

    def clean_val(self):
        v = self.cleaned_data['val']

        if v <= 0:
            raise ValidationError(_('Sorry, you must work harder...'))
        
        if v >= 10000:
            raise ValidationError(_('Sorry, you not Rocfeller'))
        
        return v

class ReportForm(forms.Form):

    CHOICES = [(0, 'expense'), (1, 'profit'), (2,'balance')]

    initilal_date = datetime.now() - timedelta(days=7)

    date_from = forms.DateField(widget=forms.SelectDateWidget, initial=(initilal_date.date))
    date_to = forms.DateField(widget=forms.SelectDateWidget, initial=(datetime.now().date))
    mode = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, initial=(CHOICES[0]))

    # def clean_date_from(self):

    #     clean_date = self.cleaned_data['date_from']

    #     return clean_date