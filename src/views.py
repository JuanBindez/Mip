from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import IPAddress
import subprocess

@csrf_exempt
def update_ip_status(request):
    if request.method == 'POST':
        ip_address = request.POST.get('ip_address')
        ip_obj = Ip.objects.get(ip_address=ip_address)
        result = subprocess.run(['ping', '-c', '1', ip_address], capture_output=True, text=True)
        if result.returncode == 0:
            ip_obj.last_ping_status = True
        else:
            ip_obj.last_ping_status = False
        ip_obj.save()
        return JsonResponse({'status': ip_obj.last_ping_status})
    else:
        ips = Ip.objects.all()
        return render(request, 'status.html', {'ips': ips})


def monitor_ip(request):
    if request.method == 'POST':
        ip_address = request.POST.get('ip_address')
        ip_obj, created = IPAddress.objects.get_or_create(ip_address=ip_address)
        ip_obj.update_ping_status()

    ip_list = IPAddress.objects.all()

    return render(request, 'ip_monitor.html', {'ip_list': ip_list})

# Create your views here.
