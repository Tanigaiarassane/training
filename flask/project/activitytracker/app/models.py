from datetime import datetime
from app import  db

class ActivityItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable= False, unique = True)
    content = db.Column(db.Text, nullable = False)
    status = db.Column(db.String(10), nullable = False, default= "New")
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, name, content,status):
        self.name = name
        self.content = content
        self.status = status

    def __repr__(self):
        return "ActivityItem({},{},{},{}".format(self.name, self.content,self.status, self.date_created)




