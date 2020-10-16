from time import sleep
import pandas as pd

from csv import reader

from instabot import Bot


bot = Bot()


# open csv filw which contains image name and caption in read mode
d = pd.read_csv("/home/johncena/Videos/insta/page1",)

for idx, row in d.iterrows():
    #folder containing images is images1
    image = '/home/johncena/Videos/insta/final_images/' + row['image_name']
    #print(image)
    caption = row['caption']
    print("**************",caption)
    bot.login(username = "username",
              password =  'password')

    try:
        bot.upload_photo(image,
                     caption =caption)

        d = d.drop(idx)
        d.to_csv("/home/johncena/Videos/insta/page1", index=False)
        print("Done")
        break
    except Exception as e:
        print(e)
