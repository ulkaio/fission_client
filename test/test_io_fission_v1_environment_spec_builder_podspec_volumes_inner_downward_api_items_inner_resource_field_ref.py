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

from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_items_inner_resource_field_ref import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerResourceFieldRef

class TestIoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerResourceFieldRef(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerResourceFieldRef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerResourceFieldRef:
        """Test IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerResourceFieldRef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerResourceFieldRef`
        """
        model = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerResourceFieldRef()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerResourceFieldRef(
                container_name = '',
                divisor = None,
                resource = ''
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerResourceFieldRef(
                resource = '',
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerResourceFieldRef(self):
        """Test IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerResourceFieldRef"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
