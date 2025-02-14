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

from fission_client.models.io_fission_v1_environment_spec_resources import IoFissionV1EnvironmentSpecResources

class TestIoFissionV1EnvironmentSpecResources(unittest.TestCase):
    """IoFissionV1EnvironmentSpecResources unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecResources:
        """Test IoFissionV1EnvironmentSpecResources
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecResources`
        """
        model = IoFissionV1EnvironmentSpecResources()
        if include_optional:
            return IoFissionV1EnvironmentSpecResources(
                claims = [
                    fission_client.models.io_fission_v1_environment_spec_builder_container_resources_claims_inner.io_fission_v1_Environment_spec_builder_container_resources_claims_inner(
                        name = '', 
                        request = '', )
                    ],
                limits = {
                    'key' : None
                    },
                requests = {
                    'key' : None
                    }
            )
        else:
            return IoFissionV1EnvironmentSpecResources(
        )
        """

    def testIoFissionV1EnvironmentSpecResources(self):
        """Test IoFissionV1EnvironmentSpecResources"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
