from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.neural_network import MLPClassifier

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

import warnings
import mlflow


warnings.filterwarnings("ignore")

# connect to tracking URI
# URI can either be a HTTP/HTTPS URI for a remote server, or a local path to log data to a directory
mlflow.set_tracking_uri('./myml') 

# set experiment name to organize runs
experiment_name = 'breast cancer'
mlflow.set_experiment(experiment_name)

# automatic logging allows us to log metrics, parameters, and models without the need for explicit log statements
mlflow.sklearn.autolog() 

# import some data to play with
data = load_breast_cancer()
x, y = data.data, data.target

# split data
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=123)

# list of models
models = [LogisticRegression(), DecisionTreeClassifier(), KNeighborsClassifier(), GaussianProcessClassifier(), \
GaussianNB(), SVC(), RandomForestClassifier(), AdaBoostClassifier(), GradientBoostingClassifier(), \
BaggingClassifier(KNeighborsClassifier()), HistGradientBoostingClassifier(), MLPClassifier()]

# loop over model
for model in models:
    with mlflow.start_run() as run:
        # train model
        model.fit(x_train, y_train)
        # evaluate model
        mlflow.sklearn.eval_and_log_metrics(model, x_val, y_val, prefix="val_")
