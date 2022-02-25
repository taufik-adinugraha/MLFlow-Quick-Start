# Quick Start

## install packages
- [anaconda](https://www.anaconda.com/products/individual)
- [git](https://git-scm.com/download/)
- [docker](https://www.docker.com/products/docker-desktop)

## setup environment
    conda create -n mlops python=3.7
    conda activate mlops

## install python dependencies
    pip install -r requirements.txt
    pip install -f http://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py.html h2o

## initiate project
    mkdir mlflow_quick
    cd mlflow_quick
    git init .

## create training script
- code examples:
    - sklearn ([script](https://github.com/taufik-adinugraha/mlflow-quick-start/blob/main/train_sklearn.py))
    - tensorflow ([script](https://github.com/taufik-adinugraha/mlflow-quick-start/blob/main/train_tensorflow.py))
    - xgboost & lgbm ([notebook](https://github.com/taufik-adinugraha/mlflow-quick-start/blob/main/train_xgb_lgb.ipynb))
    - autoML with h2o ([notebook](https://github.com/taufik-adinugraha/mlflow-quick-start/blob/main/train_h2o_automl.ipynb))
- commit:

        git add *
        git commit -m 'first commit'
    
## run MLflow server
- open new terminal with the same environment and run the server

        mlflow server --backend-store-uri <URI> --default-artifact-root <URI> --host X.X.X.X --port 5000
  
  where \<URI\> can either be a HTTP/HTTPS URI for a remote server, or a local path to log data to a directory  
  example:
    
        mlflow server --backend-store-uri ./myml --default-artifact-root ./myml --host 0.0.0.0 --port 5000

- open the UI through web browser on `http://localhost:5000` or `http://X.X.X.X:5000`

## training
- run scripts:
           
        python train_sklearn.py
     ![ui_image](images/mlflow-autoML.png)
    
        python train_tensorflow.py

- run notebooks: 

     ![ui_image](images/mlflow-gbt.png)

## deployment
- local REST API server

        mlflow models serve -m /path_to_model/ -h X.X.X.X -p port_number
    
    example:
    
        mlflow models serve -m /path_to_model/ -h 0.0.0.0 -p 1234

- docker
    - build doker image
    
            mlflow models build-docker -m /path_to_model/ -n image_name 

      example:
      
            mlflow models build-docker -m /path_to_model/ -n image_name 
            
    - run docker container

            docker run -p 8080:8080 image_name

## test the endpoint

    curl -X POST -H "Content-Type:application/json; format=pandas-split" --data json_data http://X.X.X.X:portnumber/invocations

example:

    curl -X POST -H "Content-Type:application/json; format=pandas-split" --data '{"columns":["alcohol", "chlorides", "citric acid", "density", "fixed acidity", "free sulfur dioxide", "pH", "residual sugar", "sulphates", "total sulfur dioxide", "volatile acidity"],"data":[[12.8, 0.029, 0.48, 0.98, 6.2, 29, 3.33, 1.2, 0.39, 75, 0.66]]}' http://127.0.0.1:1234/invocations
    
    
