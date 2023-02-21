from django.db import models
import os,datetime
from django.core.exceptions import ValidationError
from thycha.settings import MEDIA_ROOT

def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 4.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
    
# Create your models here.
class PortfolioMaster(models.Model):
    id = models.CharField(primary_key=True,max_length=50)
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=15,default='all',choices=[('all','all'),('print','print'),('packaging','packaging'),('illust','illust'),('digi','digi'),('brands','brands')])
    desc = models.TextField(null=True,blank=True)
    thumbnailimage = models.ImageField(upload_to ='uploads/',validators=[validate_image], blank=True, null=True,help_text='Maximum file size allowed is 4Mb')
    image1 = models.ImageField(upload_to ='uploads/',validators=[validate_image], blank=True, null=True,help_text='Maximum file size allowed is 4Mb')
    image2 = models.ImageField(upload_to ='uploads/',validators=[validate_image], blank=True, null=True,help_text='Maximum file size allowed is 4Mb')
    image3 = models.ImageField(upload_to ='uploads/',validators=[validate_image], blank=True, null=True,help_text='Maximum file size allowed is 4Mb')
    image4 = models.ImageField(upload_to ='uploads/',validators=[validate_image], blank=True, null=True,help_text='Maximum file size allowed is 4Mb')
    image5 = models.ImageField(upload_to ='uploads/',validators=[validate_image], blank=True, null=True,help_text='Maximum file size allowed is 4Mb')
    image6 = models.ImageField(upload_to ='uploads/',validators=[validate_image], blank=True, null=True,help_text='Maximum file size allowed is 4Mb')
    image7 = models.ImageField(upload_to ='uploads/',validators=[validate_image], blank=True, null=True,help_text='Maximum file size allowed is 4Mb')
    image8 = models.ImageField(upload_to ='uploads/',validators=[validate_image], blank=True, null=True,help_text='Maximum file size allowed is 4Mb')

    class Meta:
        db_table = "PORTFOLIOMASTER"
    def __str__(self):
        return self.id+' '+self.name
    def save(self, *args, **kwargs):
        
        try:
            if self.id:
                id_instance = PortfolioMaster.objects.get(id = self.id)
                if id_instance.upload != self.upload:
                    try:
                        os.remove(MEDIA_ROOT+str(id_instance.upload))
                    except:
                        pass
        except:
            pass
        super().save(*args, **kwargs)
    