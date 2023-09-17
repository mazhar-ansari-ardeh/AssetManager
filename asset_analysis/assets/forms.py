from django.forms import ModelForm, TextInput, NumberInput, Select, DateTimeInput

from .enums import AssetTypes
from .models import Stock


class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = ['title', 'type', 'quantity', 'price', 'date_obtained']

        widgets = {
            'symbol': TextInput(attrs={"type": "text"}),
            'type': Select(choices=[(choice.name, choice.value) for choice in AssetTypes]),
            'quantity': NumberInput(attrs={"type": "number", "min": "0"}),
            'price': NumberInput(attrs={"type": "number", "min": "0"}),
            'date_obtained': DateTimeInput(attrs={"type": "date"}),
        }
