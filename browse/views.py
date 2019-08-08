from django.shortcuts import render, get_object_or_404
from hosting.models import Room
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_URL= '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# Create your views here.
def home(request):
    return render(request,'home.html')

def base (request):
    return render(request,'base.html')

def findroom (request):
    rooms=Room.objects.all()
    return render(request, 'findroom.html',{'rooms':rooms, 'media_root': MEDIA_ROOT, 'media_url': MEDIA_URL})

def detail(request, room_id):
    room=get_object_or_404(Room,pk=room_id)
    return render(request,'detail.html',{'room':room})


def filter(request):
    start = request.POST.get('start', False)
    end = request.POST.get('end', False)
    #gu = request.POST.get('gu', False)
    #dong = request.POST.get('dong', False)

    gu = request.POST['gu']
    dong = request.POST['dong']

    gender = request.POST.get('gender', None)
    btype = request.POST.get('type', False)
    cost = request.POST.get('cost', False)
    deposit = request.POST.get('deposit', False)
    
    # 성별, 타입이 일치하고 가격이 cost보다 이하인 방들
    _q1 = Q(gender__exact = gender)
    _q2 = Q(building_type__exact = btype)
    _q3 = Q(cost__lte = cost)
    _q4 = Q(deposit__lte = deposit)
    _q5 = Q(start_date = range(start-7, start+7))
    _q5 = Q(end_date = range(end-7, end+7))
    
    # dong = all 이면 같은 구 
    if(dong == "전체"):
        _q6 = Q(addr_gu__exact = gu)
    # dont != all 이면 같은 동
    else:
        _q6 = Q(addr_dong__exact = dong)

    filtered_rooms = Room.objects.filter(_q1 and _q2 and _q3 and _q4 and _q5 and _q6)

    return render(request, 'findroom.html', {'filtered_rooms':filterd_rooms})
    
def test(request):
    gender=request.GET['gender']
    return render(request, 'test.html', {'gender':gender})


def myrooms(request):
    myrooms = Room.objects.filter()
    return render(request, 'myrooms.html')
