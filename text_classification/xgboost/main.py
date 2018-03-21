#!/usr/bin/python
import xgboost as xgb

#
# start
#

# set tran parameters
train_file = './data_ok/ctrain.svm.txt'
valid_file = './data_ok/cvalid.svm.txt'
test_file = './data_ok/test.svm.txt'
param = dict()
param['max_depth'] = 5
param['max_leaf_nodes'] = 50
param['eta'] = 0.2
param['silent'] = 1
param['objective'] = 'binary:logistic';
param['nthread'] = 4
param['eval_metric'] = 'auc'
num_round = 400

# read train, valid and test data
dtrain = xgb.DMatrix(train_file)
dvalid = xgb.DMatrix(valid_file)
dtest = xgb.DMatrix(test_file)
evallist = [(dtrain, 'train'), (dvalid,'valid')]

# start training
bst = xgb.train(param, dtrain, num_round, evallist)
bst.save_model('0001.model')
# bst.dump_model('dump.raw.txt')

# start predicting
ypred = bst.predict(dtest)
f = file("ypred.out", "w")
for y in ypred :
    f.write("%f\n" % y)
