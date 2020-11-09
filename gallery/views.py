from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from .models import Exhibition
from django.views.decorators.csrf import csrf_exempt
import os
import shutil
import json
from PIL import Image
from datetime import datetime
from .models import Images

FILE_PATH = "/home/palette/media/test/"

# 검색
@csrf_exempt
# json 반환
def getData(request):
    pass
    

# 삭제
@csrf_exempt
def deleteExhibition(request):
    pass


# json Update
def update():
    j = open(FILE_PATH + "database.json", encoding="utf-8-sig")
    newList = {}
    newList["DATA"] = []

    try:
        json_data = json.loads(j.read())
        print(json_data["DATA"])
        now = datetime.now()
        date_time = now.strftime("%Y%m%d")

        for i in range (len(json_data["DATA"])):
            print(json_data["DATA"][i]["DUEDATE"], end = ' ')

            if (int(json_data["DATA"][i]["DUEDATE"])) >= (int(date_time)):
                newList["DATA"].append(json_data["DATA"][i])

    except Exception as e:
        print(e)

    j.close()

    with open(FILE_PATH + 'database.json', 'w', encoding='UTF-8-sig') as f:
        f.write(json.dumps(newList, ensure_ascii=False, indent=4))


# 전시회 정보 반환
@csrf_exempt
def getExhibition(request):
    code = request.POST.get('code')
    
    try :
        exhibition_bp = Exhibition.objects.get(galleryCode=code)
        result = exhibition_bp.galleryCode
        
    except Exception as e:
        print(e)
        return HttpResponse('-1')
    
# 전시회 정보 저장
@csrf_exempt
def register(request):
    GalleryTitle = request.POST.get('galleryTitle')
    GalleryCreator = request.POST.get('galleryCreator')
    GalleryInfo = request.POST.get('galleryInfo')
    GalleryAmount = request.POST.get('galleryAmount')
    Titles = request.POST.get('titles')
    Contents = request.POST.get('contents')
    DueDate = request.POST.get('dueDate')
    Category = request.POST.get('category')
    
    # 코드 생성
    CODE = makeCode()

    j = open(FILE_PATH + "database.json", encoding="utf-8-sig")
    newList = {}
    newList["DATA"] = []

    try:
        json_data = json.loads(j.read())
        print(json_data["DATA"])
        now = datetime.now()
        date_time = now.strftime("%Y%m%d")

        for i in range (len(json_data["DATA"])):
            print(json_data["DATA"][i]["DUEDATE"], end = ' ')
        
            if (int(json_data["DATA"][i]["DUEDATE"])) >= (int(date_time)):
                newList["DATA"].append(json_data["DATA"][i])

    except Exception as e:
        print(e)

    dictToAdd = {"CODE":CODE, "TITLE":GalleryTitle, "CREATOR":GalleryCreator, "INFO":GalleryInfo, "AMOUNT":str(GalleryAmount), "ARTTITLES":Titles, "ARTCONTENTS":Contents, "DUEDATE":str(DueDate), "CATEGORY":Category}

    newList["DATA"].append(dictToAdd)
    j.close()
   
    print(newList)

    with open(FILE_PATH + 'database.json', 'w', encoding='UTF-8-sig') as f:
        f.write(json.dumps(newList, ensure_ascii=False, indent=4))

    newExhibition = Exhibition(galleryCode=CODE, galleryTitle=GalleryTitle, galleryCreator=GalleryCreator, galleryInfo=GalleryInfo, galleryAmount=GalleryAmount, titles=Titles, contents=Contents, dueDate=DueDate, category=Category)

    try :
        newExhibition.save(force_insert=True)
        return HttpResponse('1')
    except Exception as e:
        print(e)
        return HttpResponse('-1')


#exhibition 코드 생성
def makeCode():
    f = open(FILE_PATH + "galleryCode.txt", 'r')
    line = f.read()
    if (line == ''):
        line = '0'
    CODE = int(line) + 1
    f.close()

    f = open(FILE_PATH + "galleryCode.txt", 'w')
    f.write(str(CODE))

    return str(CODE) 


@csrf_exempt
def uploadTest(request):
    code = request.POST.get('code')
    img = request.FILES['image']

    bp = Exhibition.objects.get(galleryCode=code)
    
    try:
        n = str(int(bp.galleryAmount) + 1)
        bp.galleryAmount=n
        bp.save()
        return HttpResponse('1')
    except Exception as e:
        print(e)
        return HttpResponse('-1')

@csrf_exempt
def upload(request):
    file = request.FILES.get()

@csrf_exempt
def create (request):

    image_list = request.FILES.getlist('image')
    for item in image_list:
        images = Images.objects.create(photo=item)
        images.save()
        
    return HttpResponse('1')

@csrf_exempt
def joinInfo(request):
    code = request.POST.get('code')
    title = request.POST.get('title')
    content = request.POST.get('contents')

    try :
        bp = Exhibition.objects.get(galleryCode = code)
        bp.galleryAmount = str(int(bp.galleryAmout) + 1)
        bp.titles = bp.titles + "&"
        bp.contents = bp.contents + "&"
        bp.save()
        return HttpResponse('1')
    except Exception as e:
        print(e)
        return HttpResponse('-1')


