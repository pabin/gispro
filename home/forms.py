from django import forms


class CoordinateEntryForm(forms.Form):
    longitude = forms.FloatField(label='Longitude', initial=40.072)
    latitude = forms.FloatField(label='Latitude', initial=-82.88)
    zoom_level = forms.IntegerField(label='Zoom Level', initial=18)

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
