from config import db,func

class Dojo(db.Model):	
    __tablename__ = "dojos"
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(45))
    city = db.Column(db.String(45))
    state = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())   
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class Ninja(db.Model):
    __tablename__ = "ninjas"	
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())   
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    student_id = db.Column(db.Integer,db.ForeignKey("dojos.id"),nullable = False)
    student = db.relationship('Dojo',foreign_keys=[student_id],backref="dojo_ninjas",cascade = "all")