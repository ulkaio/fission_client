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

from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_resource import IoK8sApimachineryPkgApisMetaV1APIResource

class TestIoK8sApimachineryPkgApisMetaV1APIResource(unittest.TestCase):
    """IoK8sApimachineryPkgApisMetaV1APIResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoK8sApimachineryPkgApisMetaV1APIResource:
        """Test IoK8sApimachineryPkgApisMetaV1APIResource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoK8sApimachineryPkgApisMetaV1APIResource`
        """
        model = IoK8sApimachineryPkgApisMetaV1APIResource()
        if include_optional:
            return IoK8sApimachineryPkgApisMetaV1APIResource(
                categories = [
                    ''
                    ],
                group = '',
                kind = '',
                name = '',
                namespaced = True,
                short_names = [
                    ''
                    ],
                singular_name = '',
                storage_version_hash = '',
                verbs = [
                    ''
                    ],
                version = ''
            )
        else:
            return IoK8sApimachineryPkgApisMetaV1APIResource(
                kind = '',
                name = '',
                namespaced = True,
                singular_name = '',
                verbs = [
                    ''
                    ],
        )
        """

    def testIoK8sApimachineryPkgApisMetaV1APIResource(self):
        """Test IoK8sApimachineryPkgApisMetaV1APIResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
