from flask import Flask, render_template, url_for
from .views import main_views

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    app.register_blueprint(main_views.databp)    
    # @app.route('/input/')
    # def input_data():
    #     return render_template('input.html')

    # @app.route('/input/result/')
    # def ouput_data():
    #     return render_template('output.html')

    return app
