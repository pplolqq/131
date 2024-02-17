from PIL import Image
def reset_size(size,image_path,out_path):#set the size
    path = image_path
    img = Image.open(path)
    new_size = size
    img_resized = img.resize(new_size)
    img_resized.save(out_path)
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

path=r"C:\python.pycharm\picture\pic_plant\sunflower\gif"
input_image_path = r"C:\python.pycharm\picture\pic_plant\pee\gif"
output_image_path = r"C:\python.pycharm\picture\pic_plant\pee\gif"
if __name__=="__main__":
    # convert_to_transparent(input_image_path, output_image_path)
    for i in range(18):
        input_image_path=path+r"\No{}.png".format(i)
        output_image_path=input_image_path
        size=(70,75)
        reset_size(size,input_image_path,output_image_path)
    print("success!")