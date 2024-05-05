from flask import Flask,request,render_template,url_for
import numpy as np
import pandas as pd
import joblib as joblib

model = joblib.load(r'C:\Users\T.B\Desktop\Deploy\gemstone_model.pkl')
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        carat = float(request.form['carat'])
        cut = request.form['cut']
        color = request.form['color']
        clarity = request.form['clarity']

        depth = float(request.form['depth'])
        table = float(request.form['table'])
        x = float(request.form['x'])
        y = float(request.form['y'])
        z = float(request.form['z'])
        input_data = pd.DataFrame({
            'carat': [carat],
            'cut': [cut],
            'color': [color],
            'clarity': [clarity],
            'depth': [depth],
            'table': [table],
            'x': [x],
            'y': [y],
            'z': [z]
        })

        prediction = model.predict(input_data)
        print(prediction)

    return render_template('index.html', prediction=prediction)

if __name__=='__main__':
    app.run(debug=True)