#!/usr/bin/env python
import pandas as pd
import numpy as np


fds = pd.read_csv("../../Data/edit/short_wide.csv")
  
train, test, validate = np.split(fds.sample(frac=1), [int(.6*len(fds)), int(.8*len(fds))])

train.to_csv("train_data.csv")
test.to_csv("test_data.csv")
validate.to_csv("validate_data.csv")
