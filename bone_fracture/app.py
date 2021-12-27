import random

from flask import Flask, render_template, request, jsonify
from .preprossing import PreProcessing
app = Flask(__name__, static_folder='static/assets', template_folder='templates')


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/upload/with/type', methods=['POST'])
def upload_with_bone_type(): # This will handel the bones with bone type
    image_files = request.files
    form_data = request.form.to_dict()
    list_of_images=[]
    for key,value in image_files.items():
        list_of_images.append({
            'image':value,
            'type':form_data.get('select_input_'+key.split("_")[-1])
        })
    list_of_images=[{'image':'base64','type':'humr',}]
    list_results=[]
    for image in list_of_images:
        preprocess_obj=PreProcessing(image.get('image'),image.get('type'))
        label= preprocess_obj.get_processed_image()
        list_results.append({'image':image.get('image'),'result':label})
    response = jsonify({
        'success': True,
        'html_value': True,
        'list_results':list_results
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/upload/without/type', methods=['POST'])
def upload_without_bone_type(): # This will handel the bones without bone type
    image_files = request.files
    response = jsonify({
        'success': True,
        'html_value': True,
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run()
