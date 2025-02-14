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

from fission_client.models.io_fission_v1_environment_spec_builder_container_env_from_inner import IoFissionV1EnvironmentSpecBuilderContainerEnvFromInner

class TestIoFissionV1EnvironmentSpecBuilderContainerEnvFromInner(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderContainerEnvFromInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderContainerEnvFromInner:
        """Test IoFissionV1EnvironmentSpecBuilderContainerEnvFromInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderContainerEnvFromInner`
        """
        model = IoFissionV1EnvironmentSpecBuilderContainerEnvFromInner()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderContainerEnvFromInner(
                config_map_ref = fission_client.models.io_fission_v1_environment_spec_builder_container_env_from_inner_config_map_ref.io_fission_v1_Environment_spec_builder_container_envFrom_inner_configMapRef(
                    name = '', 
                    optional = True, ),
                prefix = '',
                secret_ref = fission_client.models.io_fission_v1_environment_spec_builder_container_env_from_inner_secret_ref.io_fission_v1_Environment_spec_builder_container_envFrom_inner_secretRef(
                    name = '', 
                    optional = True, )
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderContainerEnvFromInner(
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderContainerEnvFromInner(self):
        """Test IoFissionV1EnvironmentSpecBuilderContainerEnvFromInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
