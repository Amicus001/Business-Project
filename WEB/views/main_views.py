from flask import Blueprint, render_template, request


#bp instance
databp = Blueprint(name='DATA',
                   import_name= __name__,
                   static_folder= 'templates',
                   url_prefix='/input')


save_file_dir = '../static/model/data'
# routing functions

@databp.route('/') #http://127.0.0.1:5000/input
def input_data():
    return  render_template('input.html')







