# Quick Start

## setup environment
    conda create -n mlops python=3.7
    conda activate mlops

## install dependencies
    pip install mlflow
    pip install matplotlib
    pip install jupyter
    pip install scikit-learn
    pip install xgboost
    pip install lightgbm
    pip install tensorflow
    pip install future
    pip install -f http://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py.html h2o

## initiate project
    mkdir mlflow_quick
    cd mlflow_quick
    git init .

## create training script
code examples:
- autoML with sklearn classifiers ([code](https://github.com/taufik-adinugraha/mlflow-quick-start/blob/main/train_sklearn_autoML.py))
- XGBoost
- LGBM
- Tensorflow
commit:
    git add *
    git commit -m 'first commit'
    
## dashboard
- open new terminal with the same environment and run the ui inside project directory
     
      mlflow ui --backend-store-uri <URI>
  where \<URI\> can either be a HTTP/HTTPS URI for a remote server, or a local path to log data to a directory  
  - example for local path:
  
        mlflow ui --backend-store-uri ./myml
  - example for remote server:
        
        mlflow ui --backend-store-uri postgresql://URI
- open the ui through web browser
  - example for local path:
        
        http://127.0.0.1:5000
  - example for local server

        http://127.0.0.1:5000

## training
- run scripts:
           
        python train_sklearn.py
     ![ui_image](images/mlflow-autoML.png)
    
        python train_tensorflow.py

- run notebook: 

     ![ui_image](images/mlflow-gbt.png)
