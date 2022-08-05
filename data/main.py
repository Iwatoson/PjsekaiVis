import cv2  #OpenCVのインポート
import json
import collections as cl

data205 = [
    3,3,3,3,
    3,3,3,3,
    3,3,3,4,
    4,4,4,3,
    3,3,3,4,
    4,4,4,3,
    3,3,3,5,
    3,3,3,4,
    3,3,3,4,
    3,3,4,3,3,
    3,3,3,4,
    3,3,3,4,
    3,3,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,3,
    3,3,3,4,
    3,3,3,5
]
data155 = [
    4,
    4,4,4,4,
    6,7,
    3,3,4,4,4,
    4,1,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    1,2,1,2,3,
    12,4,
    4,4,4,4,
    4,4,4,6,1,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4
]
data154 = [
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,
    3,3,3,2,
    3,3,3,2,
    3,3,3,2,
    3,3,3,2,
    3,3,3,2,
    3,3,3,2,
    4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4
]
data153 = [
    4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4
]
data122 = [
    4,4,4,4,
    4,4,4,4,
    4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4
]
data107 = [
    5,
    4,5,5,5,
    4,4,4,2,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,6,5,
    4,4,
    4,4,4,4,
    4,4,4,4,
    4,4
]
data087 = [
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    3,3,3,3,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    6,6,
    6,6,
    6,6,
    6,6,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,3,4,3,
    4,3,4,4,
    4,4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4
]
data004 = [
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4,4,4,4,
    4
]
datas205={}
datas155={}
datas154={}
datas153={}
datas122={}
datas107={}
datas087={}
datas004={}

img="image/data205mst.png" #開く画像ファイル名
threshold=127 #二値化閾値
img_color= cv2.imread(img) #画像を読み出しオブジェクトimg_colorに代入
img_gray = cv2.imread(img,cv2.IMREAD_GRAYSCALE) #画像をグレースケールで読み出しオブジェクトimg_grayに代入
img_h,img_w,_=img_color.shape
i=0
count=0
Xpx=201
Ypx=146-2
xpx1=0
xpx2=0
n=0
m=0
c=1
while i<int(img_w/Xpx):
    xpx1=Xpx*i
    xpx2=Xpx*(i+1)
    l=0
    ypx1=0
    ypx2=0
    while l<int(img_h/Ypx):
        if i==0:
            ypx1 = img_h-22-(Ypx*(l+1))
            ypx2 = img_h-22-(Ypx*l)
        else :
            ypx1 = img_h-27-(Ypx*(l+1))
            ypx2 = img_h-27-(Ypx*l)
        img_g = img_gray[ypx1:ypx2,xpx1:xpx2]
        # img_c = img_color[ypx1:ypx2,xpx1:xpx2]
        ret, img_binary= cv2.threshold(img_g, threshold, 127, cv2.THRESH_BINARY) #オブジェクトimg_grayを閾値threshold(127)で二値化しimg_binaryに代入
        contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #img_binaryを輪郭抽出
        # cv2.drawContours(img_c, contours, -1, (0,0,255), 2) #抽出した輪郭を赤色でimg_colorに重ね書き
        count+=len(contours)
        if(len(contours)!=0):
            if(c==1):
                datas205[m]=len(contours)
            else:
                datas205[m]+=len(contours)
            c+=1
            if(data205[m]<c):
                c=1
                m+=1
        l+=1
    i+=1
    print(count)
print(count) #抽出した輪郭の個数を表示する

img="image/data155mst.png" #開く画像ファイル名
threshold=127 #二値化閾値
img_color= cv2.imread(img) #画像を読み出しオブジェクトimg_colorに代入
img_gray = cv2.imread(img,cv2.IMREAD_GRAYSCALE) #画像をグレースケールで読み出しオブジェクトimg_grayに代入
img_h,img_w,_=img_color.shape
i=0
count=0
Xpx=201
Ypx=99-2
xpx1=0
xpx2=0
n=0
m=0
c=1
while i<int(img_w/Xpx):
    xpx1=Xpx*i
    xpx2=Xpx*(i+1)
    l=0
    ypx1=0
    ypx2=0
    while l<int(img_h/Ypx):
        if i==0:
            ypx1 = img_h-22-(Ypx*(l+1))
            ypx2 = img_h-22-(Ypx*l)
        else :
            ypx1 = img_h-27-(Ypx*(l+1))
            ypx2 = img_h-27-(Ypx*l)
        img_g = img_gray[ypx1:ypx2,xpx1:xpx2]
        # img_c = img_color[ypx1:ypx2,xpx1:xpx2]
        ret, img_binary= cv2.threshold(img_g, threshold, 127, cv2.THRESH_BINARY) #オブジェクトimg_grayを閾値threshold(127)で二値化しimg_binaryに代入
        contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #img_binaryを輪郭抽出
        # cv2.drawContours(img_c, contours, -1, (0,0,255), 2) #抽出した輪郭を赤色でimg_colorに重ね書き
        count+=len(contours)
        if(len(contours)!=0):
            if(c==1):
                datas155[m]=len(contours)
            else:
                datas155[m]+=len(contours)
            c+=1
            if(data155[m]<c):
                c=1
                m+=1
        l+=1
    i+=1
    print(count)
print(count) #抽出した輪郭の個数を表示する

img="image/data154mst.png" #開く画像ファイル名
threshold=127 #二値化閾値
img_color= cv2.imread(img) #画像を読み出しオブジェクトimg_colorに代入
img_gray = cv2.imread(img,cv2.IMREAD_GRAYSCALE) #画像をグレースケールで読み出しオブジェクトimg_grayに代入
img_h,img_w,_=img_color.shape
i=0
count=0
Xpx=201
Ypx=99-2
xpx1=0
xpx2=0
n=0
m=0
c=1
while i<int(img_w/Xpx):
    xpx1=Xpx*i
    xpx2=Xpx*(i+1)
    l=0
    ypx1=0
    ypx2=0
    while l<int(img_h/Ypx):
        if i==0:
            ypx1 = img_h-22-(Ypx*(l+1))
            ypx2 = img_h-22-(Ypx*l)
        else :
            ypx1 = img_h-27-(Ypx*(l+1))
            ypx2 = img_h-27-(Ypx*l)
        img_g = img_gray[ypx1:ypx2,xpx1:xpx2]
        # img_c = img_color[ypx1:ypx2,xpx1:xpx2]
        ret, img_binary= cv2.threshold(img_g, threshold, 127, cv2.THRESH_BINARY) #オブジェクトimg_grayを閾値threshold(127)で二値化しimg_binaryに代入
        contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #img_binaryを輪郭抽出
        # cv2.drawContours(img_c, contours, -1, (0,0,255), 2) #抽出した輪郭を赤色でimg_colorに重ね書き
        count+=len(contours)
        if(len(contours)!=0):
            if(c==1):
                datas154[m]=len(contours)
            else:
                datas154[m]+=len(contours)
            c+=1
            if(data154[m]<c):
                c=1
                m+=1
        l+=1
    i+=1
    print(count)
print(count) #抽出した輪郭の個数を表示する

img="image/data153mst.png" #開く画像ファイル名
threshold=127 #二値化閾値
img_color= cv2.imread(img) #画像を読み出しオブジェクトimg_colorに代入
img_gray = cv2.imread(img,cv2.IMREAD_GRAYSCALE) #画像をグレースケールで読み出しオブジェクトimg_grayに代入
img_h,img_w,_=img_color.shape
i=0
count=0
Xpx=201
Ypx=99-2
xpx1=0
xpx2=0
n=0
m=0
c=1
while i<int(img_w/Xpx):
    xpx1=Xpx*i
    xpx2=Xpx*(i+1)
    l=0
    ypx1=0
    ypx2=0
    while l<int(img_h/Ypx):
        if i==0:
            ypx1 = img_h-22-(Ypx*(l+1))
            ypx2 = img_h-22-(Ypx*l)
        else :
            ypx1 = img_h-27-(Ypx*(l+1))
            ypx2 = img_h-27-(Ypx*l)
        img_g = img_gray[ypx1:ypx2,xpx1:xpx2]
        # img_c = img_color[ypx1:ypx2,xpx1:xpx2]
        ret, img_binary= cv2.threshold(img_g, threshold, 127, cv2.THRESH_BINARY) #オブジェクトimg_grayを閾値threshold(127)で二値化しimg_binaryに代入
        contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #img_binaryを輪郭抽出
        # cv2.drawContours(img_c, contours, -1, (0,0,255), 2) #抽出した輪郭を赤色でimg_colorに重ね書き
        count+=len(contours)
        if(len(contours)!=0):
            if(c==1):
                datas153[m]=len(contours)
            else:
                datas153[m]+=len(contours)
            c+=1
            if(data153[m]<c):
                c=1
                m+=1
        l+=1
    i+=1
    print(count)
print(count) #抽出した輪郭の個数を表示する

img="image/data122mst.png" #開く画像ファイル名
threshold=127 #二値化閾値
img_color= cv2.imread(img) #画像を読み出しオブジェクトimg_colorに代入
img_gray = cv2.imread(img,cv2.IMREAD_GRAYSCALE) #画像をグレースケールで読み出しオブジェクトimg_grayに代入
img_h,img_w,_=img_color.shape
i=0
count=0
Xpx=201
Ypx=99-2
xpx1=0
xpx2=0
n=0
m=0
c=1
while i<int(img_w/Xpx):
    xpx1=Xpx*i
    xpx2=Xpx*(i+1)
    l=0
    ypx1=0
    ypx2=0
    while l<int(img_h/Ypx):
        if i==0:
            ypx1 = img_h-22-(Ypx*(l+1))
            ypx2 = img_h-22-(Ypx*l)
        else :
            ypx1 = img_h-27-(Ypx*(l+1))
            ypx2 = img_h-27-(Ypx*l)
        img_g = img_gray[ypx1:ypx2,xpx1:xpx2]
        # img_c = img_color[ypx1:ypx2,xpx1:xpx2]
        ret, img_binary= cv2.threshold(img_g, threshold, 127, cv2.THRESH_BINARY) #オブジェクトimg_grayを閾値threshold(127)で二値化しimg_binaryに代入
        contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #img_binaryを輪郭抽出
        # cv2.drawContours(img_c, contours, -1, (0,0,255), 2) #抽出した輪郭を赤色でimg_colorに重ね書き
        count+=len(contours)
        if(len(contours)!=0):
            if(c==1):
                datas122[m]=len(contours)
            else:
                datas122[m]+=len(contours)
            c+=1
            if(data122[m]<c):
                c=1
                m+=1
        l+=1
    i+=1
    print(count)
print(count) #抽出した輪郭の個数を表示する

img="image/data107mst.png" #開く画像ファイル名
threshold=127 #二値化閾値
img_color= cv2.imread(img) #画像を読み出しオブジェクトimg_colorに代入
img_gray = cv2.imread(img,cv2.IMREAD_GRAYSCALE) #画像をグレースケールで読み出しオブジェクトimg_grayに代入
img_h,img_w,_=img_color.shape
i=0
count=0
Xpx=201
Ypx=114-2
xpx1=0
xpx2=0
n=0
m=0
c=1
while i<int(img_w/Xpx):
    xpx1=Xpx*i
    xpx2=Xpx*(i+1)
    l=0
    ypx1=0
    ypx2=0
    while l<int(img_h/Ypx):
        if i==0:
            ypx1 = img_h-22-(Ypx*(l+1))
            ypx2 = img_h-22-(Ypx*l)
        else :
            ypx1 = img_h-27-(Ypx*(l+1))
            ypx2 = img_h-27-(Ypx*l)
        img_g = img_gray[ypx1:ypx2,xpx1:xpx2]
        # img_c = img_color[ypx1:ypx2,xpx1:xpx2]
        ret, img_binary= cv2.threshold(img_g, threshold, 127, cv2.THRESH_BINARY) #オブジェクトimg_grayを閾値threshold(127)で二値化しimg_binaryに代入
        contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #img_binaryを輪郭抽出
        # cv2.drawContours(img_c, contours, -1, (0,0,255), 2) #抽出した輪郭を赤色でimg_colorに重ね書き
        count+=len(contours)
        if(len(contours)!=0):
            if(c==1):
                datas107[m]=len(contours)
            else:
                datas107[m]+=len(contours)
            c+=1
            if(data107[m]<c):
                c=1
                m+=1
        l+=1
    i+=1
    print(count)
print(count) #抽出した輪郭の個数を表示する

img="image/data087mst.png" #開く画像ファイル名
threshold=127 #二値化閾値
img_color= cv2.imread(img) #画像を読み出しオブジェクトimg_colorに代入
img_gray = cv2.imread(img,cv2.IMREAD_GRAYSCALE) #画像をグレースケールで読み出しオブジェクトimg_grayに代入
img_h,img_w,_=img_color.shape
i=0
count=0
Xpx=201
Ypx=99-2
xpx1=0
xpx2=0
n=0
m=0
c=1
while i<int(img_w/Xpx):
    xpx1=Xpx*i
    xpx2=Xpx*(i+1)
    l=0
    ypx1=0
    ypx2=0
    while l<int(img_h/Ypx):
        if i==0:
            ypx1 = img_h-22-(Ypx*(l+1))
            ypx2 = img_h-22-(Ypx*l)
        else :
            ypx1 = img_h-27-(Ypx*(l+1))
            ypx2 = img_h-27-(Ypx*l)
        img_g = img_gray[ypx1:ypx2,xpx1:xpx2]
        # img_c = img_color[ypx1:ypx2,xpx1:xpx2]
        ret, img_binary= cv2.threshold(img_g, threshold, 127, cv2.THRESH_BINARY) #オブジェクトimg_grayを閾値threshold(127)で二値化しimg_binaryに代入
        contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #img_binaryを輪郭抽出
        # cv2.drawContours(img_c, contours, -1, (0,0,255), 2) #抽出した輪郭を赤色でimg_colorに重ね書き
        count+=len(contours)
        if(len(contours)!=0):
            if(c==1):
                datas087[m]=len(contours)
            else:
                datas087[m]+=len(contours)
            c+=1
            if(data087[m]<c):
                c=1
                m+=1
        l+=1
    i+=1
    print(count)
print(count) #抽出した輪郭の個数を表示する

img="image/data004mst.png" #開く画像ファイル名
threshold=127 #二値化閾値
img_color= cv2.imread(img) #画像を読み出しオブジェクトimg_colorに代入
img_gray = cv2.imread(img,cv2.IMREAD_GRAYSCALE) #画像をグレースケールで読み出しオブジェクトimg_grayに代入
img_h,img_w,_=img_color.shape
i=0
count=0
Xpx=201
Ypx=99-2
xpx1=0
xpx2=0
n=0
m=0
c=1
while i<int(img_w/Xpx):
    xpx1=Xpx*i
    xpx2=Xpx*(i+1)
    l=0
    ypx1=0
    ypx2=0
    while l<int(img_h/Ypx):
        if i==0:
            ypx1 = img_h-22-(Ypx*(l+1))
            ypx2 = img_h-22-(Ypx*l)
        else :
            ypx1 = img_h-27-(Ypx*(l+1))
            ypx2 = img_h-27-(Ypx*l)
        img_g = img_gray[ypx1:ypx2,xpx1:xpx2]
        # img_c = img_color[ypx1:ypx2,xpx1:xpx2]
        ret, img_binary= cv2.threshold(img_g, threshold, 127, cv2.THRESH_BINARY) #オブジェクトimg_grayを閾値threshold(127)で二値化しimg_binaryに代入
        contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #img_binaryを輪郭抽出
        # cv2.drawContours(img_c, contours, -1, (0,0,255), 2) #抽出した輪郭を赤色でimg_colorに重ね書き
        count+=len(contours)
        if(len(contours)!=0):
            if(c==1):
                datas004[m]=len(contours)
            else:
                datas004[m]+=len(contours)
            c+=1
            if(data004[m]<c):
                c=1
                m+=1
        l+=1
    i+=1
    print(count)
print(count) #抽出した輪郭の個数を表示する

ccount=0
for a in datas205:
    ccount+=datas205[a]
print(ccount)
ccount=0
for a in datas155:
    ccount+=datas155[a]
print(ccount)
ccount=0
for a in datas154:
    ccount+=datas154[a]
print(ccount)
ccount=0
for a in datas153:
    ccount+=datas153[a]
print(ccount)
ccount=0
for a in datas122:
    ccount+=datas122[a]
print(ccount)
ccount=0
for a in datas107:
    ccount+=datas107[a]
print(ccount)
ccount=0
for a in datas087:
    ccount+=datas087[a]
print(ccount)
ccount=0
for a in datas004:
    ccount+=datas004[a]
print(ccount)

names=["205","155","154","153","122","107","087","004"]

datas=cl.OrderedDict()

datas[names[0]]=datas205
datas[names[1]]=datas155
datas[names[2]]=datas154
datas[names[3]]=datas153
datas[names[4]]=datas122
datas[names[5]]=datas107
datas[names[6]]=datas087
datas[names[7]]=datas004

jdata=open("data.json","w")

json.dump(datas,jdata,indent=4)

# cv2.imwrite("out_sample.png", img_c)
# cv2.imshow("contours",img_c) #別ウィンドウを開き(ウィンドウ名 "contours")オブジェクトimg_colorを表示
# cv2.waitKey(0) #キー入力待ち
# cv2.destroyAllWindows() #ウインドウを閉じる