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

from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_gce_persistent_disk import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGcePersistentDisk

class TestIoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGcePersistentDisk(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGcePersistentDisk unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGcePersistentDisk:
        """Test IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGcePersistentDisk
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGcePersistentDisk`
        """
        model = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGcePersistentDisk()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGcePersistentDisk(
                fs_type = '',
                partition = 56,
                pd_name = '',
                read_only = True
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGcePersistentDisk(
                pd_name = '',
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGcePersistentDisk(self):
        """Test IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGcePersistentDisk"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
