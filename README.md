# IDS Project

## Running the project

The data used can be downloaded from https://www.kaggle.com/rocki37/open-university-learning-analytics-dataset.  
The data should be put into the `data` folder.  
First, the script named `create_database.py` should be executed to create a Sqlite database with extra helper columns. The Sqlite database is also used for queries over multiple big tables.  
All of the data cleaning and model logic is in `model_features.ipynb`. Because of the big database queries jupyter might require the `--NotebookApp.iopub_data_rate_limit=1.0e10` parameter for startup.
