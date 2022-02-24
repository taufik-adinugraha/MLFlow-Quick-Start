import xgboost as xgb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, accuracy_score
import warnings
import mlflow

warnings.filterwarnings("ignore")

# connect to tracking URI
# URI can either be a HTTP/HTTPS URI for a remote server, or a local path to log data to a directory
mlflow.set_tracking_uri('./myml') 

# set experiment name to organize runs
experiment_name = 'iris'
mlflow.set_experiment(experiment_name)

# automatic logging allows us to log metrics, parameters, and models without the need for explicit log statements
mlflow.xgboost.autolog() 

# import some data to play with
data = load_iris()
x, y = data.data, data.target

# split data
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=123)
dtrain = xgb.DMatrix(x_train, label=y_train)
dval = xgb.DMatrix(x_val, label=y_val)


with mlflow.start_run():
    params = {
        "objective": "multi:softprob",
        "num_class": 3,
        "learning_rate": 0.01,
        "colsample_bytree": 0.6,
        "subsample": 0.6,
        "seed": 42,
    }
    train_params = {
        'num_boost_round': 500,
        'verbose_eval': 5,
        'early_stopping_rounds': 10,
    }
    # train model
    model = xgb.train(
        params,
        dtrain,
        evals=[(dtrain, 'train'), (dval, 'val')],
        **train_params,
    )

    # evaluate model
    y_proba = model.predict(dval)
    y_pred = y_proba.argmax(axis=1)
    auc = roc_auc_score(y_val, y_proba, multi_class='ovo')
    acc = accuracy_score(y_val, y_pred)

    # log metrics
    mlflow.log_metrics({"val_roc_auc": auc, "val_accuracy": acc})