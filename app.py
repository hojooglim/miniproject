from bson.json_util import dumps
from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://sparta:test@cluster0.8eblj3r.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/delete", methods=["POST"])
def member_delete():
    name_receive = request.form['name_give'] 
    db.members.delete_one({'name':name_receive})
    return jsonify({'msg': '삭제 되었습니다'})

@app.route("/update", methods=["POST"])
def update_post():
      name_receive = request.form['name_give']
      img_index_receive = request.form['img_index_give']
      img_1_receive = request.form['img_1_give']
      img_2_receive = request.form['img_2_give']
      img_3_receive = request.form['img_3_give']
      man_receive = request.form['man_give']
      birth_receive = request.form['birth_give']
      position_receive = request.form['position_give']
      fav_1_receive = request.form['fav_1_give']
      fav_2_receive = request.form['fav_2_give']
      fav_3_receive = request.form['fav_3_give']
      fav_4_receive = request.form['fav_4_give']
      fav_5_receive = request.form['fav_5_give']
      nav_1_receive = request.form['nav_1_give']
      nav_2_receive = request.form['nav_2_give']
      nav_3_receive = request.form['nav_3_give']
      nav_4_receive = request.form['nav_4_give']
      nav_5_receive = request.form['nav_5_give']
      tmi_1_receive = request.form['tmi_1_give']
      tmi_2_receive = request.form['tmi_2_give']
      tmi_3_receive = request.form['tmi_3_give']
      tmi_4_receive = request.form['tmi_4_give']
      tmi_5_receive = request.form['tmi_5_give']
      music_receive = request.form['music_give']
      music_url_receive = request.form['music_url_give']
   
      db.members.update_one({'name':name_receive},{'$set':{'name':name_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'img_index':img_index_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'img_1':img_1_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'img_2':img_2_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'img_3':img_3_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'man':man_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'birth':birth_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'position':position_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'fav_1':fav_1_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'fav_2':fav_2_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'fav_3':fav_3_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'fav_4':fav_4_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'fav_5':fav_5_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'nav_1':nav_1_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'nav_2':nav_2_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'nav_3':nav_3_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'nav_4':nav_4_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'nav_5':nav_5_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'tmi_1':tmi_1_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'tmi_2':tmi_2_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'tmi_3':tmi_3_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'tmi_4':tmi_4_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'tmi_5':tmi_5_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'music':music_receive}})
      db.members.update_one({'name':name_receive},{'$set':{'music_url':music_url_receive}})

      return jsonify({'msg': '수정 되었습니다'})

@app.route('/main/member/update/<id>')
def update(id):
   members = list(db.members.find({},{'_id':False}))
   user = db.members.find_one({'id':int(id)})
   return render_template('update.html',members=members, user=user)

@app.route("/create", methods=["POST"])
def create_post():
      id_receive = request.form['id_give']
      name_receive = request.form['name_give']
      img_index_receive = request.form['img_index_give']
      img_1_receive = request.form['img_1_give']
      img_2_receive = request.form['img_2_give']
      img_3_receive = request.form['img_3_give']
      man_receive = request.form['man_give']
      birth_receive = request.form['birth_give']
      position_receive = request.form['position_give']
      fav_1_receive = request.form['fav_1_give']
      fav_2_receive = request.form['fav_2_give']
      fav_3_receive = request.form['fav_3_give']
      fav_4_receive = request.form['fav_4_give']
      fav_5_receive = request.form['fav_5_give']
      nav_1_receive = request.form['nav_1_give']
      nav_2_receive = request.form['nav_2_give']
      nav_3_receive = request.form['nav_3_give']
      nav_4_receive = request.form['nav_4_give']
      nav_5_receive = request.form['nav_5_give']
      tmi_1_receive = request.form['tmi_1_give']
      tmi_2_receive = request.form['tmi_2_give']
      tmi_3_receive = request.form['tmi_3_give']
      tmi_4_receive = request.form['tmi_4_give']
      tmi_5_receive = request.form['tmi_5_give']
      music_receive = request.form['music_give']
      music_url_receive = request.form['music_url_give']
   
      doc = {
        'id' : int(id_receive),
        'name'  : name_receive,
        'img_index' : img_index_receive,
        'img_1' : img_1_receive, 
        'img_2' : img_2_receive,
        'img_3' : img_3_receive, 
        'man' : man_receive, 
        'birth' : birth_receive, 
        'position' : position_receive,
        'fav_1' : fav_1_receive ,
        'fav_2' : fav_2_receive ,
        'fav_3' : fav_3_receive ,
        'fav_4' : fav_4_receive ,
        'fav_5' : fav_5_receive ,
        'nav_1' : nav_1_receive ,
        'nav_2' : nav_2_receive ,
        'nav_3' : nav_3_receive ,
        'nav_4' : nav_4_receive ,
        'nav_5' : nav_5_receive ,
        'tmi_1' : tmi_1_receive ,
        'tmi_2' : tmi_2_receive ,
        'tmi_3' : tmi_3_receive ,
        'tmi_4' : tmi_4_receive ,
        'tmi_5' : tmi_5_receive ,
        'music' : music_receive ,
        'music_url' : music_url_receive
      }
      db.members.insert_one(doc)
      return jsonify({'msg': '생성 되었습니다'})

@app.route('/create')
def create():
   members = list(db.members.find({},{'_id':False}))
   return render_template('create.html',members=members)

@app.route('/')
def home():
   members = list(db.members.find({},{'_id':False}))
   return render_template('index.html',members=members)


@app.route('/main')
def main():
   members = list(db.members.find({},{'_id':False}))
   return render_template('index.html', members=members)


@app.route('/comment')
def commentbook():
   members = list(db.members.find({},{'_id':False}))
   return render_template('comment.html',members=members)


@app.route('/main/member/<id>')
def member(id):
      member = list(db.members.find({},{'_id':False}))
      user = db.members.find_one({'id':int(id)})
      return render_template('member.html', members=member, user=user)


@app.route("/members", methods=["GET"])
def members_get():
    member = list(db.members.find({},{'_id':False}))
    return jsonify({'result': member})


@app.route("/guestbook", methods=["POST"])
def guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
       'name' : name_receive,
       'comment' : comment_receive
    }
    db.book.insert_one(doc)
    return jsonify({'msg': 'POST 연결 완료!'})


@app.route("/guestbook", methods=["GET"])
def guestbook_get():
    all_book = list(db.book.find({},{'_id':False}))
    return jsonify({'result': all_book})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5002, debug=True)






@app.route('/member-1')
def member_1():
   return render_template('member-1.html')