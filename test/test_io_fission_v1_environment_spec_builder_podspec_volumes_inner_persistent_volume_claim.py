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

from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_persistent_volume_claim import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPersistentVolumeClaim

class TestIoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPersistentVolumeClaim(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPersistentVolumeClaim unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPersistentVolumeClaim:
        """Test IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPersistentVolumeClaim
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPersistentVolumeClaim`
        """
        model = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPersistentVolumeClaim()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPersistentVolumeClaim(
                claim_name = '',
                read_only = True
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPersistentVolumeClaim(
                claim_name = '',
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPersistentVolumeClaim(self):
        """Test IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPersistentVolumeClaim"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
