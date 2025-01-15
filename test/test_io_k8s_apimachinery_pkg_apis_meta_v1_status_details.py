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

from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_status_details import IoK8sApimachineryPkgApisMetaV1StatusDetails

class TestIoK8sApimachineryPkgApisMetaV1StatusDetails(unittest.TestCase):
    """IoK8sApimachineryPkgApisMetaV1StatusDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoK8sApimachineryPkgApisMetaV1StatusDetails:
        """Test IoK8sApimachineryPkgApisMetaV1StatusDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoK8sApimachineryPkgApisMetaV1StatusDetails`
        """
        model = IoK8sApimachineryPkgApisMetaV1StatusDetails()
        if include_optional:
            return IoK8sApimachineryPkgApisMetaV1StatusDetails(
                causes = [
                    fission_client.models.io/k8s/apimachinery/pkg/apis/meta/v1/status_cause.io.k8s.apimachinery.pkg.apis.meta.v1.StatusCause(
                        field = '', 
                        message = '', 
                        reason = '', )
                    ],
                group = '',
                kind = '',
                name = '',
                retry_after_seconds = 56,
                uid = ''
            )
        else:
            return IoK8sApimachineryPkgApisMetaV1StatusDetails(
        )
        """

    def testIoK8sApimachineryPkgApisMetaV1StatusDetails(self):
        """Test IoK8sApimachineryPkgApisMetaV1StatusDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
