import os 
import sys 
import pandas as pd
from logger import logging
from utils import save_object
from utils import evaluate_model
from dataclasses import dataclass
from exception import CustomException

from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.ensemble import AdaBoostRegressor,RandomForestRegressor,GradientBoostingRegressor

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_arr,test_arr):
        try:
            logging.info('split training and test input data')
            x_train,x_test,y_train,y_test = (
                train_arr[:,:-1],
                test_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,-1]
            )

            models = {
                'LinearRegression()' : LinearRegression(),
                'KNeighborsRegressor()' : KNeighborsRegressor(),
                'DecisionTreeRegressor()' : DecisionTreeRegressor(),
                'AdaBoostRegressor()' : AdaBoostRegressor(),
                'RandomForestRegressor()' : RandomForestRegressor(),
                'CatBoostRegressor()' : CatBoostRegressor(),
                'GradientBoostingRegressor()' : GradientBoostingRegressor(),
                'XGBRegressor()' : XGBRegressor()
            }

            train_model_report,test_model_report = evaluate_model(x_train,y_train,x_test,y_test,models=models)
            train_model_report = pd.DataFrame(train_model_report.items(),columns=['Model','R2_score']).sort_values(by=['R2_score'],ascending=False)
            test_model_report = pd.DataFrame(test_model_report.items(),columns=['Model','R2_score']).sort_values(by=['R2_score'],ascending=False)

        
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj = test_model_report
            )
            logging.info('Best model found on both training and testing dataset')
           
            return test_model_report[:1]

        except Exception as e:
            raise CustomException(e,sys)

