from flask import Flask, render_template, request
  

app = Flask(__name__, static_folder='static')
  
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/video',methods=['POST'])
def video():
    if request.method=="POST":
        return render_template('index.html')

  

if __name__ == '__main__':
    app.run(debug=True)