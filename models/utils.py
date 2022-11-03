import pickle
import json
import numpy as np
import pandas as pd
import config

class HeartAttack():
    def __init__(self,age,sex,cp,trestbp,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):

        self.age= age
        self.sex= sex
        self.cp= cp
        self.trestbp= trestbp
        self.chol= chol
        self.fbs= fbs
        self.restecg= restecg
        self.thalach= thalach
        self.exang= exang
        self.oldpeak= oldpeak
        self.slope= slope
        self.ca= ca
        self.thal= thal

    def load_model(self):
        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data=json.load(f)

        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model=pickle.load(f)

    def get_heart_prediction(self):
        self.load_model()

        array=np.zeros(len(self.json_data["column_names"]))

        array[0]=self.age
        array[1]=self.sex
        array[2]=self.cp
        array[3]=self.trestbp
        array[4]=self.chol
        array[5]=self.fbs
        array[6]=self.restecg
        array[7]=self.thalach
        array[8]=self.exang
        array[9]=self.oldpeak
        array[10]=self.slope
        array[11]=self.ca
        array[12]=self.thal

        print("Array ::",array )

        result=self.model.predict([array])[0]
        
        result1 = "You have symptoms of Heart attack" if result == 1 else "You are healthy♥♥ \n  thank you!!"

        return result1

if __name__ == "__main__":
    age= 63.0
    sex= 1.0
    cp= 3.0
    trestbp= 145.0
    chol= 233.0
    fbs= 1.0
    restecg= 0.0
    thalach= 150.0
    exang= 0.0
    oldpeak= 2.3
    slope= 0.0
    ca= 0.0
    thal= 1.0

    Obj = HeartAttack(age,sex,cp,trestbp,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    output = Obj.get_heart_prediction()
    print(output)