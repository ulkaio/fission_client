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

from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_cephfs import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfs

class TestIoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfs(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfs:
        """Test IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfs
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfs`
        """
        model = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfs()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfs(
                monitors = [
                    ''
                    ],
                path = '',
                read_only = True,
                secret_file = '',
                secret_ref = fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_cephfs_secret_ref.io_fission_v1_Environment_spec_builder_podspec_volumes_inner_cephfs_secretRef(
                    name = '', ),
                user = ''
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfs(
                monitors = [
                    ''
                    ],
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfs(self):
        """Test IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfs"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
