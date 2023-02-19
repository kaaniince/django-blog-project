from django.db import models
from blog.abstract_models import DateAbstractModel

class ContactModel(DateAbstractModel):
    email = models.EmailField(max_length=250)
    name_surname=models.CharField(max_length=150)
    message=models.TextField()
  
    class Meta:
        db_table="contact"
        verbose_name="Contact"
        verbose_name_plural="Contact"
    def __str__(self):
        return self.email