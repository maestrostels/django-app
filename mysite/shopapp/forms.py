
from django import forms
from shopapp.models import Product

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        if isinstance(data, (list, tuple)):
            cleaned_data = []
            for item in data:
                cleaned_item = super().clean(item, initial)
                cleaned_data.append(cleaned_item)
            return cleaned_data
        return super().clean(data, initial)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", "description", "discount", "preview"

    # images = forms.ImageField(
    #     widget=forms.ClearableFileInput(attrs={"multiple": True}),
    # )

    images = MultipleFileField(
        required=False,
        label="Images"
    )


class CSVImportForm(forms.Form):
    csv_file = forms.FileField()


class JSONImportForm(forms.Form):
    json_file = forms.FileField()