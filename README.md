# Performance of General Practices in North Central London

A project exploring the variation in the performance of general practices in North Central London using publically available data from NHS Digital (NHSD), the Care Quality Commission (CQC) and Public Health England (PHE).

## Setup

To set up a virtual environment for the project, please run the following commands in the command line:
```cmd
> python -m venv .venv
> .\.venv\Scripts\activate.bat
> python -m pip install -r requirements.txt
```
Before running the pipeline please check the following:
1. Make sure the notebook is connected to the virtual environment before executing any code cells;
2. Create a folder called `data` containing the `task_dataset.csv` in the root directory of the project, as shown below. Or alter the file paths in `src/parameters.py` specifying the location of the dataset locally. 

## Running the Pipeline

The pipeline can be run using the jupyter notebook `main.ipynb`. 
Code is shown alongside markdown documentation explaining each step in the process.

## Project Structure

The project is structured as follows:
```
.
├── data                    Folder to store input data
│   ├── task_dataset.csv    GP level dataset (provided) including publically available statistics 
├── outputs                 Folder to store code outputs (visualisations etc)
├── src                     Source code for the project
│   ├── parameters.py       Parameters defining performance metrics to consider
│   ├── utils.py            Useful functions
├── main.ipynb              Main notebook to run the pipeline
├── README.md               This file
├── requirements.txt        Packages used by the project
└── setup.py                 Sets up the project as a python package
```

