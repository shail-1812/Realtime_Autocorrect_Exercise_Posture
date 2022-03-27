from flask import Flask, request, jsonify, render_template,send_from_directory
from ray import method
import json
from calculations import get_Score



app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getSitUp')
def getSitUp():
    return render_template('situp.html')

@app.route('/getPunch')
def getPunch():
    return render_template('punch.html')

@app.route("/uploadFile", methods = ['POST'])
def uploadFile():
   if request.method == 'POST':
      #print(json.loads(request.form.get('actionType')))
      a = request.form.get('actionType')
      print(a)
      f = request.files['file']
      f.save(f.filename)
      print("Inside method")
      action = "situp - side"
      lookup = "lookup_test.pickle"
      video = f.filename

      g = get_Score(lookup)

      final_score,score_list = g.calculate_Score(video,action)
      print(final_score)
      print(score_list)

      return render_template('viewResult.html',join_video='joint.mp4', uploaded_video=f.filename,final_score=final_score,score_list=score_list)

if __name__ == "__main__":
    app.run(debug=True)
