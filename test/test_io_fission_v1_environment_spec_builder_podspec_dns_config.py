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

from fission_client.models.io_fission_v1_environment_spec_builder_podspec_dns_config import IoFissionV1EnvironmentSpecBuilderPodspecDnsConfig

class TestIoFissionV1EnvironmentSpecBuilderPodspecDnsConfig(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderPodspecDnsConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderPodspecDnsConfig:
        """Test IoFissionV1EnvironmentSpecBuilderPodspecDnsConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderPodspecDnsConfig`
        """
        model = IoFissionV1EnvironmentSpecBuilderPodspecDnsConfig()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderPodspecDnsConfig(
                nameservers = [
                    ''
                    ],
                options = [
                    fission_client.models.io_fission_v1_environment_spec_builder_podspec_dns_config_options_inner.io_fission_v1_Environment_spec_builder_podspec_dnsConfig_options_inner(
                        name = '', 
                        value = '', )
                    ],
                searches = [
                    ''
                    ]
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderPodspecDnsConfig(
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderPodspecDnsConfig(self):
        """Test IoFissionV1EnvironmentSpecBuilderPodspecDnsConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
