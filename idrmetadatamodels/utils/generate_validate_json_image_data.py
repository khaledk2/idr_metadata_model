#from linkml_runtime.linkml_model.types import Integer, String, Uri
''''
This script is used to extract a container (project or screen) images' meta data from the searchengine
It will handle the data and create the objects from the generated python code (generated from the image schema)
Then it will get the json from the objects and validate it using the schema model
This script is still in progress
'''
import sys

from jsonpath_ng.bin.jsonpath import print_matches

from idrmetadatamodels.models.image_schema import Image, OrganismPart, Organism, Phenotype, Compound, Protein, CellLine, SiRNA
from idrmetadatamodels.models.study_schema import Study
from idrmetadatamodels.utils.get_schema_attributes import get_included_schema_classes

schema_classes={"Image":Image, "Organism Part":OrganismPart, "Organism":Organism, "Phenotype":Phenotype,
         "Compound":Compound, "Protein":Protein,"Cell line":CellLine,"siRNA":SiRNA}

from idrmetadatamodels.utils.get_schema_attributes import get_schema_attributes
import logging
import json

logger=logging.getLogger("idr-metadata-model")

logger.setLevel(logging.INFO)

from idrmetadatamodels.utils.idr_connector import get_results, get_query_results

classes_schema={"Image": Image, "Study": Study}

muti_values=[""]
def convert_to_key_value(json_ob):
    objects={}
    for key, item in json_ob.items():
        if key == "key_values":
            for lst in item: #json_ob.get("key_values"):
                if type(lst) is dict:
                        objects[lst.get("name")]=lst.get("value")
        else:
            objects[key]=item
    return objects

def get_image_data_for_schema():
    pass

def get_resource_from_single_attribute_qury(attr, value, target_schema="all", container_name=None, resource="image",data_source=None):
    resources_results=get_query_results(attr, value, container_name,resource, data_source)
    import os
    schema_path=None
    if os.path.isfile(target_schema):
        schema_path=target_schema
        target_schema=os.path.basename(target_schema).replace(".yaml", "")
    return (process_results(resources_results,target_schema,schema_path))

def get_image_data_inside_container(container,target_schema="all", resource="image"):
    images_results=get_results(container, resource)
    return (process_results(images_results,target_schema))


def extract_schema_data(resource_data, all_attributes, target_schema):
    records={}
    image_lower = {k.lower(): v for k, v in resource_data.items() if k}
    if target_schema in all_attributes:
        main_schema_attributes=all_attributes[target_schema]
    else:
        main_schema_attributes=get_schema_attributes(target_schema)
        all_attributes[target_schema]=main_schema_attributes
    for main_schema, atts in main_schema_attributes.items():
        for atr in atts:
            if atr.get("range") in ["string", "uri","integer"]:
                if resource_data.get(atr.get("name")):
                    records[atr.get("name")]=resource_data.get(atr.get("name"))
                elif image_lower.get(atr.get("name").lower()):
                    records[atr.get("name")] = image_lower.get(atr.get("name"))
            else:
                records[atr.get("name")] = extract_schema_data(resource_data, all_attributes, atr.get("range"))
    return records

def process_results(resource_results, target_schema="Image", schema_path=None):
    resource_json = []
    if target_schema.lower() == "all":
        target_schema = "Image"
    all_attributes={}
    all_attributes[target_schema]=get_schema_attributes(target_schema,schema_path)
    included_schema_classes = get_included_schema_classes(target_schema, schema_path)
    for sub_schem in included_schema_classes:
        all_attributes[sub_schem]=get_schema_attributes(sub_schem)
    for res_rcord in resource_results:
        resource_ = convert_to_key_value(res_rcord)
        attrs=extract_schema_data(resource_,all_attributes,target_schema)
        if target_schema and target_schema.lower()!="image" and target_schema.lower()!="study": #and target_schema.lower()!="ssbdproject":
            res_dict = {"id": res_rcord.get("id"), "name":res_rcord.get("name"),target_schema.lower(): attrs}
        else:
            res_dict = attrs
            res_dict["id"]=res_rcord.get("id")
            res_dict["name"]=res_rcord.get("name")
        #img_dict = json_dumper(json_dumper(image_obj))
        #del img_dict['@type']
        resource_json.append(res_dict)
        ## clean the data
        to_be_deleted=[]
        for item, itev in res_dict.items():
            try:
                if len(itev)==0:
                    to_be_deleted.append(item)
            except:
                pass
        for it in to_be_deleted:
            del res_dict[it]

    return resource_json

def set_data_for_testing (org_data):
    new_test={}
    for key, value in org_data.items():
        if type(value) is dict:
            new_test[key.replace(" ", "_")] = set_data_for_testing(value)
        else:
            new_test[key.replace(" ", "_")] = value
    return new_test

def validate_data(resource_json, target_schema="Image"):
    data_is_valid = True
    for res_json in resource_json:
        try:
            test_res_json=set_data_for_testing(res_json)
            res_class=classes_schema.get(target_schema)
            res_object = res_class(**test_res_json)  # This will raise an error if validation fails
            logger.info('Valid data!, the %s  data with id=%s, and name %s is valid.' %(target_schema, res_json.get("id"), res_json.get("name")))
        except Exception as e:
            logger.info("Validation failed for %s , id: %s, error message is: %s"%(target_schema,res_json.get("id"),e))
            logger.info("Validation error is: %s" %e)
            data_is_valid=False
    return data_is_valid

def create_schema_class_run_time(schema_path):
    import subprocess, os
    class_name = os.path.basename(schema_path).replace(".yaml", "")
    schema_folder=os.path.dirname(schema_path)
    class_path = os.path.join(schema_folder,"%s.py"%class_name )
    command = "gen-python %s --genmeta > %s" % (schema_path, class_path)
    proc = subprocess.run(command, shell=True, capture_output=True, text=True)
    logger.info("Output: %s"%proc.stdout)
    logger.info("Error:  %s"%proc.stderr)
    with open(class_path, "r") as f:
        lines = f.readlines()
    with open(class_path, "w") as f:
        for line in lines:
            if "from .types import Integer, String" not in line and "from .types import String" not in line:
                f.write(line)
    return class_path

def validate_data_run_time(images_json, class_path):
    #from data.Biosample import Biosample
    data_is_valid = True
    with open(class_path, 'r') as file:
        class_code = file.read()
    # Execute the class definition
    exec(class_code, globals())
    import os
    schema_class_name = os.path.basename(class_path).replace(".py", "")
    Schema_class = globals().get(schema_class_name)
    for image_json in images_json:
        try:
            class_data=image_json.get(schema_class_name.lower())
            if class_data:
                modified_class={}
                for key, value in class_data.items():
                    modified_class[key.replace(" ","_")]=value
                #for ke, val in image_json.items():
                #    if ke==schema_class_name.lower():
                #        continue
                #    modified_class[ke]=val
                schema_class = Schema_class(**modified_class)  # This will raise an error if validation fails
                logger.info('Valid data!, the image data with id=%s, and name %s is valid.' %(image_json.get("id"), image_json.get("name")))
            else:
                logger.info('No valid data is found the image data with id=%s, and name %s is not found.' % (
                image_json.get("id"), image_json.get("name")))
                data_is_valid=False
        except Exception as e:
            logger.info("Validation failed for image, id: %s, error message is: %s"%(image_json.get("id"),e))
            data_is_valid=False
    return data_is_valid

def save_results_file(results, file_name="results.json"):
    with open(file_name, "w") as outfile:
        outfile.write(json.dumps(results, indent=4))