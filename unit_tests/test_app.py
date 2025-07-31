import unittest
import os
from  idrmetadatamodels.utils.generate_validate_json_image_data import (
    get_resource_from_single_attribute_qury,
    create_schema_class_run_time,
    get_image_data_inside_container,
    validate_data,
    validate_data_run_time,
    logger)

from idrmetadatamodels.utils.query_builder import build_query
class BasicTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_build_in_schema(self):
        resource_json = get_resource_from_single_attribute_qury("Organism", "Danio rerio")
        assert len(resource_json) > 0
        self.assertTrue(validate_data(resource_json))
        logger.info("Number of generated records: %s" % len(resource_json))

    def test_external_schema(self):
        target_schema="test_data/TestModel.yaml"
        path, filename = os.path.split(os.path.realpath(__file__))
        target_schema=os.path.join(path, target_schema)
        resource_json = get_resource_from_single_attribute_qury("Protein Name", "ras-related protein 11b",target_schema=target_schema)
        assert len(resource_json) > 0
        class_path = create_schema_class_run_time(target_schema)
        self.assertTrue(validate_data_run_time(resource_json, class_path))
        logger.info("Number of generated records: %s" % len(resource_json))
