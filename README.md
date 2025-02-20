Idr Metadata Model
=================
The LINKML schema for the study is: study_schema.yaml.

The LINKML schema for the image is: image_schema.yaml.

Setup working environment
=========================

The user should clone the project, create a python venv and install the required packages    

        git clone https://github.com/khaledk2/idr_metadata_model.git
        cd idr_metadata_model 
        python -m venv venv3
        source  venv3/bin/activate
        pip install -r requirements.txt

Alternatively, user can install it using these commands:

        python -m venv idr_metamodel
        source  idr_metamodel/bin/activate
        pip install https://github.com/khaledk2/idr_metadata_model/releases/download/V_0.2/idr_metadata_model-0.1-py3-none-any.whl

It is required to install plantuml, in rocky linux 9:

        sudo dnf -y update
        sudo dnf install -y plantuml

Some usefully commands:
===================

Verify the schema:

         linkml-validate -s  idrmetadatamodels/models/image_schema.yaml 

Generate a python code for the model:

        gen-python idrmetadatamodels/models/image_schema.yaml  --genmeta  > idrmetadatamodels/models/image_schema.py

Generate class diagram

        gen-plantuml idrmetadatamodels/models/image_schema.yaml > idrmetadatamodels/models/image.puml

Generate png image

        plantuml  idrmetadatamodels/models/image.puml

Generate excel playbook

        gen-excel idrmetadatamodels/models/image_schema.yaml > idrmetadatamodels/models/image.xlsx


Data Search
===========
Users can query the search engine, and the returned data will be formatted to be compatible with the IDR schema. They can provide search criteria and, if no schema is specified, the default “image” schema will be used., users have the option to request a sub-schema, such as " Cell Line" Additionally.
Users can provide an external schema, and the search results will be formatted accordingly.
In all cases, users should provide a search term, for example, searching for "organism" with a value of "homo species"

Examples
--------

The user wants to search for **Danio rerio Organism** and return the format the results according to the **image** schema:

     resource_json = get_resource_from_single_attribute_qury("Organism", attribute_value=Danio rerio, target_schema="image", resource="image")

To validate the returned results using the target schema, you can use the following method:

     validate_data(resource_json, target_schema="image")

To save the results to a file, the following method should be used: 

        save_results_file(resource_json, file_name="my_results.json")


Another example, the user wants to use a special (external) schema and would like to search for the images which has **Protein Name** which value is **ras-related protein 11b**
The user should provide his yaml file schema 

    images_json = get_resource_from_single_attribute_qury(attribute_name="Protein Name", attribute_value="ras-related protein 11b", target_schema="path/to/my/yaml/scvhema/file")

ALso, the user can validate the results using the next method:

        validate_data(resource_json, target_schema)
   
The user may save the results using the following method, the default file name is "results.json" and th use can use his onw name

        save_results_file(resource_json,file_name="my_results.json")

In the examples folder, the user can find some working examples.
