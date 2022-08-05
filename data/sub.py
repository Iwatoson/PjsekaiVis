import cv2  #OpenCVのインポート

img="image/205bg.png" #開く画像ファイル名
# img1="image/data155mst.png" #開く画像ファイル名
threshold=127 #二値化閾値

img_color= cv2.imread(img) #画像を読み出しオブジェクトimg_colorに代入
img_gray = cv2.imread(img,cv2.IMREAD_GRAYSCALE) #画像をグレースケールで読み出しオブジェクトimg_grayに代入

# img_color1= cv2.imread(img1) #画像を読み出しオブジェクトimg_colorに代入
# img_gray1 = cv2.imread(img1,cv2.IMREAD_GRAYSCALE) #画像をグレースケールで読み出しオブジェクトimg_grayに代入

img_h,img_w,_=img_color.shape

img_a=img_h-180

image_cut = img_gray[img_a:img_h-23,0:201]
# image_cut1 = img_gray1[img_h-172:img_h-23,0:201]

cv2.imwrite("out_sampl.png", image_cut)
# cv2.imwrite("out_sampl1.png", image_cut1)

print(int(img_h/146))