"""
一个生成二维码的库

作者:vecang
邮箱:www.457335363@qq.com
"""
import qrcode
from PIL import Image
 

url="QQ:457335363"

pic_path="./RowPic/Vecang_CCH.png"
icon_path="./RowPic/Vecang.png"

save_path="./HandledPic/Vecang_Pic.png"
save_path2="./HandledPic/Vecang_Icon.png"
save_path3="./HandledPic/Vecang_IconPic.png"

class vQR(object):
    def __init__(self,url):
        self.url = url
        
        self.qr=qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=2
            )
        self.make_qr()
        
    def make_qr(self):
        self.qr.add_data(self.url)
        self.qr.make(fit=True) 
        self.qr_img=self.qr.make_image()
        self.qr_img=self.qr_img.convert("RGBA")

    def makeQRWithIcon(self,icon,save_path):
        self.icon=Image.open(icon).convert("RGBA")  
        # 重置图标大小
        img_w,img_h=self.qr_img.size
        factor=4
        size_w=int(img_w/factor)
        size_h=int(img_h/factor)
        icon_w,icon_h=self.icon.size
        if icon_w>size_w:
            icon_w=size_w
        if icon_h>size_h:
            icon_h=size_h
        self.icon=self.icon.resize((icon_w,icon_h),Image.ANTIALIAS)
        set_w=int((img_w-icon_w)/2)
        set_h=int((img_h-icon_h)/2)

        self.qr_img.paste(self.icon,(set_w,set_h),self.icon)
        self.qr_img.save(save_path)

    def makePicWithQR(self,qrpic,save_path,setWhere="BottomRight",size=150):
        self.qr_img=self.qr_img.resize((size,size),Image.ANTIALIAS)
        self.qrpic=Image.open(qrpic).convert("RGBA") 
        pic_w,pic_h=self.qrpic.size 
        if setWhere=="BottomRight":
            self.qrpic.paste(self.qr_img,(pic_w-size,pic_h-size))   
        elif setWhere=="BottomLeft":
            self.qrpic.paste(self.qr_img,(0,pic_h-size))  
        elif setWhere=="TopRight":
            self.qrpic.paste(self.qr_img,(pic_w-size,0))   
        elif setWhere=="TopLeft":
            self.qrpic.paste(self.qr_img,(0,0))

        self.qrpic.save(save_path)
    
    def makeIconPic(self,icon,qrpic,save_path,setWhere="BottomRight",size=150):
        self.makeQRWithIcon(icon,save_path)
        self.makePicWithQR(qrpic,save_path,setWhere,size)
    
    


if __name__=="__main__":
    # 设置二维码大小,默认150
    QRsize=80

    qrpic=vQR(url)
    qrpic.makePicWithQR(pic_path,save_path)
    qrpic.makeQRWithIcon(icon_path,save_path2)
    qrpic.makeIconPic(icon_path,pic_path,save_path3,"BottomRight",QRsize)