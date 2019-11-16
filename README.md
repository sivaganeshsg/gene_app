# Gene App

## About

Gene App built on Flask allows users to search for a gene by its name.

The endpoint accepts the following parameters:

- lookup (required and minimum of 3 characters) - e.g. BRC 
- species (optional) - e.g. homo_sapiens
- page_num (optional) - e.g. 3


The endpoint returns the following response that matches the given lookup and species
- current_page
- total_matches_found
- total_page
- gene_result -  contains gene_name, location, ensembl_stable_id and species

The gene_result is limited to 10 per page and can be navigated by passing 'page_num' parameter.

### Prerequisites

You need have the following software to run the program

- Python 3
- Pip 3
- Git


### Code

To download the 'gene_app' codebase,

- Clone the repository via HTTPS or SSH

  HTTPS:

      git clone https://github.com/sivaganeshsg/gene_app.git

  SSH:

      git clone git@github.com:sivaganeshsg/gene_app.git

### Setup and Run

To setup and start the application, run the following script from the 'gene_app' directory

    ./setup.sh

The `setup.sh` file configures the virtual environment, installs the necessary packages from `requirements.txt` and executes `start.sh` to run the flask app. 
### Config and env file

All the configurations are declared in config.py while the `.env` contains the value such as Ensembl database details, SQLAlchemy Flag. Please note that the `.env` file should NEVER be shared on a repository for a real world application.   
