from datetime import datetime
import pytz as tz
import pdb
from flask import Flask

app = Flask(__name__)

TZ = dict(NY  = tz.timezone('America/New_York'),
          ZRH = tz.timezone('Europe/Zurich'),
          LDN = tz.timezone('Europe/London'),
          JPY = tz.timezone('Asia/Tokyo'))

TIME_FORMAT = "%Y:%m:%d %H:%M:%S"

@app.route('/time')
def get_current_time():
    return {k: datetime.now(v).strftime(TIME_FORMAT) for k, v in TZ.items()}
