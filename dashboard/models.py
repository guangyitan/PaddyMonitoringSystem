from django.db import models

# Create your models here.

class PaddyAreaInfo(models.Model): #child
    area_name = models.CharField(max_length = 225)
    start_date = models.DateTimeField()
    logitude = models.DecimalField(max_digits = 9, decimal_places = 6, null = True)
    latitude = models.DecimalField(max_digits = 9, decimal_places = 6, null = True)
    # verbose_name, used as display name in django
    # growth_classification = models.IntegerField(verbose_name = "Growth Classification", null=True)
    # latest_image = models.ImageField(default='default.png', blank=True, upload_to='info_images')

    def __str__(self):
        return self.area_name 

class ImagePredictions(models.Model):
    paddy_area_id = models.ForeignKey(PaddyAreaInfo, on_delete=models.CASCADE)
    prediction_date = models.DateTimeField()
    # image used to predict the growth
    image = models.ImageField(default='default.png', blank=True, upload_to='photos/%Y/%m/%d')
    # prediction result
    prediction = models.IntegerField()

    def _str_(self):
        return self.paddy_area_id + str(self.prediction_date)


