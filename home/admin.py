from django.contrib import admin
from .models import PortfolioMaster



# Register your models here.
admin.site.register(PortfolioMaster)


admin.site.site_header = "Thycha Creations Admin"
admin.site.site_title = "Thycha Creations Admin Page"
admin.site.index_title = "Welcome to Thycha Creations Page Manager"