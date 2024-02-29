from PIL import Image
def convert_to_transparent(image_path, output_path): #transparent the pic 
    img = Image.open(image_path)
    img = img.convert("RGBA")
    width, height = img.size  
    for x in range(width):  
        for y in range(height):  
            pixel = img.getpixel((x, y))  
            if pixel[0] == 0:  
                img.putpixel((x, y), (255, 255, 255, 0))
    img.save(output_path, "PNG")
# 将以下路径替换为你的图片文件路径和输出路径  
input_image_path = "mygane0.4/rotate_pic/sa/No35.png"  
output_image_path = "mygane0.4/rotate_pic/toolbar.png"
if __name__=="__main__":
    pass