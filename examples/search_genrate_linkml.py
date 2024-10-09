
from utils.generate_validate_json_image_data import (
    get_image_from_single_attribute_qury,
    get_image_data_inside_container,
    validate_data,
    save_results_file,
    logger)

from utils.query_builder import build_query
import json

def run_json_query():
    '''
    Search using a specific schema data which is included in a file
    and return a json string contains the images which satisfy the query criteria
    It contains the specified classes

    :return:
    '''
    file_name='../data/organism_query_sample.jsom'
    with open(file_name) as f:
        query = json.load(f)
    images_json=build_query(query,"Organism")
    validate_data(images_json)
    save_results_file(images_json)
    print (len(images_json))
    print ("DONE!")



def run_query_container():
    '''
    Return the data inside a container (project or screen)
    It will return a complete image schema
    The user can set the target schema then it will limit the results to this schema
    :return:
    '''
    container = "idr0157"
    images_json = get_image_data_inside_container(container)
    validate_data(images_json)
    save_results_file(images_json)
    logger.info(len(images_json))

def run_query_for_attr_value():
    '''
    Query using attibute name and value
    Limit the returned results to contain only organism classes
    if the user wants to return everything, they should remove target schema  or set it to 'all'
    :return:
    '''

    images_json = get_image_from_single_attribute_qury("Organism", "Danio rerio", "Organism")
    validate_data(images_json)
    save_results_file(images_json)
    logger.info("Number of generated records: %s"%len(images_json))


#run_json_query()
run_query_container()
#run_query_for_attr_value()