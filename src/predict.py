# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 14:31:18 2020

@author: Admin
"""

# -*- coding: utf-8 -*-

import os
import pandas as pd
import numpy as np
from sklearn import metrics

import joblib

import slackbot

os.chdir(os.environ.get("WRK_DIR"))
TEST_DATA = os.environ.get('TEST_DATA')
MODEL = os.environ.get("MODEL")


def predict():
    df = pd.read_csv(TEST_DATA)
    test_idx = df["id"].values
    predictions =  None
    
    for FOLD in range(5):
        print(FOLD)
        df = pd.read_csv(TEST_DATA)
        encoders = joblib.load(os.path.join("./models/" , f"{MODEL}_{FOLD}_label_encoder.pkl"))
        columns =joblib.load(os.path.join("./models/" ,f"{MODEL}_{FOLD}_columns.pkl"))
        for col in encoders:
            lbl = encoders[col]
            df.loc[:,col] = lbl.transform(df[col].values.tolist())
        
        
        #data is ready to train
        clf = joblib.load(os.path.join("./models/" , f"{MODEL}_{FOLD}.pkl"))
        df =df[columns]
        preds = clf.predict_proba(df)[: , 1]
        #score = metrics.roc_auc_score(df.target.values, preds)
        if(FOLD == 0):
            predictions = preds
            print(predictions)
        else:
            predictions += preds
           # predictions = preds + predictions
            
    predictions/=5
    sub =pd.DataFrame(np.column_stack((test_idx , predictions)) , columns=["id" ,"target"])
    return sub
    
if __name__ == "__main__":
    submission = predict()
    submission['id'] = submission['id'].astype(int)
    submission.to_csv(f"./models/{MODEL}.csv" , index=False)
    slackbot.sendNotification("SUBMISSION FILE CREATED(KAGGLE)" ,  ":)")