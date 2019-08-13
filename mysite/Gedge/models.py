import threading
import os
import time
from django.db import models
from django.conf import settings
from django.core.files import File
from django.utils import timezone
from Algorithms.demo import run

class AlgoTypeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


img1path = 'Uploads/images1/'
img2path = 'Uploads/images2/'
img3path = 'Uploads/images3/'

map_algo = []
map_algo.append('cyclegan')  # type 0 -> cyclegan
map_algo.append('poolnet')  # type 1 -> poolnet


# 考虑多线程 更复杂方案：Celery  可定时执行一些任务
class Generate_Edge(threading.Thread):
    def __init__(self, UploadImage_obj):
        self.UploadImage_obj = UploadImage_obj
        self.imgname = os.path.basename(UploadImage_obj.img1.name)
        self.imgname_no_suffix = os.path.splitext(self.imgname)[0]
        self.path1 = os.path.join(settings.MEDIA_ROOT, UploadImage_obj.img1.name)
        # self.path2 = os.path.join(settings.MEDIA_ROOT, img2path) + self.imgname_no_suffix + '.svg'
        self.path2 = os.path.join(settings.MEDIA_ROOT, img2path) + self.imgname
        self.path3 = os.path.join(settings.MEDIA_ROOT, img3path) + self.imgname
        self.algotype = UploadImage_obj.algo_type
        threading.Thread.__init__(self)

    def run(self):
        print('开始处理 目标路径：' + self.path2)
        if self.algotype > len(map_algo) - 1:
            raise AlgoTypeError('please check AlgoType is 0 ~ {}'.format(len(map_algo) - 1))
        # string = "from Algorithms." + map_algo[self.algotype] + " import run"
        # exec(string, globals())
        while not os.path.exists(self.path1):  # 等待用户上传图片写入磁盘
            time.sleep(0.1)
            print("wait!")
        tmp_path2, tmp_path3 = run.deecamp32(self.path1, self.path2, self.path3, map_algo[self.algotype])  # 生成另外2种图
        # 记录完成时间
        self.UploadImage_obj.finished_time = timezone.now()        
        # generate之后指定自己的img2 img3
        self.UploadImage_obj.img3.save(
            os.path.basename(self.path3),
            File(open(tmp_path3, 'rb'))
        )
        self.UploadImage_obj.img2.save(
            os.path.basename(self.path2),
            File(open(tmp_path2, 'rb'))
        )
        self.UploadImage_obj.save()
        print('处理完毕 路径2：' + self.path2  + '路径3：' + self.path3)


class UploadImage(models.Model):
    author = models.CharField(max_length = 200, null=True, blank = True, default = "admin")
    upload_time = models.DateTimeField(auto_now_add=True)  # editable=False blank=True
    finished_time = models.DateTimeField(null=True, blank = True)  # 指的是生成image2的时间
    img1 = models.ImageField(upload_to = img1path)
    img2 = models.ImageField(upload_to = img2path, null = True, blank = True)
    img3 = models.ImageField(upload_to = img3path, null = True, blank = True)  # 矢量化
    algo_type = models.IntegerField(default = 0) 
    
    def __str__(self):
        return self.img1.url  

    class Meta:
        ordering = ["-upload_time"]

    def generate_edge(self):
        # 实例化Generate_Edge对象 开始执行
        ge_obj = Generate_Edge(self)
        ge_obj.start() # 开启线程
