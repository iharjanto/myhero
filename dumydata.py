plant = [
    {'nama':'Mesin Listrik2','plant_id':2},
    {'nama':'Mesin Listrik1','plant_id':1}
]
"""
plant_id = db.Column(db.Integer, db.ForeignKey('plant.plant_id'))
    plant = db.relationship('Plant', backref='connectors')
    nama = db.Column(db.String)
    tipe = db.Column(db.String)
    port = db.Column(db.String)
    baudrate = db.Column(db.Integer, default = 9600)
    method = db.Column(db.String)
    ismodbus = db.Column(db.Boolean, default = False)
"""
conn = [
    {'nama':'Konektor Modbus', 'tipe':'modbus', 'port':'/dev/ttyUSB0','baudrate':9600,'method':'rtu'},
    {'nama':'Konektor Serial', 'tipe':'serial', 'port':'/dev/ttyUSB1','baudrate':9600}
]

'''    
 sensor_id = db.Column(db.Integer, primary_key = True)
    nama = db.Column(db.String)
    functioncode = db.Column(db.Integer)
    address = db.Column(db.Integer)
    connector_id = db.Column(db.Integer, db.ForeignKey("connector.connector_id"))
    connector = db.relationship("Connector", backref= 'sensors')
    unit = db.Column(db.Integer, nullable = False)
 '''
sensor = [
    {
        'nama' :'SensorTemperatur', 
        'functioncode':4,
        'address':1000,
        'connector_id':1,
        'unit':1
        },
    {
        'nama' :'Sensor Level', 
        'functioncode':2,
        'address':1,
        'connector_id':1,
        'unit':1
        }
]

import random
from datetime import datetime
from .main.service import save_change
from .main.models import Telemetry

def randomdata(a,b):
    return random.random() + random.randrange(a,b)

def dumydata(count,id):
    for i in range(count):
        d = {
            'sensor_id':id,
            'value':randomdata(20,40),
            'timestamp': datetime.now()
        }
        t = Telemetry(**d) 
        save_change(t)

def st(count,id):
    for i in range(count):
        d = {
            'sensor_id':id,
            'value':randomdata(20,40),
            'timestamp': datetime.now()
        }
        t = Telemetry(**d) 
        save_change(t)

