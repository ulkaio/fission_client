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

from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_empty_dir import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEmptyDir

class TestIoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEmptyDir(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEmptyDir unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEmptyDir:
        """Test IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEmptyDir
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEmptyDir`
        """
        model = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEmptyDir()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEmptyDir(
                medium = '',
                size_limit = fission_client.models.size_limit.sizeLimit()
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEmptyDir(
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEmptyDir(self):
        """Test IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEmptyDir"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
