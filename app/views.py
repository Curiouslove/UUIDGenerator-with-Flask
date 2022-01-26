from app import app, db
from app.models import UuidModel
from flask import jsonify
from collections import OrderedDict


@app.route("/")
def index():
    uuid_ = UuidModel()
    db.session.add(uuid_)
    db.session.commit()

    data = UuidModel.query.all()

    data = {str(d.timestamp): d.uuid_ for d in reversed(data)}
    

    return data

