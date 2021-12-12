from django.conf import settings
import os

# from PaddyMonitoringSystem import settings

def get_image_directory(image_instance_path):
    # zz = str(settings.MEDIA_ROOT
    a= str(settings.BASE_DIR).split('\\')
    a[0] = 'D:\\'
    a.append('media')
    b= str(image_instance_path).split('/')
    return os.path.join(*a,*b) 
    # return os.path.join(*a,"/media/",*b) 
    # return os.path.join(zz, "/", image_instance_path) 