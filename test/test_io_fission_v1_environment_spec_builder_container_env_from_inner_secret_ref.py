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

from fission_client.models.io_fission_v1_environment_spec_builder_container_env_from_inner_secret_ref import IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerSecretRef

class TestIoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerSecretRef(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerSecretRef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerSecretRef:
        """Test IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerSecretRef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerSecretRef`
        """
        model = IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerSecretRef()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerSecretRef(
                name = '',
                optional = True
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerSecretRef(
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerSecretRef(self):
        """Test IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerSecretRef"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
