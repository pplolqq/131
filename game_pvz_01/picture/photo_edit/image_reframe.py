from PIL import Image,ImageSequence

path="mygame0.2/pic/zombie.gif"
# path=""
pic=Image.open(path)
l=0
place="mygame0.2/gif/gif_zombie"
for frame in ImageSequence.all_frames(pic):
   frame.save(place+f"/No{l}.png",quality=95)
   l+=1
    