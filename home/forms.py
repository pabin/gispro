from django import forms


class CoordinateEntryForm(forms.Form):
    longitude = forms.FloatField(label='Longitude')
    latitude = forms.FloatField(label='Latitude')
    zoom_level = forms.IntegerField(label='Zoom Level')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
                })


class ImageUploadForm(forms.Form):
    file = forms.FileField(label="Choose JPG/PNG File")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
                })
