from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://sparta:test@cluster0.8eblj3r.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

members = [
    {
        'id': 1, 
        'name':'임호중', 
        'img_index':'static/images/index_lim.JPG',
        'img_1':'images/hojooglim01.JPG',
        'img_2':'images/hojooglim02.JPG',
        'img_3':'images/hojooglim03.JPG',
        'man':'남자', 
        'birth':'1991.04.08', 
        'position':'팀장', 
        'fav_1':'테니스', 
        'fav_2':'조깅', 
        'fav_3':'여행', 
        'fav_4':'술', 
        'fav_5':'축구', 
        'nav_1':'추위',
        'nav_2':'더위',
        'nav_3':'배고픔', 
        'nav_4':'지저분한것', 
        'nav_5':'더러운것',
        'tmi_1':'MBTI:ISTj',
        'tmi_2':'1년 내내 전기장판 틀기',
        'tmi_3':'기혼',
        'tmi_4':'맥유저',
        'tmi_5':'핸드폰은 갤럭시',
        'music':'부석순 - 화이팅해야지',
        'music_url' : '<iframe width="560" height="315" src="https://www.youtube.com/embed/mBXBOLG06Wc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
    },
    {
        'id': 2,
        'name':'최혜원',
        'img_index':'static/images/IMG_2272.JPG',
        'img_1':'images/hyewon1.JPG',
        'img_2':'images/hyewon2.JPG',
        'img_3':'images/hyewon3.JPG',
        'man':'여자',
        'birth':'1994.02.18',
        'position':'팀원',
        'fav_1':'사진📷',
        'fav_2':'여행🌊',
        'fav_3':'러닝🏃‍♀️',
        'fav_4':'커피☕️',
        'fav_5':'음악🎧',
        'nav_1':'시끄러운 곳',
        'nav_2':'주목받는 것',
        'nav_3':'술, 담배',
        'nav_4':'예의 없는 사람',
        'nav_5':'지저분한 것',
        'tmi_1':'MBTI:INFP',
        'tmi_2':'수다떠는 걸 좋아해요',
        'tmi_3':'집에 안 읽은 책이 많아요',
        'tmi_4':'여름에 손에만 땀이 나요',
        'tmi_5':'콜드브루를 좋아해요',
        'music':'CHARLIE PUTH - THATS NOT HOW THIS WORKS',
        'music_url' : '<iframe width="560" height="315" src="https://www.youtube.com/embed/PAKFzFqJa58" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
    },
    {   'id': 3, 
        'name':'양소영', 
        'img_index':'static/images/pic_y.JPG',
        'img_1':'images/young_01.JPG',
        'img_2':'images/young_02.JPG',
        'img_3':'images/young_03.JPG',
        'man':'여자', 
        'birth':'1990.07.13', 
        'position':'팀원', 
        'fav_1':'자연&도시', 
        'fav_2':'국내&국외 여행', 
        'fav_3':'게임', 
        'fav_4':'성장', 
        'fav_5':'문화 생활. 음악,그림,영화,책...!', 
        'nav_1':'더우면서 습한 날씨',
        'nav_2':'무례한 말과 행동',
        'nav_3':'담배', 
        'nav_4':'불만, 짜증, 불평', 
        'nav_5':'욕',
        'tmi_1':'MBTI:ENTJ',
        'tmi_2':'원래 잠이 별로 없어요',
        'tmi_3':'현지 음식 먹어요 !',
        'tmi_4':'잘 웃어요',
        'tmi_5':'손이 많이 차요',
        'music':'A R I Z O N A - Moving On',
        'music_url' : '<iframe width="560" height="315" src="https://www.youtube.com/embed/YMHRCXiGrvo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
    },
    {
        'id': 4, 
        'name':'추지혜', 
        'img_index':'static/images/index_jihye.JPG',
        'img_1':'images/jihye01.JPG',
        'img_2':'images/jihye01.JPG',
        'img_3':'images/jihye01.JPG',
        'man':'여자', 
        'birth':'1999.09.15', 
        'position':'팀원', 
        'fav_1':'music is my life', 
        'fav_2':'산과 바다', 
        'fav_3':'넷플릭스', 
        'fav_4':'카페', 
        'fav_5':'여유로운 시간', 
        'nav_1':'무례한 사람',
        'nav_2':'벌레',
        'nav_3':'무기력한 무언가', 
        'nav_4':'습한 날씨', 
        'nav_5':'더러운 환경',
        'tmi_1':'MBTI:INTJ',
        'tmi_2':'나는야 취미 부자',
        'tmi_3':'강아지 키워요',
        'tmi_4':'영화관 좋아해요',
        'tmi_5':'잠이 많아요',
        'music':'Pink Sweat$ - Honesty(Remix)',
        'music_url' : '<iframe width="560" height="315" src="https://www.youtube.com/embed/L1Ja6Y8GvY8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
    },
    {
        'id': 5, 
        'name':'안정민', 
        'img_index':'static/images/index_jeong.JPG',
        'img_1':'images/jeong01.JPG',
        'img_2':'images/jeong01.JPG',
        'img_3':'images/jeong01.JPG',
        'man':'남자', 
        'birth':'1995.12.24', 
        'position':'팀원', 
        'fav_1':'노래', 
        'fav_2':'게임', 
        'fav_3':'OTT', 
        'fav_4':'여행', 
        'fav_5':'산책', 
        'nav_1':'여름',
        'nav_2':'더위',
        'nav_3':'물놀이', 
        'nav_4':'오만', 
        'nav_5':'선입견',
        'tmi_1':'MBTI:ISTP',
        'tmi_2':'예비역 하사에요',
        'tmi_3':'새벽을 좋아해요',
        'tmi_4':'야구장 많이가요',
        'tmi_5':'물을 무서워해요',
        'music':'YB(윤도현밴드) - 흰수염고래',
        'music_url' : '<iframe width="560" height="315" src="https://www.youtube.com/embed/nu3YsyDplUQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
    }
    

]

for a in members :
    id = a['id']
    name = a['name']
    img_index = a['img_index']
    img_1 = a['img_1']
    img_2 = a['img_2']
    img_3 = a['img_3']
    man = a['man']
    birth = a['birth']
    position = a['position']
    fav_1 = a['fav_1']
    fav_2 = a['fav_2']
    fav_3 = a['fav_3']
    fav_4 = a['fav_4']
    fav_5 = a['fav_5']
    nav_1 = a['nav_1']
    nav_2 = a['nav_2']
    nav_3 = a['nav_3']
    nav_4 = a['nav_4']
    nav_5 = a['nav_5']
    tmi_1 = a['tmi_1']
    tmi_2 = a['tmi_2']
    tmi_3 = a['tmi_3']
    tmi_4 = a['tmi_4']
    tmi_5 = a['tmi_5']
    music = a['music']
    music_url  = a['music_url']
    doc = {
        'id' : id,
        'name'  : name,
        'img_index' : img_index,
        'img_1' : img_1, 
        'img_2' : img_2,
        'img_3' : img_3, 
        'man' : man, 
        'birth' : birth, 
        'position' : position,
        'fav_1' : fav_1 ,
        'fav_2' : fav_2 ,
        'fav_3' : fav_3 ,
        'fav_4' : fav_4 ,
        'fav_5' : fav_5 ,
        'nav_1' : nav_1 ,
        'nav_2' : nav_2 ,
        'nav_3' : nav_3 ,
        'nav_4' : nav_4 ,
        'nav_5' : nav_5 ,
        'tmi_1' : tmi_1 ,
        'tmi_2' : tmi_2 ,
        'tmi_3' : tmi_3 ,
        'tmi_4' : tmi_4 ,
        'tmi_5' : tmi_5 ,
        'music' : music ,
        'music_url' : music_url
    }
 













