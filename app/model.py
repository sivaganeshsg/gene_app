from . import db, ma
from marshmallow import fields
from sqlalchemy.sql.expression import and_


class Gene(db.Model):
    __tablename__ = 'gene_autocomplete'
    stable_id = db.Column(db.String(128), primary_key=True)
    species = db.Column(db.String(255))
    display_label = db.Column(db.String(128))
    location = db.Column(db.String(60))

    def __init__(self, display_label, location, stable_id, species):
        self.display_label = display_label
        self.location = location
        self.stable_id = stable_id
        self.species = species


class GeneSchema(ma.Schema):
    ensembl_stable_id = fields.String(attribute="stable_id")
    gene_name = fields.String(attribute="display_label")
    location = fields.String()
    species = fields.String()


gene_schema = GeneSchema()
genes_schema = GeneSchema(many=True)
# Can be changed later or accepted part of the input parameter
items_per_page = 10


def fetch_genes(lookup, do_species_filter, species, page):
    filters = []

    if do_species_filter:
        filters.append(Gene.species == species)

    filters.append(Gene.display_label.ilike('%' + lookup + '%'))

    response_data = Gene.query.filter(and_(*filters)). \
        order_by(Gene.stable_id.asc()). \
        paginate(page, items_per_page, error_out=False)

    return response_data
