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

from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPI

class TestIoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPI(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPI:
        """Test IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPI`
        """
        model = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPI()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPI(
                default_mode = 56,
                items = [
                    fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_items_inner.io_fission_v1_Environment_spec_builder_podspec_volumes_inner_downwardAPI_items_inner(
                        field_ref = fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_items_inner_field_ref.io_fission_v1_Environment_spec_builder_podspec_volumes_inner_downwardAPI_items_inner_fieldRef(
                            api_version = '', 
                            field_path = '', ), 
                        mode = 56, 
                        path = '', 
                        resource_field_ref = fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_items_inner_resource_field_ref.io_fission_v1_Environment_spec_builder_podspec_volumes_inner_downwardAPI_items_inner_resourceFieldRef(
                            container_name = '', 
                            divisor = fission_client.models.divisor.divisor(), 
                            resource = '', ), )
                    ]
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPI(
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPI(self):
        """Test IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
