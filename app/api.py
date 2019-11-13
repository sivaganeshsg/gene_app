from flask import request, jsonify, Blueprint
import re
from .model import fetch_genes, genes_schema

bp = Blueprint('api', __name__)


@bp.route("/genes", methods=["GET"])
def search_genes():

    status_code = 200
    error = False
    response_messages = []

    lookup = request.args.get('lookup')
    # Optional
    species = request.args.get('species')
    # Optional
    page_num = request.args.get('page_num')

    lookup_validation = lookup_validator(lookup)
    if lookup_validation['error']:
        error = lookup_validation['error']
        status_code = lookup_validation['status_code']
        response_messages.append(lookup_validation['error_message'])

    species_validation = species_validator(species)
    do_species_filter = species_validation['do_species_filter']
    if species_validation['error']:
        error = species_validation['error']
        status_code = species_validation['status_code']
        response_messages.append(species_validation['error_message'])

    page = get_page_number(page_num)

    if not error:
        response_data = fetch_genes(lookup, do_species_filter, species, page)
        gene_data = genes_schema.dump(response_data.items)
        result = {"current_page": response_data.page, "total_page": response_data.pages,
                  "total_matches_found": response_data.total, "gene_result": gene_data}
    else:
        result = {"messages": response_messages}

    return jsonify(result), status_code


def lookup_validator(lookup):
    # Input validator for string/number/special_chars like "_"/"-"
    error = False
    status_code = 200
    error_message = None
    if (lookup is None) or (len(lookup) < 3) or (not re.match(r'^[A-Za-z0-9_-]+$', lookup)):
        error = True
        status_code = 422
        error_message = "The lookup should contain only Alphanumeric character and should contain at least 3 characters"
    return {'error': error, 'status_code': status_code, 'error_message': error_message}


def species_validator(species):
    # Input validator for string/number/special_chars like "_"/"-"
    error = False
    status_code = 200
    error_message = None
    do_species_filter = False
    if (species is not None) and (len(species) > 0):
        if re.match(r'^[A-Za-z0-9_-]+$', species):
            do_species_filter = True
        else:
            error = True
            status_code = 422
            error_message = "The Species should contain only Alphanumeric character and underscores"
    return {'error': error, 'status_code': status_code, 'error_message': error_message, 'do_species_filter': do_species_filter}


def get_page_number(page_num):
    page = 1
    if (page_num is not None) and (page_num.isdigit()) and (page_num >= "0"):
        page = int(page_num)
    return page
