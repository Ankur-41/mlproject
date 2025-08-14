import os 
import sys
import dill

import numpy as np 
import pandas as pd

from sklearn.metrics import r2_score
from exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    

def evaluate_model(x_train,y_train,x_test,y_test,models):
    try:
        train_report = {}
        test_report = {}
        best_model = None
        best_score = float('-inf')
        for name,model in models.items():
            model.fit(x_train,y_train)
            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)
            train_score = r2_score(y_train,y_train_pred)
            test_score = r2_score(y_test,y_test_pred)

            train_report[name] = train_score
            test_report[name] = test_score

            if test_score > best_score:
                best_score = test_score
                best_model = model

        return train_report,test_report,best_model
    except Exception as e:
        raise CustomException(e,sys)
    
def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)


