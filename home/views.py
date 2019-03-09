from django.shortcuts import render
from django.views import View
import requests
import cv2


from .forms import (
    CoordinateEntryForm,
    ImageUploadForm,
)

from .utils import (
    ImageGeneratorFromGoogleMap,
)

from .models import(
    GoogleMapImage,
)

class HomeView(View):
    template_name = 'home/home.html'
    form_class = CoordinateEntryForm

    def get(self, request):
        form = self.form_class()
        context = {
        'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        context = {
            'form': form,
        }

        if form.is_valid():
            lat = form.cleaned_data.get('longitude')
            lng = form.cleaned_data.get('latitude')
            zoom = form.cleaned_data.get('zoom_level')

            gmd = ImageGeneratorFromGoogleMap(lat, lng, zoom)
            print("The tile coorindates are {}".format(gmd.getXY()))

            try:
                # Get the high resolution image
                img = gmd.generateImage()
            except IOError:
                print("Could not generate the image - try adjusting the zoom level and checking your coordinates")
            else:
                #Save the image to disk
                img.save("img_"+str(lat)+"_"+str(lng)+"_zoom_"+str(zoom)+"_.png")
                print("The map has been successfully created")


            return render(request, self.template_name, context)

        return render(request, self.template_name, context)




class ImageIdentification(View):
    template_name = 'home/upload.html'
    form_class = ImageUploadForm

    def get(self, request):
        form = self.form_class()
        context = {
        'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        context = {
            'form': form,
        }

        if form.is_valid():
            print('valid...')
            file = request.FILES['file']

            print(file, 'file...')
            return render(request, self.template_name, context)

        print('Error')
        return render(request, self.template_name, context)
