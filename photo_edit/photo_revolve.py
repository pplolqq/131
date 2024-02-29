from PIL import Image
def convert_to_transparent(img):  
    img:Image.Image 
    img = img.convert("RGBA")
    width, height = img.size  
    for x in range(width):  
        for y in range(height):  
            pixel = img.getpixel((x, y))  
            if pixel[0] == 0:  
                img.putpixel((x, y), (255, 255, 255, 0))
    return img
# 将以下路径替换为你的图片文件路径和输出路径  
# 打开图片  
path="mygane0.4/rotate_pic/shovel.png"
place="mygane0.4/rotate_pic/rotato_sholve"
image = Image.open(path)
for i in range(36):
    angle=(i+1)*10  
    rotated_image = image.rotate(angle)
    rotated_image=convert_to_transparent(rotated_image)
# 保存旋转后的图片  
    rotated_image.save(place+f"/No{i}.png",quantity=950)  
