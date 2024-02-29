from PIL import Image
# 打开图片  
path="mygane0.4/rotate_pic/0.png"
img = Image.open(path)
# 转换为 RGB 模式  
# img_rgb = img.convert("RGB")
# # 转换为灰度模式  
# img_gray = img_rgb.convert("L")
# # 保存为黑白图片  
# img_gray.save(path)  
img = img.convert("RGB")
width, height = img.size  
for x in range(width):  
    for y in range(height):  
        pixel = img.getpixel((x, y))  
        if pixel[0] == 255:  
            img.putpixel((x, y), (255, 255, 0))
# img.save("mygane0.4/rotate_pic/toolbar.png")
# img=img.show()ss
# print(pixel)