import cv2
import numpy as np
import os
from django.conf import settings

def cv_imread(filePath):
    cv_img=cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), -1)
    ## imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
    # cv_img=cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)  # 转为bgr
    return cv_img



# 2 3 两张图  检测1是否库(static/type/image1/)里有一摸一样的
# 有的话取static/type/image2~3 写入到upload下 文件名保持img1相同
# 没有的话就用原图了
def deecamp32(path1, path2, path3, algotype):
    img1 = cv_imread(path1)
    findpath1 = os.path.join(settings.BASE_DIR, 'Algorithms/demo/static/'+ algotype + '/image1/')
    findpath2 = os.path.join(settings.BASE_DIR, 'Algorithms/demo/static/'+ algotype + '/image2/')
    findpath3 = os.path.join(settings.BASE_DIR, 'Algorithms/demo/static/'+ algotype + '/image3/')
    flag = False
    for item in os.listdir(findpath1):
        tpimg = cv_imread(os.path.join(findpath1, item))
        if tpimg.shape == img1.shape and (img1 == tpimg).all():
            # 找到了
            img2 = cv_imread(os.path.join(findpath2, item))
            img3 = cv_imread(os.path.join(findpath3, item))
            flag = True
            break
    if not flag:
        print("没找到已有结果，结果使用原图")
        img2 = img1
        img3 = img1


    file_suffix = os.path.splitext(path2)[1]
    tmp_path2 = os.path.join(settings.BASE_DIR, 'Algorithms/demo/backup/images2/' + os.path.basename(path1))
    cv2.imencode(file_suffix, img2)[1].tofile(tmp_path2)

    file_suffix = os.path.splitext(path3)[1]
    tmp_path3 = os.path.join(settings.BASE_DIR, 'Algorithms/demo/backup/images3/' + os.path.basename(path1))
    cv2.imencode(file_suffix, img3)[1].tofile(tmp_path3)

    return (tmp_path2, tmp_path3)
    


