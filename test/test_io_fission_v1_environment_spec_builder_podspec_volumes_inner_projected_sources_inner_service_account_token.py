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

from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_service_account_token import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerServiceAccountToken

class TestIoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerServiceAccountToken(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerServiceAccountToken unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerServiceAccountToken:
        """Test IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerServiceAccountToken
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerServiceAccountToken`
        """
        model = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerServiceAccountToken()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerServiceAccountToken(
                audience = '',
                expiration_seconds = 56,
                path = ''
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerServiceAccountToken(
                path = '',
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerServiceAccountToken(self):
        """Test IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerServiceAccountToken"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
