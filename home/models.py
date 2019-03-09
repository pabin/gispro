from django.db import models


class GoogleMapImage(models.Model):
    image = models.ImageField(upload_to="images")
    thumbnail = models.ImageField(upload_to="images", null=True)
    def save(self, *args, **kwargs):
        super(GoogleMapImage, self).save(*args, **kwargs)
        self.thumbnail = get_thumbnail(self.image,
                                      '50X50',
                                      crop='center',
                                      quality=00).url
