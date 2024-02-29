from PIL import Image,ImageSequence

path="game_pvz_01\picture\pic_temp\sun.gif"
# path=""
pic=Image.open(path)
l=0
place="game_pvz_01\picture\pic_temp"
for frame in ImageSequence.all_frames(pic):
   frame.save(place+fr"\No{l}.png",quality=95)
   l+=1
    