from vqr import vQR

url="QQ:457335363"

pic_path="./RowPic/Vecang_CCH.png"
icon_path="./RowPic/Vecang.png"

save_path="./HandledPic/Vecang_Pic.png"
save_path2="./HandledPic/Vecang_Icon.png"
save_path3="./HandledPic/Vecang_IconPic.png"


QRsize=120

qrpic=vQR(url)
qrpic.makePicWithQR(pic_path,save_path)
qrpic.makeQRWithIcon(icon_path,save_path2)
qrpic.makeIconPic(icon_path,pic_path,save_path3,"BottomLeft",size=QRsize)