from django.db import models
from django.conf import settings
import uuid
# Create your models here.
class Order(models.Model):

    details = models.TextField(max_length=2000)
    fulfilled = models.BooleanField(default=False)
    taker = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,related_name='orders_taken')
    fulfilled_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,related_name='orders_fulfilled')
    created = models.DateTimeField(auto_now_add=True)
    unique_number = models.UUIDField(default=uuid.uuid4(),editable=False,)