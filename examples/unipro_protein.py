#!/usr/bin/env python

import requests
import json
from idrmetadatamodels.utils.idr_connector import get_query_results
from idrmetadatamodels.utils.generate_validate_json_image_data import get_image_from_single_attribute_qury, validate_data


def get_linmkl_for_uniprot_bucket(protein_url, validate=False):
    # call the idr and get the protein schema
    images_json = get_image_from_single_attribute_qury("Protein URL", protein_url, "Protein")
    if validate:
        validate_data(images_json)
    print(len(images_json))
    return images_json


def determine_uniprot_images():
    '''
        This script calls the IDR to obtain the URLs of proteins which have a uniprot URL, then gets all the images for each value
    '''
    # Call idr to get all the uniprot Protein URL values
    buckets_url= "https://idr.openmicroscopy.org/searchengine//api/v1/resources/image/searchvalues/?value=uniprot"
    buckets = requests.get(buckets_url, timeout=10).json().get("data")
    print (json.dumps(buckets, indent=2))

    print ("No. of different Protein URL values:%s "%len(buckets))
    # Call idr to  obtain all the images for each value
    all_results={}
    # dict contains the images for each Protein URL value
    for bucket in buckets:
        print ("Obtaining value %s/%s"%(buckets.index(bucket)+1, len(buckets)))
        print ("Protein URL %s has %s images" %((bucket.get("Value")), bucket.get("Number of images")))
        all_images=get_query_results (bucket.get("Key"), bucket.get("Value"))
        print ("No of received images %s"%len(all_images))
        rv=[]
        for result in all_images:
            image = result["id"]
            rv.append(image)
        all_results[bucket.get("Value")] = rv

    print("id,url,thumbnail")
    for protein, images in all_results.items():
        for image in images:
            print(f"{image},{protein},https://idr.openmicroscopy.org/webgateway/render_thumbnail/{image}/")
            break
        break

#https://idr.openmicroscopy.org/webgateway/render_thumbnail/12805109/
images_json=get_linmkl_for_uniprot_bucket("https://www.uniprot.org/uniprot/q15907",validate=True)
print (json.dumps(images_json, indent=2))
print(len(images_json))

#determine_uniprot_images()