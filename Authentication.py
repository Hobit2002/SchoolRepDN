from django.core.cache import cache
from ipware import get_client_ip
import socket

def VisitorIp(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    try:
        socket.inet_aton(ip)
        ip_valid = True
    except socket.error:
        ip_valid = False
    if ip_valid is True:
        return ip

def ExcludeROB(request):
    Ip = VisitorIp(request)
    #cache.set(str(Ip),1,86400)
    IpCount = cache.get_or_set(str(Ip),1, 86400)
    if IpCount>30:
        return False
    else:
        cache.set(str(Ip),IpCount+1, 86400)
        return True