from flask_marshmallow import Marshmallow 
ms = Marshmallow()

class PlantSchema(ms.Schema):
    class Meta:
        fields = ('plant_id', 'nama')

plantSchema = PlantSchema()
all_plantSchema = PlantSchema(many = True)

class ConnectorSchema(ms.Schema):
    class Meta:
        fields = ('connector_id',
        'nama',
        'tipe',
        'port',
        'baudrate',
        'method')

connectorSchema = ConnectorSchema()
all_connectorSchema = ConnectorSchema(many = True)

class SensorSchema(ms.Schema):
    class Meta:
        fields = ('nama', 'sensor_id')

sensorSchema = SensorSchema()
all_sensorSchema = SensorSchema(many = True)

class TelemetrySchema(ms.Schema):
    class Meta:
        fields = ('nama','timestamp','value')

currentTelemetry = TelemetrySchema()
telemetrySchema = TelemetrySchema(many = True)
