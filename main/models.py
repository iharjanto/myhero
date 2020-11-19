from datetime import datetime
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()


class Plant(db.Model):
    __tablename__ = "plant"

    plant_id = db.Column(db.Integer, primary_key = True)
    nama = db.Column(db.String)
    def __repr__(self):
        return "<Plant '{}'>".format(self.nama)

class Connector(db.Model):
    __tablename__ = "connector"
    connector_id = db.Column(db.Integer, primary_key = True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plant.plant_id'))
    plant = db.relationship('Plant', backref='connectors')
    nama = db.Column(db.String)
    tipe = db.Column(db.String)
    port = db.Column(db.String)
    baudrate = db.Column(db.Integer, default = 9600)
    method = db.Column(db.String)
    ismodbus = db.Column(db.Boolean, default = False)

    def __repr__(self):
        return "<Connector '{}'>".format(self.nama)
    

class Sensor(db.Model):
    __tablename__ = "sensor"
    sensor_id = db.Column(db.Integer, primary_key = True)
    nama = db.Column(db.String)
    functioncode = db.Column(db.Integer)
    address = db.Column(db.Integer)
    connector_id = db.Column(db.Integer, db.ForeignKey("connector.connector_id"))
    connector = db.relationship("Connector", backref= 'sensors')
    unit = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return "<Sensor '{}'>".format(self.nama)

class Telemetry(db.Model):
    __tablename__ = "telemetry"
    tele_id = db.Column(db.Integer, primary_key = True)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.sensor_id'))
    sensor=db.relationship('Sensor', backref='datatelemetry')
    value=db.Column(db.Float,nullable=True)
    status=db.Column(db.Boolean, nullable=True)
    timestamp=db.Column(db.DateTime, default = datetime.now() )
    def __repr__(self):
        return "<Telemetry : {} '{}'>".format(self.sensor_id, self.value)