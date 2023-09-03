from django.forms import ModelForm, TextInput, NumberInput, Select, DateTimeInput

from .enums import AssetTypes
from .models import Asset


class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = ['title', 'type', 'amount', 'date']

        widgets = {
            'title': TextInput(attrs={"type": "text"}),
            'type': Select(choices=[(choice.name, choice.value) for choice in AssetTypes]),
            'amount': NumberInput(attrs={"type": "number", "min": "0"}),
            'date': DateTimeInput(attrs={"type": "date"}),
        }
