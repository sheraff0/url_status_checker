import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Url


@login_required(login_url='/checkpoint/login/')
def url_list(request):
    urls = Url.objects.all()
    return render(request, 'url-list.html', {
        'urls': urls})


@login_required(login_url='/checkpoint/login/')
@api_view(['GET', ])
def request_url(request, **kwargs):
    pk = kwargs.get('pk')
    url = Url.objects.filter(pk=pk).first()
    if not url:
        return Response({})
    r = requests.get(url)
    return Response({
        "status": r.status_code
    })
