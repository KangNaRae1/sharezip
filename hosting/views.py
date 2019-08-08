from django.shortcuts import render, redirect
from .models import Room
from sharezip.settings import MEDIA_ROOT, MEDIA_URL

# Create your views here.

def hosting1(request):
    return render(request,'hosting1.html')
   
def create1(request):
    room = Room()
    room.addr_gu = request.POST.get('addr_gu', False)
    room.addr_dong = request.POST.get('addr_dong', False)
    room.address = request.POST.get('address', False)
    room.address_detail = request.POST.get('detailAddress', False)
    room.rent_type = request.POST.get('rent_type', False)
    room.roommate_num = request.POST.get('roommate_num', False)
    room.building_type = request.POST.get('building_type', False)
    room.rooms = request.POST.get('room_num', False)
    room.options = request.POST.getlist('options', False)
    room.save()
    return render(request,'hosting2.html',{'current_room':room.id, 'rtype':room.rent_type})
    
def create2(request):
    room_id = request.POST.get('room_obj', False)    # 룸 객체 아이디
    room = Room.objects.get(id=room_id)
    
    room.image1 = request.FILES.get('thumb1')
    room.image2 = request.FILES.get('thumb2')
    room.image3 = request.FILES.get('thumb3')
    room.detail = request.POST.get('details', False)
    room.title = request.POST.get('title', False)
    room.cost = request.POST.get('cost', False)
    room.start_date = request.POST.get('start_date', False)
    room.end_date = request.POST.get('end_date', False)
    room.deposit = request.POST.get('deposit', False)
    room.save()
    return redirect('/')

def hosting2(request):
    return render(request, 'hosting2.html')
