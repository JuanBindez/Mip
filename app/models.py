from django.db import models
import subprocess

class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    last_ping_status = models.BooleanField(default=False)

    def __str__(self):
        return self.ip_address

    def update_ping_status(self):
        result = subprocess.run(['ping', '-c', '1', str(self.ip_address)], capture_output=True, text=True)
        if result.returncode == 0:
            self.last_ping_status = True
        else:
            self.last_ping_status = False
        self.save()

