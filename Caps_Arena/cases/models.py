from django.db import models

class chip(models.Model):
    user_id = models.TextField()
    chip_id = models.TextField()
    way = models.TextField()
    
class chip_type(models.Model):
    chip_id = models.TextField()
    chip_name = models.TextField()
    chip_ico = models.TextField()
    can_drop = models.TextField()
    
class case(models.Model):
    case_name = models.TextField()
    case_drop = models.TextField()
    