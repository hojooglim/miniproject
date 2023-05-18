from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://sparta:test@cluster0.8eblj3r.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/main')
def home():
   members = list(db.members.find({},{'_id':False}))
   return render_template('index.html',members=members)

@app.route('/comment')
def commentbook():
   members = list(db.members.find({},{'_id':False}))
   return render_template('comment.html',members=members)

@app.route('/main/member/<id>')
def member(id):
      
      member = list(db.members.find({},{'_id':False}))

      user = db.members.find_one({'id':int(id)})
      music_url = user['music_url']
      
      return render_template('member.html', members=member, user=user, music_url=music_url)

@app.route("/members", methods=["GET"])
def members_get():
    all_members = list(db.members.find({},{'_id':False}))
    return jsonify({'result': all_members})


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