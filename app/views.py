from django.shortcuts import render, redirect
from src.models import IPStatus


def status(request):
    ip_statuses = IPStatus.objects.all()
    return render(request, 'index.html', {'ip_statuses': ip_statuses})

def adicionar_ip(request):
    if request.method == 'POST':
        ip = request.POST['ip']
        ip_status = IPStatus.objects.create(ip=ip)
        ip_status.save()
        return redirect('status')
    return render(request, 'index.html')