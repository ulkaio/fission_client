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

from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_flex_volume_secret_ref import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolumeSecretRef

class TestIoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolumeSecretRef(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolumeSecretRef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolumeSecretRef:
        """Test IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolumeSecretRef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolumeSecretRef`
        """
        model = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolumeSecretRef()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolumeSecretRef(
                name = ''
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolumeSecretRef(
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolumeSecretRef(self):
        """Test IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolumeSecretRef"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
