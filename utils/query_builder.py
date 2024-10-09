import sys
import os
from linkml.validator import validate
from utils.idr_connector import get_results, get_query_results,query_searchengine
from utils.generate_validate_json_image_data import logger, process_results, validate_data


schema_names={
        "organism":"organism_schema",
        "egen":"gene_schema",
        "phenotype": "phenotype_schema",
        "compound": "compound_schema",
        "pathology": "pathology_schema",
        "antibody": "antibody_schema",
        "sirna": "siRNA_schema",
        "cell_line": "cell_line_schema",
}

'''
Return a complete image schema or only a class schema
for example:
Return the idr classes for "Danio rerio" organism and "Tailbud" organism part
'''

def build_query(query, schema):
        if schema.lower() not in schema_names:
                return "%s is not supported"%schema
        schema_file = os.path.join(sys.path[1], "models/%s.yaml" % schema_names[schema.lower()])
        os.chdir(os.path.join(sys.path[1], "models"))
        logger.info("Loading schema from %s" % schema_file)
        report = validate(query, schema_file, schema)
        if not report.results:
            logger.info('The query data %s  is valid!' % schema)
        and_filters=[]
        for attr, val in query.items():
            print (attr, val)
            if type(val) is str:
                and_clause= {
                    "name": attr,
                    "value": val,
                    "operator": "contains",
                    "resource": "image"
                }
                and_filters.append(and_clause)
            elif type(val) is list:
                for va in val:
                        for at, v in va.items():
                            and_clause = {
                                    "name": at,
                                    "value": v,
                                    "operator": "contains",
                                    "resource": "image"
                            }
                            and_filters.append(and_clause)

        query_data = {"query_details": {"and_filters": and_filters}}
        print (query_data)
        received_results=query_searchengine(query_data)
        print (len(received_results))
        images_json=process_results (received_results, schema)
        return images_json


