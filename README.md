# Quick Tutorial

<p align="center">
  <img src=images/mlflow-components.png alt="drawing" width="700"/>
</p>

## 1. Setup
### Optional Packages
- [anaconda](https://www.anaconda.com/products/individual) (environment manager)
- [git](https://git-scm.com/downloads) (version control)
- [docker](https://www.docker.com/products/docker-desktop) (container manager)
- [java](https://www.java.com/download/ie_manual.jsp) (required for running H2O)

### Environment
example:

    conda create -n mlops python=3.7
    conda activate mlops

### Download or Clone The Tutorial

    git clone https://github.com/taufik-adinugraha/mlflow-tutorial.git
    cd mlflow-tutorial

### Python Dependencies
    pip install -r requirements.txt
    pip install -f http://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py.html h2o


## 2. MLflow Tracking
MLflow Tracking is an open-source API for live logging of parameters, metrics, and metadata when running a machine learning code. It provides valuable information and visibility that enables you to monitor the progress of the training process and take action if necessary.

<p align="center">
  <img src=images/mlflow-tracking.png alt="drawing" width="500"/>
</p>

### Training Scripts
- sklearn ([script](https://github.com/taufik-adinugraha/mlflow-quick-start/blob/main/train_sklearn.py))
- tensorflow ([script](https://github.com/taufik-adinugraha/mlflow-quick-start/blob/main/train_tensorflow.py))
- xgboost & lgbm ([notebook](https://github.com/taufik-adinugraha/mlflow-quick-start/blob/main/train_xgb_lgb.ipynb))
- autoML with H2O ([notebook](https://github.com/taufik-adinugraha/mlflow-quick-start/blob/main/train_h2o_automl.ipynb))
    
### Run MLflow Server
- open new terminal/console with the same environment and run the server

        mlflow server --backend-store-uri <URI> --default-artifact-root <URI> --host X.X.X.X --port port_number
  
  where \<URI\> can either be a database server, or a local path to log data to a directory.
  
  example when using local directory *myml*:
    
        mlflow server --backend-store-uri ./myml --default-artifact-root ./myml --host 0.0.0.0 --port 5000

- open the UI through web browser on `http://localhost:5000` or `http://X.X.X.X:5000`

### Training
- run ***train_sklearn.py***:
           
        python train_sklearn.py
     ![sklearn](images/mlflow-sklearn.png)

- run ***train_tensorflow.py***:

        python train_tensorflow.py
     ![sklearn](images/mlflow-tensorflow.png)
     ![sklearn](images/mlflow-tensorflow-architecture.png)
     ![sklearn](images/mlflow-tensorflow-metrics.png)

- run ***train_xgb_lgb.ipynb***: 

     ![xgblgb](images/mlflow-gbt.png)

- run ***train_h2o_automl.ipynb*** (only save the best model): 

     ![sklearn](images/mlflow-h2o_autoML.png)
     ![sklearn](images/h2o_autoML_leaderboard.png)

## 3. MLflow Projects
An MLflow Project is a format for packaging data science code in a reusable and reproducible way, based primarily on conventions. In addition, the Projects component includes an API and command-line tools for running projects, making it possible to chain together projects into workflows.

<p align="center">
  <img src=images/mlflow-projects.png alt="drawing" width="500"/>
</p>

### Main Components:
- 'MLproject' config file [(example)](https://github.com/taufik-adinugraha/mlflow-run-example/blob/main/conda.yaml)
- code or script as an entry point [(example)](https://github.com/taufik-adinugraha/mlflow-run-example/blob/main/train_tensorflow.py)
- data source (csv or another source)

### Run Example:
    
    export MLFLOW_TRACKING_URI='/home/mlflow-user/mlflow-run-example/myml'
    mlflow run https://github.com/taufik-adinugraha/mlflow-run-example.git --version=main --experiment-name=MNIST -P epochs=9 -P learning_rate=0.025

## 4. MLflow Models
An MLflow Model is a standard format for packaging machine learning models that can be used in a variety of downstream tools—for example, real-time serving through a REST API or batch inference on Apache Spark. The format defines a convention that lets you save a model in different “flavors” that can be understood by different downstream tools.

<p align="center">
  <img src=images/mlflow-models.png alt="drawing" width="500"/>
</p>

### Model Deployment
- REST API Server

        mlflow models serve -m /path_to_model/ -h X.X.X.X -p port_number
    
    example:
    
        mlflow models serve -m myml/3/649571fc79bd4fedb78378aa11a583d4/artifacts/model -h 0.0.0.0 -p 1234

- Docker
    - build docker image
    
            mlflow models build-docker -m /path_to_model/ -n image_name 

      example:
      
            mlflow models build-docker -m myml/3/649571fc79bd4fedb78378aa11a583d4/artifacts/model -n my_model 
            
    - run docker container

            docker run -p 8080:8080 image_name

### Test The Endpoint

    curl -X POST -H "Content-Type:application/json; format=pandas-split" --data json_data http://X.X.X.X:portnumber/invocations

example:

    curl -X POST -H "Content-Type:application/json; format=pandas-split" --data '{"columns":["sepal length", "sepal width", "petal length", "petal width"],"data":[[5.1, 3.5, 1.4, 0.2]]}' http://localhost:1234/invocations
    
the response should be similar to this:

    [[0.9854555235937683, 0.009577244786833805, 0.004967231619397863]]
    
    
## 5. MLflow Model Registry
The MLflow Model Registry component is a centralized model store, set of APIs, and UI, to collaboratively manage the full lifecycle of an MLflow Model. It provides model lineage (which MLflow experiment and run produced the model), model versioning, stage transitions (for example from staging to production), and annotations.

<p align="center">
  <img src=images/mlflow-registry.jpeg alt="drawing" width="500"/>
</p>

Not available in community version. [More info](https://www.mlflow.org/docs/latest/model-registry.html)
