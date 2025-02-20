from  idrmetadatamodels.utils.generate_validate_json_image_data import (
    get_resource_from_single_attribute_qury,
    get_image_data_inside_container,
    create_schema_class_run_time,
    validate_data_run_time,
    validate_data,
    save_results_file,
    logger)

from idrmetadatamodels.utils.query_builder import build_query
import json


def run_query_for_attr_value(attribute_name, attribute_value , target_schema="Image",resource="image"):
    '''
    Query using attibute name and value
    Limit the returned results to contain only organism classes
    if the user wants to return everything, they should remove target schema  or set it to 'all'
    :return:
    '''

    images_json = get_resource_from_single_attribute_qury(attribute_name, attribute_value, target_schema, resource=resource)
    class_path=create_schema_class_run_time(target_schema)
    validate_data_run_time(images_json,class_path)
    save_results_file(images_json)
    logger.info("Number of generated records: %s"%len(images_json))
    print(images_json[0])


#run_query_for_attr_value("Protein Name", "ras-related protein 11b", "../data/Genetic.yaml")
#run_query_for_attr_value("Gene symbol", "B0336.10, rpl-23", "../data/SSBDProject.yaml", resource="project")

run_query_for_attr_value("Organism", "Homo sapiens", "../data/SSBDProject.yaml", resource="project")
