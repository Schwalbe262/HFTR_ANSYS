import pandas
import pycaret

filename = "Data_v1.csv"

csv = pandas.read_csv(filename)
csv = csv.dropna(axis=0).reset_index(drop=True)#drop NaN

csv = csv.drop('Lmt',axis=1)
csv = csv.drop('Lmr',axis=1)
csv = csv.drop('Llk',axis=1)
#csv = csv.drop('Rt',axis=1)
csv = csv.drop('Rr',axis=1)

dataset = csv

data = dataset.sample(frac=0.7, random_state=786).reset_index(drop=True)
data_unseen = dataset.drop(data.index).reset_index(drop=True)

from pycaret.regression import *
exp_reg101 = setup(data = data, target = 'Rt', session_id=123, silent=True) 

top3 = compare_models(n_select = 3) 

tuned_top3 = [tune_model(i) for i in top3]

bagged_top3 = [ensemble_model(i) for i in tuned_top3]

blender = blend_models(estimator_list = top3)

best4 = automl(optimize = 'RMSE')
