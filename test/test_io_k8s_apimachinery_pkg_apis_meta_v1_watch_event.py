# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.30.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_watch_event import IoK8sApimachineryPkgApisMetaV1WatchEvent

class TestIoK8sApimachineryPkgApisMetaV1WatchEvent(unittest.TestCase):
    """IoK8sApimachineryPkgApisMetaV1WatchEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoK8sApimachineryPkgApisMetaV1WatchEvent:
        """Test IoK8sApimachineryPkgApisMetaV1WatchEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoK8sApimachineryPkgApisMetaV1WatchEvent`
        """
        model = IoK8sApimachineryPkgApisMetaV1WatchEvent()
        if include_optional:
            return IoK8sApimachineryPkgApisMetaV1WatchEvent(
                object = None,
                type = ''
            )
        else:
            return IoK8sApimachineryPkgApisMetaV1WatchEvent(
                object = None,
                type = '',
        )
        """

    def testIoK8sApimachineryPkgApisMetaV1WatchEvent(self):
        """Test IoK8sApimachineryPkgApisMetaV1WatchEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
