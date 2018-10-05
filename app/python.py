#https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from sqlalchemy import Boolean, Column, DateTime, Integer, Numeric, String, Text, text

app = Flask(__name__)

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Data(db.Model):
    __tablename__ = 'db_integration__hackathon_team_external_db'
    id = db.Column(Integer, primary_key=True, server_default=text("nextval('db_integration__hackathon_team_external_db_id_seq'::regclass)"))
    device_id = db.Column(Integer)
    device_name = db.Column(Text)
    device_group_id = db.Column(Integer)
    device_group_name = db.Column(Text)
    device_otaa_dev_eui = db.Column(String(16))
    device_otaa_app_eui = db.Column(String(16))
    device_session_id = db.Column(Integer)
    device_session_dev_addr = db.Column(String(8))
    device_session_frame_count_up = db.Column(Integer)
    device_session_frame_count_down = db.Column(Integer)
    gateway_id = db.Column(Integer)
    gateway_eui = db.Column(String(16))
    gateway_name = db.Column(Text)
    gateway_latitude = db.Column(Numeric)
    gateway_longitude = db.Column(Numeric)
    gateway_altitude = db.Column(Numeric)
    port = db.Column(Integer)
    confirmed = db.Column(Boolean)
    payload_raw = db.Column(String(1024))
    payload_fields = db.Column(String(1024))
    reception_time = db.Column(DateTime(True))
    reception_rssi = db.Column(Integer)
    reception_snr = db.Column(Numeric)
    receptions_count = db.Column(Integer)
    receptions_json = db.Column(Text)
    frequency = db.Column(Integer)
    modulation = db.Column(Text)
    data_rate = db.Column(Text)
    coding_rate = db.Column(Text)
    p_x3 = db.Column(Text)
    p_x4 = db.Column(Text)
    p_index = db.Column(Text)
    p_cmd = db.Column(Text)
    p_bus_addr = db.Column(Text)
    p_msg_id = db.Column(Text)
    p_x1 = db.Column(Text)
    p_x2 = db.Column(Text)


class DataSchema(ma.Schema):
    class Meta:
        model = Data

data_schema = DataSchema()

# endpoint to show all users
@app.route("/getData", methods=["GET"])
def get_data():
    device = Data(device_id='14')
    return jsonify(data_schema.dump(device).data)

if __name__ == '__main__':
    app.run(debug=True)
