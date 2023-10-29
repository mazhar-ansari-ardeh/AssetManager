from django import forms

from .models import Stock

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class NewStockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('category', 'name', 'ticker', 'quantity', 'purchase_price', 'currency', 'purchased_at')
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'ticker': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'quantity': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'purchase_price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'currency': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'purchased_at': forms.DateTimeInput(attrs={
                "type": "date"
            }),
        }


class EditStockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('name', 'ticker', 'quantity', 'purchase_price', 'currency', 'purchased_at')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'ticker': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'quantity': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'purchase_price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'currency': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'purchased_at': forms.DateTimeInput(attrs={
                "type": "date"
            }),

        }
