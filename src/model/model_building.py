import pandas as pd
import numpy as np
from src.logger import logging
import yaml
import pickle
from sklearn.svm import LinearSVC

def load_data(file_path):
    try:
        df=pd.read_csv(file_path)
        logging.info("Data Loaded from %s",file_path)
        return df
    except pd.errors.ParserError as e:
        logging.error("failed to parse the csv file: %s",e)
        raise
    except Exception as e:
        logging.error("Unexcepted error occured while loaded the data : %s",e)
        raise

def train_model(X_train,y_train):
    try:
        clf = LinearSVC(C=0.7,loss='squared_hinge',max_iter=3000)
        clf.fit(X_train,y_train)
        logging.info("model trainning completed")
        return clf
    except Exception as e:
        logging.error("Error during model Training: %s",e)
        raise

def save_model(model,file_path):
    try:
        with open(file_path,"wb") as file:
            pickle.dump(model,file)
        logging.info("model saved to %s",file_path)
    except Exception as e:
        logging.error("Error occurred while saving the model: %s",e)
        raise

def main():
    try:
        train_data = load_data('./data/processed/train_bow.csv')
        X_train = train_data.iloc[: , :-1].values
        y_train = train_data.iloc[: , -1].values

        clf = train_model(X_train,y_train)
        save_model(clf,"models\model.pkl")
    except Exception as e:
        logging.error('Failed to complete the model building process: %s', e)
        print(f"Error: {e}")

if __name__ == '__main__':
    main()

