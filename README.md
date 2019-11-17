# Gene App

## About

Gene App built on Flask that allows users to search for a gene by its name where the data is retrieved from the Ensembl database `ensembl_website_97`.


The `genes` endpoint accepts the following parameters:

- lookup (required and minimum of 3 characters) - e.g. BRC 
- species (optional) - e.g. homo_sapiens
- page_num (optional) - e.g. 3

| Endpoint | Method | Parameter | Response |
| -------- |:------:| ---------:|---------:|
| genes    | GET    | lookup (req), species, page_num  |  current_page, total_page, gene_result, total_matches_found |

Each `gene_result` contains gene_name, location, ensembl_stable_id and species.

The gene_result is limited to 10 per page and can be navigated by passing `page_num` parameter.

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

---
## Request and Response:

### Sample Request
```http://127.0.0.1:5000/genes?lookup=BRC&species=anser_brachyrhynchus```

### Sample Response
```
{
    "current_page": 1,
    "gene_result": [
        {
            "ensembl_stable_id": "ENSABRG00000013131",
            "gene_name": "BRCA1",
            "location": "NXHY01000201.1:747323-771146",
            "species": "anser_brachyrhynchus"
        },
        {
            "ensembl_stable_id": "ENSABRG00000020312",
            "gene_name": "BRCC3",
            "location": "NXHY01000005.1:10133012-10137594",
            "species": "anser_brachyrhynchus"
        }
    ],
    "total_matches_found": 2,
    "total_page": 1
}
```
---

### Methodologies

- The application is built using modular, reusable code where applicable.
- The naming of the class, function, variable makes it easy to understand for fellow developers/team.
- During the development, the API is tested using Postman Client.
- The `lookup_validator` and `species_validator` function validates the input parameters, and appropriate HTTP status code is given to the client if the validation fails. As the helper function grows, we can move the functions it to a Utility/Helper class.
- The `.env` file contains all the database configuration. It allows the application to retrieve the appropriate configuration from the different environment (development/QA/staging/production) and the repository will never share the .env file.
- The query filter uses query chaining, making it easy to build complex queries.
- The application has an error handling mechanism to catch both client-side(404, 405) and server-side errors/exceptions. In terms of server-side errors and exception, it displays a generic error message to the user while the actual error message can be logged to a file/database/external logging service to identify the issue.

### Future Improvements
- The definition of items_per_page, regular expression can be moved to a file or a settings table in the database to make it easy to modify in one place.
- The `items_per_page` can be passed in the parameter to give more flexibility for the users - with higher items per page limitation(e.g. 1000) and default items per page.
- Define all the error code and corresponding error messages in a separate `error_lookup` table and retrieve the error messages dynamically, making the code cleaner. We can use this information in the documentation for developers to quickly identify the issue with the request based on the error code.
- To protect the application/database service from brute force or a client using the service in a way that affects other users, we can employ API rate limiters based on IP address or token-based API request.


## Task 2, 3, 4

Task about Deployment, Testing and Documentation can be found in [TASKS.md](TASKS.md)
