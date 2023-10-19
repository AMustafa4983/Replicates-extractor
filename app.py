# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request, render_template, url_for, redirect
  
from gpt.generator import generate_item, suggest_item, clean_items
from pipeline.splitter import split_sections, split_sections_by_length
from pipeline.cleaner import clean_english_text
import json

# creating a Flask app
app = Flask(__name__)
  

@app.route('/')
def index():
    return render_template('submit.html')


@app.route('/submit', methods = ['POST'])
def submit():

    if 'file' not in request.files:
        return jsonify({'error' : 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error' : 'No selected file'})
    
    if file and file.filename.endswith('.txt'):
        text = file.read().decode('utf-8')
    
    try:
        sections = split_sections(text)
        if len(sections) == 1:
            sections = split_sections_by_length(text)
        
        text = clean_english_text(sections[1])
        if len(text) > 4097:
            text = text[:3950]

    except ValueError:
        return jsonify({'error' : f"No text sent!\n{ValueError}"})
    
    try:
        
        res = generate_item(text)
    except:
        if len(text) > 4097:
            return jsonify({'error' : f"Text has more than 4097 token"})
        else:
            return jsonify({'error' : f"Bad predictions with generated list!"})
    
    try:
        items = res.choices[0].message.content
        items = json.loads(items)
    except:
        return jsonify({'error' : f"Failed to convert string to json!"})

    try:
        res = suggest_item(res.choices[0].message.content)
        items['Suggested'] = json.loads(res.choices[0].message.content)['Suggested']
        
        res = clean_items(items)
        items = json.loads(res.choices[0].message.content)
        
        return render_template('submit.html', materials=items['Materials'], suggested=items['Suggested'], suppliers=items['Suppliers'])
    
    except:
        return jsonify({'error' : f"Bad predictions with Suggested list!"})

  

if __name__ == '__main__':
  
    app.run(debug = True, host='0.0.0.0', port=5000)
