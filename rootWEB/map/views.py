from django.shortcuts import render

# Create your views here.
def map(request) :
    print('>>>>>> debug , 127.0.0.1:8000/cm/index')
    return render(request , 'map/map.html')


def jongno(request) :
    print('>>>>>> debug , 127.0.0.1:8000/cm/jongno')
    return render(request , 'map/jongno.html')

def seocho(request) :
    print('>>>>>> debug , 127.0.0.1:8000/cm/seocho')
    return render(request , 'map/seocho.html')


def gwangjin(request) :
    print('>>>>>> debug , 127.0.0.1:8000/cm/gwangjin')
    return render(request , 'map/gwangjin.html')


def seongdong(request) :
    print('>>>>>> debug , 127.0.0.1:8000/cm/seongdong')
    return render(request , 'map/seongdong.html')

def yongsan(request) :
    print('>>>>>> debug , 127.0.0.1:8000/cm/seongdong')
    return render(request , 'map/yongsan.html')