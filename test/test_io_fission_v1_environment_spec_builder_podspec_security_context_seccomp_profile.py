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

from fission_client.models.io_fission_v1_environment_spec_builder_podspec_security_context_seccomp_profile import IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextSeccompProfile

class TestIoFissionV1EnvironmentSpecBuilderPodspecSecurityContextSeccompProfile(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextSeccompProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextSeccompProfile:
        """Test IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextSeccompProfile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextSeccompProfile`
        """
        model = IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextSeccompProfile()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextSeccompProfile(
                localhost_profile = '',
                type = ''
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextSeccompProfile(
                type = '',
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderPodspecSecurityContextSeccompProfile(self):
        """Test IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextSeccompProfile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
