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

from fission_client.models.io_fission_v1_environment_spec_builder_podspec_resource_claims_inner import IoFissionV1EnvironmentSpecBuilderPodspecResourceClaimsInner

class TestIoFissionV1EnvironmentSpecBuilderPodspecResourceClaimsInner(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderPodspecResourceClaimsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderPodspecResourceClaimsInner:
        """Test IoFissionV1EnvironmentSpecBuilderPodspecResourceClaimsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderPodspecResourceClaimsInner`
        """
        model = IoFissionV1EnvironmentSpecBuilderPodspecResourceClaimsInner()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderPodspecResourceClaimsInner(
                name = '',
                resource_claim_name = '',
                resource_claim_template_name = ''
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderPodspecResourceClaimsInner(
                name = '',
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderPodspecResourceClaimsInner(self):
        """Test IoFissionV1EnvironmentSpecBuilderPodspecResourceClaimsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
