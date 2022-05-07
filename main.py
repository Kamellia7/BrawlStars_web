from flask import Flask, render_template
from data import db_session
from data.brawler import User
import json

app = Flask(__name__)

db_session.global_init("db/blogs.db")


@app.route('/')
@app.route('/index')
def index():
    db_sess = db_session.create_session()
    slov = db_sess.query(User.name, User.href_img, User.name_rus).filter(User.rarity == "ordinary").all()
    sp = []
    for el in slov:
        sp.append({"name": el[0], "url": el[1], "name_r": el[2]})
    sp_f = []
    for i in range(0, len(sp), 3):
        if i + 3 <= len(sp) - 1:
            sp_f.append(sp[i:i + 3])
        else:
            sp_f.append(sp[i:])
    return render_template('index.html', slov=sp_f)


@app.route('/rare')
def rare():
    db_sess = db_session.create_session()
    slov = db_sess.query(User.name, User.href_img, User.name_rus).filter(User.rarity == "rare").all()
    sp = []
    for el in slov:
        sp.append({"name": el[0], "url": el[1], "name_r": el[2]})
    sp_f = []
    for i in range(0, len(sp), 3):
        if i + 3 <= len(sp) - 1:
            sp_f.append(sp[i:i + 3])
        else:
            sp_f.append(sp[i:])
            print(sp_f)
    return render_template('rare.html', slov=sp_f)


@app.route('/super_rare')
def super_rare():
    db_sess = db_session.create_session()
    slov = db_sess.query(User.name, User.href_img, User.name_rus).filter(User.rarity == "super_rare").all()
    sp = []
    for el in slov:
        sp.append({"name": el[0], "url": el[1], "name_r": el[2]})
    sp_f = []
    for i in range(0, len(sp), 3):
        if i + 3 <= len(sp) - 1:
            sp_f.append(sp[i:i + 3])
        else:
            sp_f.append(sp[i:])
            print(sp_f)
    return render_template('super_rare.html', slov=sp_f)


@app.route('/epic')
def epic():
    db_sess = db_session.create_session()
    slov = db_sess.query(User.name, User.href_img, User.name_rus).filter(User.rarity == "epic").all()
    sp = []
    for el in slov:
        sp.append({"name": el[0], "url": el[1], "name_r": el[2]})
    sp_f = []
    for i in range(0, len(sp), 3):
        if i + 3 <= len(sp) - 1:
            sp_f.append(sp[i:i + 3])
        else:
            sp_f.append(sp[i:])
            print(sp_f)
    return render_template('epic.html', slov=sp_f)


@app.route('/mythical')
def mythical():
    db_sess = db_session.create_session()
    slov = db_sess.query(User.name, User.href_img, User.name_rus).filter(User.rarity == "mif").all()
    sp = []
    for el in slov:
        sp.append({"name": el[0], "url": el[1], "name_r": el[2]})
    sp_f = []
    for i in range(0, len(sp), 3):
        if i + 3 <= len(sp) - 1:
            sp_f.append(sp[i:i + 3])
        else:
            sp_f.append(sp[i:])
            print(sp_f)
    return render_template('mythical.html', slov=sp_f)


@app.route('/legendary')
def legendary():
    db_sess = db_session.create_session()
    slov = db_sess.query(User.name, User.href_img, User.name_rus).filter(User.rarity == "leg").all()
    sp = []
    for el in slov:
        sp.append({"name": el[0], "url": el[1], "name_r": el[2]})
    sp_f = []
    for i in range(0, len(sp), 3):
        if i + 3 <= len(sp) - 1:
            sp_f.append(sp[i:i + 3])
        else:
            sp_f.append(sp[i:])
    return render_template('legendary.html', slov=sp_f)


@app.route('/chromatic')
def chromatic():
    db_sess = db_session.create_session()
    slov = db_sess.query(User.name, User.href_img, User.name_rus).filter(User.rarity == "xrom").all()
    sp = []
    for el in slov:
        sp.append({"name": el[0], "url": el[1], "name_r": el[2]})
    sp_f = []
    for i in range(0, len(sp), 3):
        if i + 3 <= len(sp) - 1:
            sp_f.append(sp[i:i + 3])
        else:
            sp_f.append(sp[i:])
    return render_template('chromatic.html', slov=sp_f)


@app.route('/<brawler>')
def brawler_info(brawler):
    db_sess = db_session.create_session()
    slov = db_sess.query(User.href_json, User.href_img).filter(User.name == brawler).all()
    if slov:
        with open(slov[0][0], encoding='utf-8') as file:
            data = json.load(file)
        data = data[0]
        name = data["name"]
        description = data["description"]
        attack = data["attack"]
        super = data["super"]
        amplification = data["amplification"]
        gadget = data["gadget"]
        return render_template('brawlers.html', name=name, description=description, attack=attack, superr=super,
                               amplification=amplification, gadget=gadget, img_href=slov[0][1])
    return "404"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
