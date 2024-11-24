# Performance of General Practices in North Central London

A project exploring the variation in the performance of general practices in North Central London using publically available data from NHS Digital (NHSD), the Care Quality Commission (CQC) and Public Health England (PHE).

## Setup

To set up a virtual environment for the project, please run the following commands in the command line:
```cmd
> python -m venv .venv
> .\.venv\Scripts\activate.bat
> python -m pip install -r requirements.txt
```

## Running the Pipeline

The pipeline can be run using the jupyter notebook `main.ipynb`. 
Make sure the notebook is connected to the virtual environment before executing any code cells.
Code is shown alongside markdown documentation explaining each step in the process.

## Project Structure

The project is structured as follows:
```
.
├── data                    Folder to store input data
├── outputs                 Folder to store code outputs (visualisations etc)
├── src                     Source code for the project
│   ├── parameters.py       Parameters defining performance metrics to consider
│   ├── utils.py            Useful functions
├── main.ipynb              Main notebook to run the pipeline
├── README.md               This file
├── requirements.txt        Packages used by the project
└──setup.py                 Sets up the project as a python package
```

