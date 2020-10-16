# Instagram-Automation-using-Python
After reading a medium article about a guy who eats for free in New York using automation, artificial intelligence and Instagram, I decided to build this system for me.
article linl: https://medium.com/@chrisbuetti/how-i-eat-for-free-in-nyc-using-python-automation-artificial-intelligence-and-instagram-a5ed8a1e2a10

After experimenting with  two instagram accounts, I decided to open source the code for this project.

Three things you need:
1. Instagram account
2. Google cloud platform vision api(which google provides for free)
3. Even if you dont want to use above mentioned api, it will work.

Steps:
1. Enter the name of accounts, whose images you want to share in ig_users.txt(each account in a new line)
2. Run pip install -r requirements.txt
3. Create free google cloud platform account(needs debit/credit card) and download json file(keep it in same directory as notebook), which contains service account to use api using python client.(This step is optional and is used to filter images, which contains owner's signatures and for object detecion to classify objects into different categories to assign different tags and captions accordingly to these tags). You can use the free credits to run a vm instance on gcp and run your code from there for free for 1 year.
Note: You can also use open source alternatives to gcp for image processing like yoplov5 for object detection and ocr for text detecion. i tried them but open source ocr was miserable at detecting texts.
4. Run jupyter notebook and read comments to understand thoroughly.
5. Specify hashtags, captions, comments according to your theme of isntagram page inside jupyter notebook.


Note: A lot more can be done if you want. Thank you for visiting this repo and if you have any doubts you can raise an issue and I will try to resolve them.
Please star my repo, if you like my work.

I have deleted the instagram accounts I created for experimentation. This repo is only for sharing knowledge. Bots are not permitted on instagram as it affects real users. Please do not use this code for doing any unethical activity on instagram.

Thank you open source community for sharing immense amount of knowledge everday on world wide web.
