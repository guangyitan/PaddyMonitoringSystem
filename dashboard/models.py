from django.db import models

# Create your models here.

class PaddyAreaInfo(models.Model): #child
    # paddy_area_info_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    start_date = models.DateTimeField(auto_now_add=True)
    growth_calssification = models.IntegerField()
    paddy_images = models.ImageField(default='default.png', blank=True, upload_to='info_images')

    def __str__(self):
        return self.area_name