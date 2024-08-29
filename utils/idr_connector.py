# This code is based on the following search engine example
# https://github.com/ome/omero_search_engine/blob/main/examples/pagination_submitquery.py
'''
It will accept the cidr number as input, call the searchengine, retrieve all the results
'''

import datetime
import logging
import json
import requests
import sys


submit_query_url ="https://idr.openmicroscopy.org/searchengine/api/v1/resources/submitquery/"

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

received_results = []
page = 1
ids = []
total_pages = 0
pagination_dict = None
next_page = None


def get_current_page_bookmark(pagination_dict):
    current_page = pagination_dict["current_page"]
    bookmark = None
    for page_rcd in pagination_dict["page_records"]:
        if page_rcd["page"] == current_page:
            bookmark = page_rcd["bookmark"]
    return current_page, bookmark


def call_omero_searchengine_return_results(url, data=None, method="post"):
    global page, total_pages, pagination_dict, next_page
    if method == "post":
        resp = requests.post(url, data=data)
    else:
        resp = requests.get(url)
    try:
        returned_results = json.loads(resp.text)
        if not returned_results.get("results"):
            logging.info(returned_results)
            sys.exit()

        elif len(returned_results["results"]) == 0:
            logging.info("Your query returns no results")
            sys.exit()
        # get the bookmark which will be used to call
        # the next page of the results
        pagination_dict = returned_results["results"].get("pagination")
        page, bookmark = get_current_page_bookmark(pagination_dict)
        page = pagination_dict.get("current_page")
        # get the size of the total results
        total_pages = pagination_dict.get("total_pages")
        next_page = pagination_dict.get("next_page")

        total_results = returned_results["results"]["size"]

        for res in returned_results["results"]["results"]:
            received_results.append(res)
            if res["id"] in ids:
                raise Exception(" Id dublicated error  %s" % res["id"])
            ids.append(res["id"])
        return bookmark, total_results

    except Exception as ex:
        logging.info("Error: %s" % ex)

def get_query_results(re_attribute, value, container_name=None):
    and_filters = [
        {
            "name": re_attribute,
            "value": value,  # "idr0051", #"idr0157",
            "operator": "equals",
            "resource": "image"
        },
    ]
    if container_name:
        and_filters.append({
            "name": "name",
            "value": container_name, #"idr0051", #"idr0157",
            "operator": "contains",
            "resource": "container"
        })

    query_data = {"query_details": {"and_filters": and_filters}}
    return query_searchengine(query_data)

def get_results(container_name):
    start = datetime.datetime.now()
    and_filters = [
        {
            "name": "name",
            "value": container_name, #"idr0051", #"idr0157",
            "operator": "contains",
            "resource": "container"
        },
    ]

    query_data = {"query_details": {"and_filters": and_filters}}
    return query_searchengine(query_data)
def query_searchengine(query_data):

    query_data_json = json.dumps(query_data)
    bookmark, total_results = call_omero_searchengine_return_results(
        submit_query_url, data=query_data_json
    )
    logging.info(
        "page: %s, / %s received results: %s / %s"
        % (page, total_pages, len(received_results), total_results)
    )

    while next_page:  # len(received_results) < total_results:
        query_data_ = {
            "query_details": query_data["query_details"],
            "pagination": pagination_dict,
        }
        query_data_json_ = json.dumps(query_data_)

        bookmark, total_results = call_omero_searchengine_return_results(
            submit_query_url, data=query_data_json_
        )

        logging.info(
            "bookmark: %s, page: %s, / %s received results: %s / %s"
            % (bookmark, page, total_pages, len(received_results), total_results)
        )
    end = datetime.datetime.now()
    return received_results

#received_results=get_results("idr0051")
#print (received_results)