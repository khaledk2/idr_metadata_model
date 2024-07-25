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

         linkml-validate -s  models/image_schema.yaml 

Generate a python code for the model:

        gen-python models/image_schema.yaml  --genmeta  > models/image_schema.py

Generate class diagram

        gen-plantuml models/image_schema.yaml > models/image.puml

Generate png image

        plantuml  models/image.puml





