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

from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_secret import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerSecret

class TestIoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerSecret(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerSecret unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerSecret:
        """Test IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerSecret
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerSecret`
        """
        model = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerSecret()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerSecret(
                default_mode = 56,
                items = [
                    fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_config_map_items_inner.io_fission_v1_Environment_spec_builder_podspec_volumes_inner_configMap_items_inner(
                        key = '', 
                        mode = 56, 
                        path = '', )
                    ],
                optional = True,
                secret_name = ''
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerSecret(
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerSecret(self):
        """Test IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerSecret"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
