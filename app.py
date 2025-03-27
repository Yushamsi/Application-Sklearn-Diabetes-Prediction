from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load('diabetes_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract data from form
        data = [float(request.form.get('feature'+str(i))) for i in range(10)]
        
        # Make prediction
        prediction = model.predict([data])[0]
        
        return render_template('index.html', result=prediction)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
