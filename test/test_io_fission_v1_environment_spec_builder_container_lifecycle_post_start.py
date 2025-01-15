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

from fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle_post_start import IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart

class TestIoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart:
        """Test IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart`
        """
        model = IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart(
                var_exec = fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle_post_start_exec.io_fission_v1_Environment_spec_builder_container_lifecycle_postStart_exec(
                    command = [
                        ''
                        ], ),
                http_get = fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle_post_start_http_get.io_fission_v1_Environment_spec_builder_container_lifecycle_postStart_httpGet(
                    host = '', 
                    http_headers = [
                        fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle_post_start_http_get_http_headers_inner.io_fission_v1_Environment_spec_builder_container_lifecycle_postStart_httpGet_httpHeaders_inner(
                            name = '', 
                            value = '', )
                        ], 
                    path = '', 
                    port = fission_client.models.port.port(), 
                    scheme = '', ),
                sleep = fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle_post_start_sleep.io_fission_v1_Environment_spec_builder_container_lifecycle_postStart_sleep(
                    seconds = 56, ),
                tcp_socket = fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle_post_start_tcp_socket.io_fission_v1_Environment_spec_builder_container_lifecycle_postStart_tcpSocket(
                    host = '', 
                    port = fission_client.models.port.port(), )
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart(
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart(self):
        """Test IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
