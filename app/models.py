
from app import db
import uuid
from datetime import datetime
from dataclasses import dataclass



@dataclass
class UuidModel(db.Model):
    id: int
    uuid_: str
    timestamp: datetime
    
    id = db.Column(db.Integer, primary_key =True)
    uuid_ = db.Column(db.String, nullable = False, default=str(uuid.uuid4()))
    timestamp = db.Column(db.DateTime, nullable= False, default=datetime.now())