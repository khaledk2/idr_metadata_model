Idr Metadata Model
=================
The LINKML schema for the study is: study_schema.yaml.

The LINKML schema for the image is: image_schema.yaml.

Setup working environment
=========================

The user should create a python venv and install the linkml packages

        python -m venv venv3
        source  venv3/bin/activate
        pip install -r requirements.txt

It  is required to install plantuml, in rocky linux 9:

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




