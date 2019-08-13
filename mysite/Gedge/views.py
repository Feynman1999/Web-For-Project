import os
from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import UploadImage
from django.core.files.storage import FileSystemStorage
from django.conf import settings

algos={'cyclegan':0, 'poolnet':1}

def upload(request):
    context = {}
    context['algos'] = algos.keys()
    if request.method == "POST":
        # form = UploadForm(request.POST, request.FILES)
        # if form.is_valid():
        #     up_obj = form.save(commit=False)# 此处的save有commit=False参数，意思是只生成model对象，而不保存，生成的model对象就可以修改了
        #     # <class 'Gedge.models.UploadImage'>
        #     up_obj.save()
        #     # print(os.path.join(settings.MEDIA_ROOT, up_obj.img1.name))  # .name 貌似类内调用和类外调用结果不一样（类内是name 类外是有前缀）
        #     # print(os.path.exists(os.path.join(settings.MEDIA_ROOT, up_obj.img1.name)))
        #     up_obj.generate_edge()
        #     return redirect('history')
        if request.FILES.get('img1', -1) == -1:
            return render(request, 'upload.html') 
        select_algo = request.POST.get('algo', None)
        if select_algo is None:
            algotype = 0 
        else:
            algotype = algos.get(select_algo, 0)
        up_obj = UploadImage(img1 = request.FILES['img1'], algo_type = algotype)
        up_obj.save()
        up_obj.generate_edge()
        return redirect('history')
    else:
        pass
    return render(request, 'upload.html', context)   



def history(request):
    uploads = UploadImage.objects.all()
    return render(request, 'history.html', {'uploads': uploads})



def history_detail(request, id):
    upload = UploadImage.objects.get(id = id)
    context={}
    context['upload'] = upload
    return render(request, 'history_detail.html', context)
