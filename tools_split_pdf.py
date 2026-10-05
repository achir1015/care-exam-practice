# 依目錄書本頁碼切檔：PDF 第 n 頁 = 書本第 2n-6（左）與 2n-5（右）頁
import pypdf, copy
from pypdf.generic import RectangleObject
r = pypdf.PdfReader('g.pdf')
W, H = 1194.06, 834.04
TOP, BOT = 0.040, 0.030   # 去掉 iPad 狀態列與底部列
RANGES = {
 "00_共通技術_洗手":(16,18),
 "01_生命徵象測量":(19,36), "02_成人異物哽塞急救法":(37,42), "03_成人心肺甦醒術":(43,55),
 "04_備餐餵食用藥":(56,74), "05_洗頭衣物更換":(75,90), "06_會陰沖洗及尿管清潔":(91,129),
 "07_協助上下床及坐輪椅":(130,144)}
for name,(a,b) in RANGES.items():
    w = pypdf.PdfWriter()
    for p in range(a, b+1):
        if p % 2 == 0: idx, half = (p+6)//2 - 1, 0
        else:          idx, half = (p+5)//2 - 1, 1
        pg = w.add_page(r.pages[idx])
        x0 = 0 if half == 0 else W/2
        box = RectangleObject([x0, H*BOT, x0+W/2, H*(1-TOP)])
        pg.mediabox = box; pg.cropbox = box
    w.compress_identical_objects()
    w.write(f"out/{name}.pdf")
