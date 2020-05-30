from flask import Flask,render_template
​
​
app = Flask(__name__)
​
@app.route('/')
def welcome():
​
    return (
         f"Welcome Energy Production API <br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/Landing<br/>"
        f"/api/v1.0/Comparison<br/>"
        f"/api/v1.0/Data<br/>"
        f"/api/v1.0/Visualization1<br/>"
        f"/api/v1.0/Visualization2<br/>"
        f"/api/v1.0/Visualization3<br/>"
        f"/api/v1.0/Visualization4<br/>"
​
    )
    
​
​
@app.route('/api/v1.0/Landing')
def home():
​
    return render_template('landing.html')
​
@app.route('/api/v1.0/Comparison')
def comparisons():
​
    return render_template('/comparisons.html')
​
@app.route('/api/v1.0/Data')
def data():
    
    return render_template('data.html')
​
@app.route('/api/v1.0/Visualization1')
def visualization1():
​
    return render_template('visualization1.html')
​
@app.route('/api/v1.0/Visualization2')
def visualization2():
​
    return render_template('visualization2.html')
​
@app.route('/api/v1.0/Visualization3')
def visualization3():
​
    return render_template('visualization3.html')
​
@app.route('/api/v1.0/Visualization4')
def visualization4():
​
    return render_template('visualization4.html')
​
​
if __name__ == '__main__':
    app.run(debug=True)
