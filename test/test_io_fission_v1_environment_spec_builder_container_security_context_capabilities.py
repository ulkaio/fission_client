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

from fission_client.models.io_fission_v1_environment_spec_builder_container_security_context_capabilities import IoFissionV1EnvironmentSpecBuilderContainerSecurityContextCapabilities

class TestIoFissionV1EnvironmentSpecBuilderContainerSecurityContextCapabilities(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderContainerSecurityContextCapabilities unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderContainerSecurityContextCapabilities:
        """Test IoFissionV1EnvironmentSpecBuilderContainerSecurityContextCapabilities
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderContainerSecurityContextCapabilities`
        """
        model = IoFissionV1EnvironmentSpecBuilderContainerSecurityContextCapabilities()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderContainerSecurityContextCapabilities(
                add = [
                    ''
                    ],
                drop = [
                    ''
                    ]
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderContainerSecurityContextCapabilities(
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderContainerSecurityContextCapabilities(self):
        """Test IoFissionV1EnvironmentSpecBuilderContainerSecurityContextCapabilities"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
