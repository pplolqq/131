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
path="game_shoot_pvp\pic\stave1.png"
place="game_shoot_pvp\z_temp\Z_temp_1"
image = Image.open(path)
for i in range(36):
    angle=(i+1)*10  
    rotated_image = image.rotate(angle)
    # rotated_image=convert_to_transparent(rotated_image)
# 保存旋转后的图片  
    rotated_image.save(place+f"/No{i}.png",quantity=950)  

print("ok!")