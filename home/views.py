from django.shortcuts import render
from django.views import View
import requests
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

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

from .detector import (
    _object_detector
)

import argparse
import os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


from django.conf import settings

image_path = settings.MEDIA_ROOT + 'images/'
file_path = settings.STATIC_ROOT

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
                img_name = "img_"+str(lat)+"_"+str(lng)+"_zoom_"+str(zoom)+"_.png"
                img.save(image_path+img_name)

                new_img = cv.imread(image_path+img_name)
                print(new_img, 'this is from google map..')

                context['success'] = True
                my_image = "img_40.072_-82.88_zoom_19_.png"
                context['image_url'] = image_path+my_image
                return render(request, self.template_name, context)

        my_image = "Newphoto.png"

        # img = cv.imread(image_path+my_image)
        # cv.line(img, (0,0), (150,150), (255, 255, 255), 15)
        # cv.rectangle(img, (15, 25), (200, 155), (0, 255, 0), 5)
        # cv.imshow('image', img)
        # cv.waitKey(0)
        # cv.destroAllWindows()

        context['image_url'] = image_path+my_image
        context['success'] = True
        return render(request, self.template_name, context)




class ImageIdentification(View):
    template_name = 'home/upload.html'
    form_class = ImageUploadForm

    def get(self, request):
        # print(image_path, 'image_path...')
        img = cv.imread(image_path+"/123.png", cv.IMREAD_GRAYSCALE)
        print(img, 'img...')




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



class ObjectDetectionTest(View):
    template_name = 'home/detection.html'

    def get(self, request):

        _object_detector()
        # my_image = "Newphoto.png"
        # my_image = "prl.JPG"
        #
        # face_cascade = cv.CascadeClassifier("/home/raj/PythonProjects/GIS/env/lib/python3.5/site-packages/cv2/data/haarcascade_frontalface_alt.xml")
        # eye_cascade = cv.CascadeClassifier("/home/raj/PythonProjects/GIS/env/lib/python3.5/site-packages/cv2/data/haarcascade_eye.xml")
        #
        # img = cv.imread(image_path+my_image)
        # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        #
        # faces = face_cascade.detectMultiScale(gray, 1.5, 5)
        # print(faces, 'faces...')
        # for (x,y,w,h) in faces:
        #     cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #     roi_gray = gray[y:y+h, x:x+w]
        #     roi_color = img[y:y+h, x:x+w]
        #     eyes = eye_cascade.detectMultiScale(roi_gray)
        #     for (ex,ey,ew,eh) in eyes:
        #         cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        # cv.imshow('img',img)
        # cv.waitKey(0)
        # cv.destroyAllWindows()


        context = {
        'title': 'Object Detection',
        }
        return render(request, self.template_name, context)
