from flask import Blueprint, render_template
from .schema import all_plantSchema, plantSchema, \
    connectorSchema, all_connectorSchema, sensorSchema, all_sensorSchema,\
        telemetrySchema, currentTelemetry

from .service import query_all, query_plant, getcurrent_telemetry_byplant
from .models import Plant, Telemetry, Connector, Sensor

exbp = Blueprint('api', __name__)

table_list = {
    'plant': Plant,
    'sensor': Sensor,
    'connector': Connector
}
@exbp.route('/plant/')
def plants():
    all = Plant.query.all()
    return all_plantSchema.dumps(all)

@exbp.route('/plant/<id>')
def get_plant(id):
    p = query_plant(id)
    return plantSchema.dumps(p)

@exbp.route('/connectors/<id>')
def conector_by_plant(id):
    c = Connector.query.filter_by(plant_id=id)
    return all_connectorSchema.dumps(c)

@exbp.route('/connector/<id>')
def get_connector(id):
    c = Connector.query.filter_by(connector_id=id).first()
    return connectorSchema.dumps(c)

@exbp.route('/telemetry/current/<id>')
def get_current_data(id):
    s = getcurrent_telemetry_byplant(id)
    return telemetrySchema.dumps(s)
