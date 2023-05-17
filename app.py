from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://sparta:test@cluster0.8eblj3r.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/main')
def home():
   return render_template('index.html')

@app.route('/member-1')
def member_1():
   return render_template('member-1.html')

@app.route('/member-2')
def member_2():
   return render_template('member-2.html')

@app.route('/member-3')
def member_3():
   return render_template('member-3.html')

@app.route('/member-4')
def member_4():
   return render_template('member-4.html')

@app.route('/comment')
def commentbook():
   return render_template('comment.html')


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
   app.run('0.0.0.0', port=5001, debug=True)