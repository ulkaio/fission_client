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

from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_status_cause import IoK8sApimachineryPkgApisMetaV1StatusCause

class TestIoK8sApimachineryPkgApisMetaV1StatusCause(unittest.TestCase):
    """IoK8sApimachineryPkgApisMetaV1StatusCause unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoK8sApimachineryPkgApisMetaV1StatusCause:
        """Test IoK8sApimachineryPkgApisMetaV1StatusCause
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoK8sApimachineryPkgApisMetaV1StatusCause`
        """
        model = IoK8sApimachineryPkgApisMetaV1StatusCause()
        if include_optional:
            return IoK8sApimachineryPkgApisMetaV1StatusCause(
                field = '',
                message = '',
                reason = ''
            )
        else:
            return IoK8sApimachineryPkgApisMetaV1StatusCause(
        )
        """

    def testIoK8sApimachineryPkgApisMetaV1StatusCause(self):
        """Test IoK8sApimachineryPkgApisMetaV1StatusCause"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
