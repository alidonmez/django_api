from django.db import models

# Create your models here.

class FormEntry(models.Model):
    name = models.CharField(max_length=80)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(max_length=255,default='')

    def get_dob(self):
        return self.dob

    def __repr__(self):
        return self.name + ' added.'    