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

from fission_client.models.io_fission_v1_environment_spec_builder_container_env_from_inner_config_map_ref import IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerConfigMapRef

class TestIoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerConfigMapRef(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerConfigMapRef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerConfigMapRef:
        """Test IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerConfigMapRef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerConfigMapRef`
        """
        model = IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerConfigMapRef()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerConfigMapRef(
                name = '',
                optional = True
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerConfigMapRef(
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerConfigMapRef(self):
        """Test IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerConfigMapRef"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
