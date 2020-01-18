# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:59:24 2020

@author: Admin
"""

import os
import sys

os.environ['WRK_DIR'] = 'D:/Utham/ML_proj/categorical_encoding/'
os.environ['TRAINING_DATA'] = 'D:/Utham/ML_proj/categorical_encoding/input/train_folds.csv'
os.environ['TEST_DATA'] = 'D:/Utham/ML_proj/categorical_encoding/input/test.csv'
os.environ['FOLD'] = sys.argv[2]
os.environ["MODEL"] = sys.argv[1]