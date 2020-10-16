from flask import Flask
import common

app = Flask(__name__)
common.app = app

import basket.controller.order

if __name__ == "__main__":
    app.run()