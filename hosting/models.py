from django.db import models
from django.utils import timezone
from jsonfield import JSONField

# Create your models here.
class Room(models.Model):
    start_date=models.DateField(default=timezone.now())
    end_date=models.DateField(default=timezone.now())
    rent_type=models.IntegerField(default=-1) # 양도 1, 기간대여 2, 룸메이트 3
    roomate_num=models.IntegerField(default=-1) # 구하는 룸메이트 수, 양도,기간 대여라면 0
    building_type=models.IntegerField(default=-1) # 아파트 1, 오피스텔 2, 빌라 3
    period=models.IntegerField(default=-1) # 하루 1, 월세 2, 전세 3
    cost=models.IntegerField(default=-1) # 만원 단위로, 2만원이라면 2
    university=models.IntegerField(default=-1)
    gender=models.IntegerField(default=-1) # 남자 1, 여자 2
    addr_gu=models.CharField(max_length=20)
    addr_dong=models.CharField(max_length=20)
    image1=models.ImageField(blank=False, upload_to='images/')
    image2=models.ImageField(blank=True, null=True, upload_to='images/')
    image3=models.ImageField(blank=True, null=True, upload_to='images/')
    detail=models.TextField(default="", blank=True, null=True)
    deposit=models.IntegerField(default=-1) # 보증금
    rooms=models.IntegerField(default=-1)
    options=JSONField(default={'wifi':0, 'air_conditioner':0, 'tv':0, 'doorlock':0, 'washer':0, 'induction':0, 'closet':0, 'desk':0, 'bed':0, 'duplex':0})
    address=models.CharField(max_length=50, default=" ")
    address_detail=models.CharField(max_length=50, default=" ")
    creator=models.CharField(max_length=150, default=" ")
    title=models.CharField(max_length=50, default=" ")

    def pGender(self):
        if self.gender==1:
            return "남"
        if self.gender==2:
            return "여"
    
    def pRentType(self):
        if self.rent_type==1:
            return "양도"
        if self.rent_type==2:
            return "대여"
        if self.rent_type==3:
            return "룸메이트"

    def pBuildingType(self):
        if self.building_type==1:
            return "아파트"
        if self.building_type==2:
            return "오피스텔"
        if self.building_type==3:
            return "빌라"

    def pPeriod(self):
        if self.period==1:
            return "하루 "
        if self.period==2:
            return "월 "
        if self.period==2:
            return "전세 "

    def pCost(self):
        if self.period==1:
            return str(self.cost)
        if self.period==2:
            return str(self.cost)+"/"+str(self.deposit)
        if self.period==3:
            return str(self.cost)

    def pOptions(self):
        list = ["wifi", "air_conditioner", "tv", "doorlock", "washer", "induction", "closet", "dest", "bed", "duplex"]
        for x in list:
            if x in self.options:
                self.options



