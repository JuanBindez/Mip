from django.db import models


class IPStatus(models.Model):
    ip = models.CharField(max_length=15)
    status = models.BooleanField(default=False)
    last_checked = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'app'
