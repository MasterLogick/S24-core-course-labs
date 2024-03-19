from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """
    :return: Current Moscow time
    """
    mos_date_time = datetime.now(ZoneInfo("Europe/Moscow"))
    return mos_date_time.isoformat()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
