from inspect import Parameter
from flask import Flask, render_template, request
import symbl
  

app = Flask(__name__, static_folder='static')
  
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/video',methods=['POST'])
def video():
    conversation_object = symbl.Video.process_file(file_path="static/video_test.mp4")
    if request.method=="POST":
        return render_template('index.html', transcript=conversation_object.get_messages())
  

if __name__ == '__main__':
    app.run(debug=True)