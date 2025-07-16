from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["meeting_reservation"]

@app.route('/users')
def show_users():
    users = list(db.users.find({}, {"_id": 0}))
    return render_template("users.html", users=users)

@app.route('/rooms')
def show_rooms():
    rooms = list(db.rooms.find({}, {"_id": 0}))
    return render_template("rooms.html", rooms=rooms)

from flask import request, redirect

@app.route('/reserve', methods=["GET", "POST"])
def reserve():
    if request.method == "POST":
        user_name = request.form["user_name"]
        room_name = request.form["room_name"]

        user = db.users.find_one({"name": user_name})
        room = db.rooms.find_one({"name": room_name})

        if not user or not room:
            return "사용자 또는 회의실을 찾을 수 없습니다.", 400

        reservation = {
            "user_id": user["_id"],
            "room_id": room["_id"],
            "start_time": request.form["start_time"],
            "end_time": request.form["end_time"],
            "status": "pending",
            "purpose": request.form["purpose"]
        }
        db.reservations.insert_one(reservation)
        return redirect("/reservations")

    users = list(db.users.find({}, {"_id": 0, "name": 1}))
    rooms = list(db.rooms.find({}, {"_id": 0, "name": 1}))
    return render_template("reserve.html", users=users, rooms=rooms)

@app.route('/reservations')
def show_reservations():
    reservations = list(db.reservations.find({}, {"_id": 0}))
    return render_template("reservations.html", reservations=reservations)

@app.route('/')
def index():
    return '''
    <h2>예약 시스템</h2>
    <p><a href="/users">[사용자 목록 보기]</a></p>
    <p><a href="/rooms">[회의실 목록 보기]</a></p>
    <p><a href="/reservations">[예약 목록 보기]</a></p>
    <p><a href="/reserve">[회의실 예약하기]</a></p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
