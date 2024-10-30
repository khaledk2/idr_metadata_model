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

Some usefull commands:
===================

Verify the schema:

         linkml-validate -s  idrmetadatamodels/models/image_schema.yaml 

Generate a python code for the model:

        gen-python idrmetadatamodels/models/image_schema.yaml  --genmeta  > idrmetadatamodels/models/image_schema.py

Generate class diagram

        gen-plantuml idrmetadatamodels/models/image_schema.yaml > idrmetadatamodels/models/image.puml

Generate png image

        plantuml  idrmetadatamodels/models/image.puml

Generate excelplaybook

        gen-excel idrmetadatamodels/models/image_schema.yaml > idrmetadatamodels/models/image.xlsx




