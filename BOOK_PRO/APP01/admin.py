from django.contrib import admin
from APP01 import models
# Register your models here.
admin.site.register(models.Author)
admin.site.register(models.Publish)
admin.site.register(models.AuthorDetail)
admin.site.register(models.Book)