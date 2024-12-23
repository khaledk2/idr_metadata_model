
from linkml_runtime.utils.schemaview import SchemaView


import os
def get_included_schema_classes(schema_class_name, schema_path=None):
    included_schema_classes= []
    if not schema_path:
        path_s = os.path.dirname(os.path.realpath(__file__)).replace("utils", "models")
        print(path_s)
        schema_path = "%s/%s_schema.yaml" % (path_s,schema_class_name.lower())
    if not os.path.isfile((schema_path)):
        print ("No schema file %s is found for %s" % (schema_path,schema_class_name))
        return included_schema_classes


    schema_view = SchemaView(schema_path)
    # Get the class definition
    class_def = schema_view.get_class(schema_class_name)
    # Extract all attributes (slots) for the class
    for slot_name in class_def.attributes:
        # Get slot definition which includes range and other details
        slot_def = schema_view.get_slot(slot_name)
        # Check attribute refers to another class
        range_name = slot_def.range
        if range_name:
            # Check if the range is a class defined in the schema
            if schema_view.get_class(range_name):
                print("IT is a class: %s" % range_name)
                included_schema_classes.append(range_name)
                #included_schema_classes[range_name]=schema_view.get_class(range_name)
    return included_schema_classes

def get_schema_class_attribut(schema_class_name):
    schema_attributes = {}

    path_s=os.path.dirname(os.path.realpath(__file__)).replace("utils","models")

    schema_path = "%s/%s_schema.yaml" % (path_s,schema_class_name.lower().replace(" ","_"))
    if not os.path.isfile((schema_path)):
        print("No schema file %s is found for %s" % (schema_path,schema_class_name))
        return schema_attributes

    schema_view = SchemaView(schema_path)

    # Get the class definition
    class_def = schema_view.get_class(schema_class_name)
    print (type(class_def), type(schema_view))
    print (class_def.__dict__)
    if class_def.attributes:
        print(f"Attributes of class '{schema_class_name}':")
        for slot_name, slot_def in class_def.attributes.items():
            attribute = {}
            schema_attributes[slot_name]=attribute
            attribute["name"] = slot_name
            attribute["identifier"] = slot_def.identifier
            attribute["range"] = slot_def.range
            attribute["required"] = slot_def.required

    return schema_attributes

def get_schema_attributes(class_name, schema_path=None):
    # Load your schema file
    class_def=None
    if schema_path and  os.path.isfile(schema_path):
        schema_view = SchemaView(schema_path)
        class_def = schema_view.get_class(class_name)
    elif class_name:
        path_s = os.path.dirname(os.path.realpath(__file__)).replace("utils", "models")
        print (path_s)
        schema_path = "%s/%s_schema.yaml" % (path_s, class_name.replace(" ", "_").lower())
        schema_view = SchemaView(schema_path)
        class_def = schema_view.get_class(class_name)
    # Get the class definition
    schema_attributes={}
    # Extract all attributes (slots) for the class

    if class_def and class_def.attributes:
        attributes=[]
        schema_attributes[class_name]=attributes
        #print(f"Attributes of class '{class_name}':")
        for slot_name, slot_info in class_def.attributes.items():
            slot_def = schema_view.get_slot(slot_name)
            attribute={}
            attributes.append(attribute)
            attribute["name"]=slot_name
            attribute["identifier"]=slot_def.identifier
            attribute["range"]=slot_def.range
            attribute["required"]=slot_def.required
    else:
        print(f"Class '{class_name}' has no attributes defined.")
    return schema_attributes
