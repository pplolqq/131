from PIL import Image
def reset_size(size,image_path,out_path):#set the size
    path = image_path
    img = Image.open(path)
    new_size = size
    img_resized = img.resize(new_size)
    img_resized.save(out_path)
path=r"game_shoot_pvp\pic\gun.png"
size=(40,28)
# input_image_path = r"game_shoot_pvp/pic/back1.png"
input_image_path =path
# output_image_path = r"game_shoot_pvp/pic/back1.png"
output_image_path =path
if __name__=="__main__":

    # convert_to_transparent(input_image_path, output_image_path)
    reset_size(size,input_image_path,output_image_path)
    print("success!")