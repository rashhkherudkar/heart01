from models.utils import HeartAttack
from flask import Flask,jsonify,render_template,request
import config


app = Flask(__name__)

@app.route("/")

def hello_flask():
    print("We are in Flask API")
    return render_template("index.html")
    
@app.route("/heart_pred",methods=["POST"])

def get_predicted():



    age= eval(request.form.get("age"))
    sex= eval(request.form.get("sex"))
    cp= eval(request.form.get("cp"))
    trestbp= eval(request.form.get("trestbp"))
    chol=eval(request.form.get("chol"))
    fbs= eval(request.form.get("fbs"))
    restecg=eval(request.form.get("restecg"))
    thalach= eval(request.form.get("thalach"))
    exang=eval(request.form.get("exang"))
    oldpeak=eval(request.form.get("oldpeak"))
    slope=eval(request.form.get("slope"))
    ca= eval(request.form.get("ca"))
    thal=eval(request.form.get("thal"))

    print("age,sex,cp,trestbp,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal\n",age,sex,cp,trestbp,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)

    Obj=HeartAttack(age,sex,cp,trestbp,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    result1= Obj.get_heart_prediction()
   
    return render_template("index.html",prediction=result1) 


if __name__ == "__main__":
    app.run(host="0.0.0.0",port = config.PORT_NUMBER, debug=True)