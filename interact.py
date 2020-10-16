from instapy import InstaPy
from instapy import smart_run
from time import sleep
import random,time
import os, subprocess

# login credentials
insta_username = 'insta_username'  # <- enter username here
insta_password = 'insta_password'  # <- enter password here


#Read documentation in detail of instapy here: https://github.com/timgrossmann/InstaPy/blob/master/DOCUMENTATION.md
#interact means like, comment and follow
friendly_usernames = ["abc","ass","sfd", "sd"] # with whom you want to interact on daily basis

most_famous_accounts = ['theshaderoom', 'liampayne', 'caiocastro', 'ozuna', 'mancity', 'luisasonza', 'tirullipa', 'dedesecco', 'fashionnova', 'bhadbhabie', 'starbucks', 'sandradewi88', '3gerardpique', 'hannahstocking', 'vans', 'anuel_2blea', 'rockstargames', 'brunogagliasso', 'bramastavrl', 'arsenal', 'houseofhighlights', 'kartikaaryan', 'flaviapavanelli', 'farrukoofficial', 'lucaslucco', 'shaq', 'jscmila', 'burberry', 'carlinhosmaiaof', '_agentgirl_', 'diddy', 'tamerhosny', 'brittanya187', 'earthpix', 'chapolinsincero', 'offsetyrn', 'streetartglobe', 'taapsee', 'blacchyna', 'ikercasillas', 'gadiiing', 'theshilpashetty', 'gabunion', 'thalia', 'cznburak', 'yuyacst', 'michaelkors', 'gianlucavacchi', 'gisele', 'rafakalimann', 'tarajiphenson', 'cvillaloboss', 'future', 'manugavassi', 'lisaandlena', 'ollaramlanaufar', 'bclsinclair', 'hugogloss', 'simoneesimaria', 'daquan', 'samsmith', 'aurelie.hermansyah', 'burakozcivit', 'waynerooney', 'jujusalimeni', 'ninja', 'sarcasm_only', 'camilaqueiroz', 'annecurtissmith', 'bretmanrock', 'borodylia', 'juliaperrezz', 'viihtube', 'cocielo', 'elliegoulding', 'pavelvolyaofficial', 'dagelan', 'nissa_sabyan', 'leosantana', 'dejesusoficial', 'givenchyofficial', 'gusein.gasanov', 'lexa', 'alghazali7', 'greeicy1', 'miguel.g.herran', 'alexisren', 'lakers', 'raphaelvarane', 'gatenm123', 'tutorials.gallery', 'luisafernandaw', 'cagritaner', 'mustafahosnyofficial', 'norafatehi', 'badabun', 'wonderful_places', 'snooki', 'joellemardinian', 'louboutinworld', 'neymarjr', 'natgeo', 'jlo', 'katyperry', 'theellenshow', 'victoriassecret', 'iamcardib', 'nasa', 'priyankachopra', '9gag', 'ronaldinho', 'maluma', 'camila_cabello', 'anitta', 'marvel', 'dualipa', 'willsmith', 'jamesrodriguez10', 'marcelotwelve', 'jacquelinef143', 'raffinagita1717', '5.min.crafts', 'lelepons', 'k.mbappe', 'gucci', 'daddyyankee', 'chanelofficial', 'natgeotravel', 'buzzfeedtasty', 'nickyjampr', 'marinaruybarbosa', 'sunnyleone', 'hm', 'karimbenzema', 'princessyahrini', 'gusttavolima', 'maisa', 'ivetesangalo', 'danbilzerian', 'dior', 'laudyacynthiabella', 'wizkhalifa', 'karolg', 'marshmellomusic', 'wesleysafadao', 'gisel_la', '433', 'bmw', 'mercedesbenz', 'sabrinasato', 'voguemagazine', 'badbunnypr', 'lunamaya', 'lamborghini', 'urvashirautela', 'simoneses', 'natashawilona12', 'kevinho', 'amandacerny', 'julianapaes', 'eliana', 'tiktok', 'ciara', 'sommerray', 'nattinatasha', 'eljuanpazurita', 'kyliecosmetics', 'kapilsharma', 'letthelordbewithyou', 'zachking', 'ashanty_ash', 'chelseaoliviaa', 'sachintendulkar', 'inijedar', 'sebastianyatra', '6ix9ine', 'isisvalverde', 'fernandasouzaoficial', 'agnezmo', 'ludmilla', 'simaria', 'porsche', 'ivan_gunawan', 'versace', 'fcbayern', 'claudialeitte', 'calvinklein', 'miakhalifa', 'tyga', 'chiaraferragni', 'djkhaled', 'alok', 'thegoodquote', 'kimberly.loaiza', 'amberrose', 'brentrivera', 'loren', 'luisitocomunica', 'gio_ewbank', 'aliciakeys', 'tatafersoza', 'toofaced', 'attahalilintar', 'beautifuldestinations', 'bbcnews', 'iamyanetgarcia', 'redbull', '_irishbella_', 'jakepaul', 'kefera', 'kingarturo23oficial', 'dababy', 'rondarousey', 'alfinetei', 'pevpearce', 'rafaavitti', 'giovannaantonelli', 'mercedesamg', 'handemiyy', 'camilomusica', 'iza', 'aliandooo', 'jenselter', 'adamlevine', 'frenchmontana', 'aron.piper', 'anacheri', 'kayla_itsines', 'adrianalima', 'tatizaqui', 'troubleman31', 'lacasadepapel', 'ridwankamil', 'joaoguilherme', 'prettylittlething', 'netflixlat', 'okisetianadewi', 'cita_citata', 'thecwriverdale', 'divyankatripathidahiya', 'mr_faisu_07', 'rickyharun', 'samoylovaoxana', 'danirussotv', 'amandaeliselee', 'germangarmendia', 'nacho', 'albafloresoficial', 'salshabillaadr', 'ahlamalshamsi', 'joselyncano', 'ralphlauren', 'nikebasketball', 'mariapedraza_', 'maudyayunda', 'yasmine_sabri', 'footlocker', 'jailyneojeda', 'wisin', 'cnn', 'sebas', 'isdadahlia', 'theestallion', 'm_galustyan', 'anllela_sagra', 'jordynwoods', 'kiaraaliaadvani', 'natgeoimagecollection', 'ververa', 'lucasranngel', 'amrdiab', 'angeldimariajm', 'cats_of_instagram', 'yandel', 'migos', 'wakeupandmakeup', 'micheltelo', 'mango', 'xuxamenegheloficial', 'rosalia.vt', 'cescf4bregas', 'tiwasavage', 'saudinews50', 'tammyhembrow', 'hoodclips', 'richforever', 'zenetoecristiano', 'balenciaga', 'puma', 'juicewrld999', 'jimmychoo', 'avneetkaur_13', 'yemialade', 'filmygyan', 'samburskaya', 'funkejenifaakindele', 'anastasiya_kvitko', 'salicerose', 'ashleygraham', 'donia.samir.ghanem', 'leaelui', 'radwaelsherbiny', 'angeliqueboyer', 'arcangel', 'thefatjewish', 'lilbaby_1', 'marcanthony', 'sureshraina3', 'giovannachaves', 'dudeperfect', 'soueunavida', 'pabllovittar', 'trippieredd', 'bvb09', 'ahickmann', 'sophiavalverde', 'glennalinskie', 'piawurtzbach', 'morphebrushes', 'mikhail_litvin', 'makegirlz', 'sheinofficial', 'aislinnderbez', 'jadapinkettsmith', 'titi_kamall', 'balmain', 'lanarhoades', 'iqbaal.e', 'inanna', 'nehasharmaofficial', 'nashgrier', 'francinyehlke', 'zyxzjs', 'aurakasih', 'gabyespino', 'pornhub', 'therealcalebmclaughlin', 'araujovivianne', 'mrsayudewi', 'leonardo', 'aline_riscado', 'off____white', 'jiffpom', 'converse', 'kellyrowland', 'audimarissa', 'marigonzalez', 'benefitcosmetics', 'proper_tasty', 'dcyoungfly', 'citraciki', 'jojo_babie', 'ansel', 'camilaloures', 'brazzersofficial', 'tartecosmetics', 'viniciusjunior', 'saadlamjarred1', 'henriqueejuliano', 'manuelneuer', 'itsrossa910', 'torylanez', 'lanacondor', 'natgeowild', 'jojotodynho', 'shuapeck', 'fentybeauty', 'telemundo', 'marcjacobs', 'cartier', 'gabriellasaraivah', 'alexandermcqueen', 'nba_youngboy', 'auronplay', 'bhuvan.bam22', 'catriona_gray', 'moschino', 'sebastianrulli', 'jadepicon', 'karrueche', 'kimshantal', 'alissaviolet', 'lilyachty', 'manelyk_oficial', 'billboard', 'colourpopcosmetics', 'astonmartinlagonda', 'jessicakes33', 'f1', 'belenrodriguezreal', 'andressasuita', 'zelenskiy_official', 'luisfonsi', 'mariahcarey', 'iniedo', 'ladbible', 'jerrysmithoficial', 'sneakernews', 'hitocaesar', 'claudiaalende', 'annakhilkevich', 'nianaguerrero', 'zoesugg', 'rudymancuso', 'time', 'jessica.syj', 'pyonglee', 'alexmorgan13', 'liviaandradereal', 'cinthiacruz_', 'diamondplatnumz', 'saraunderwood', 'abigailratchford', 'volkswagen', 'kodakblack', 'yara', 'dailyart', 'donjazzy', 'lojain_omran', 'bbcpersian', 'davidmichigan', 'peterpsquare', 'hypebeast', 'lindseypelas', 'yuvisofficial', 'syifahadjureal', 'officialboosieig', 'haifa_hassony', 'tessabrooks', 'chelseaislan', 'redvelvet.smtown', 'thedodo', 'lizzobeeating', 'juulianapaiva', '2chainz', 'iamkevingates', 'jyoti_shrotriya_', 'official_pepe', 'swaelee', 'bentleymotors', 'zareenkhan', 'anaclaraac', 'suicidegirls', 'nahcardoso', '6ar8o', 'aycomedian', 'melissamelmaia', 'davidguetta', 'mturizomusic', 'graoficial', 'annanystrom', 'celsoportiolli', 'dr_kholodiii', 'diljitdosanjh', 'ross_lynch', 'ngakakkocak', 'pautips', 'smtown', 'urgantcom', 'cassandraslee', 'arthuraguiar', 'anushkasen0408', 'nph', 'gabrielmedina', 'marcusrashford', 'nohastyleicon', 'malutrevejo', 'khiza_13', 'primark', 'kindalloush', 'flamengo', 'harialmeida_', 'doctor_komarovskiy', 'rizkyfbian', 'supassra_sp', 'barstoolsports', 'o.dembele7', 'michelleziu', 'oficialkellykey', 'dennycagur', 'dynhoalves', 'bulgariofficial', 'ruggeropasquarelli', 'karinakross', 'pretagil', 'tiffanyyoungofficial', 'stassiebaby', 'sbtonline', 'eduardocosta', 'muniknunes', 'margie_rasri', 'afnan_albatel', 'garyvee', '8fact', 'loreimprota', 'galileamontijo', 'drayamichele', 'isabellasantoni', 'boss', 'felipearaujocantor']


comments=[
#Read documentation in detail of instapy here: https://github.com/timgrossmann/InstaPy/blob/master/DOCUMENTATION.md
    {'mandatory_words': ["ice", "india"], 'comments': ["Delhi loves me and I love it",
                                                        "God created Delhi with dil"]},


    {'mandatory_words': [["food",'food']], 'comments': ["The only thing I like better than talking about Food is eating.",
"Wow!! checkout my feed too"]
}
]
photo_comments = ['Nice shot! ',
                 'I love your profile! ',
             'Your feed is an inspiration :thumbsup:',
             'I can feel your passion  :muscle:','nice!','Great!','Cool','Super!','Nice!!!','Good!!!',"Just amazing", "Love your passion!", "Wish you all the best", "Amazing!!", comments]


# I have created multiple sessions so that if one shuts down due to some error or limitations by instagram, new session can be started after hours and do different things.


# interact with followers of starbucks (change it to ["user0","user1" etc])
def interact_with_user_followers(interact_amount,users_amount,username = 'starbucks'):
    session = InstaPy(username='username',
                      password='password',
                      headless_browser=True)
    with smart_run(session):
        session.set_simulation(enabled=True, percentage=100)
        session.set_skip_users(skip_private=True,
                               private_percentage=100,
                               skip_business=True,
                               business_percentage=100)
        session.set_action_delays(enabled=True,
                                   like=50,
                                   comment=100,
                                   follow=317,
                                   unfollow=488,
                                   story=100, randomize=True, random_range_from=90, random_range_to=140)

        session.set_user_interact(amount=interact_amount, randomize=True, percentage=80)
        #session.set_do_follow(enabled=True, percentage=20)
        session.set_do_like(enabled=True, percentage=90)
        session.set_comments(photo_comments)
        session.set_do_comment(enabled=True, percentage=10)
        session.interact_user_followers([username], amount=users_amount, randomize=True)
        session.end()


#unfollow users who do not follow you back
def unfollow_normal_users(unfollow_amount):
    session = InstaPy(username='username',
                      password='password',
                      headless_browser=True)
    with smart_run(session):
        session.set_simulation(enabled=True, percentage=100)
        session.set_skip_users(skip_private=True,
                               private_percentage=100,
                               skip_business=True,
                               business_percentage=100)
        session.set_action_delays(enabled=True,
                                   like=50,
                                   comment=100,
                                   follow=317,
                                   unfollow=488,
                                   story=100, randomize=True, random_range_from=70, random_range_to=140)

        session.unfollow_users(amount=unfollow_amount, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=755)
        session.end()

# learn more about pods here: https://blog.hubspot.com/marketing/instagram-pods
def pods_run(topic='food'):
    session = InstaPy(username='username',
                          password='password',
                          headless_browser=True)
    with smart_run(session):
        session.set_simulation(enabled=True, percentage=100)
        session.set_skip_users(skip_private=True,
                               private_percentage=100,
                               skip_business=True,
                               business_percentage=100)
        session.set_action_delays(enabled=True,
                                   like=50,
                                   comment=100,
                                   follow=317,
                                   unfollow=488,
                                   story=100, randomize=True, random_range_from=70, random_range_to=140)

        session.join_pods(topic=topic, engagement_mode = 'no_comments')
        session.end()



#1. Like your feed
#2. Interact with friendly_usernames
#3. Like by tags
#4. follow by tags
def interact_with_specific_user_and_like_by_feed_and_tags(user, interact_amount):
    session = InstaPy(username='username',
                      password='password',
                      headless_browser=True)
    with smart_run(session):
        session.set_simulation(enabled=True, percentage=100)
        session.set_skip_users(skip_private=True,
                               private_percentage=100,
                               skip_business=True,
                               business_percentage=100)
        session.set_action_delays(enabled=True,
                                   like=50,
                                   comment=100,
                                   follow=317,
                                   unfollow=488,
                                   story=100, randomize=True, random_range_from=70, random_range_to=140)

        #session.set_do_follow(enabled=True, percentage=100)
        session.set_do_comment(enabled=True, percentage=50)
        session.set_do_like(True, percentage=70)
        session.set_user_interact(amount=2, percentage=50)
        session.set_do_follow(enabled=True, percentage=50, times=2)
        session.like_by_feed(amount=5, randomize=True, unfollow=True, interact=True)
        session.set_comments(photo_comments)
        session.interact_by_users([user], amount=interact_amount)
        session.like_by_tags(random.choice(['tag1', 'tag2', 'tag3', 'tag4', 'tag5']), amount=10,interact=True)
        session.follow_by_tags(['tag1', 'tag2'], amount=20)
        session.end()

while True:
    subprocess.run(args= ["python3", "post.py"]) #post a picture with caption
    time.sleep(random.randint(100,200))
    interact_with_specific_user_and_like_by_feed_and_tags(user= random.choice(interact_with_users), interact_amount= 5)
    time.sleep(random.randint(100,200))
    subprocess.run(args= ["python3", "post.py"])
    time.sleep(random.randint(100,300))
    interact_with_specific_user_and_like_by_feed_and_tags(user= random.choice(interact_with_users), interact_amount= 5)
    time.sleep(random.randint(500,600))
    interact_with_user_followers(interact_amount,users_amount,username = ['starbucks'])
    time.sleep(random.randint(500,600))
    pods_run(topic=random.choice(['general', 'fashion', 'food', 'travel', 'sports', 'entertainment']))
    time.sleep(random.randint(3000,6000))
    unfollow_normal_users(unfollow_amount=20)
    time.sleep(random.randint(500,600))
