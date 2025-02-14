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

from fission_client.models.io_fission_v1_kubernetes_watch_trigger_spec_functionref import IoFissionV1KubernetesWatchTriggerSpecFunctionref

class TestIoFissionV1KubernetesWatchTriggerSpecFunctionref(unittest.TestCase):
    """IoFissionV1KubernetesWatchTriggerSpecFunctionref unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1KubernetesWatchTriggerSpecFunctionref:
        """Test IoFissionV1KubernetesWatchTriggerSpecFunctionref
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1KubernetesWatchTriggerSpecFunctionref`
        """
        model = IoFissionV1KubernetesWatchTriggerSpecFunctionref()
        if include_optional:
            return IoFissionV1KubernetesWatchTriggerSpecFunctionref(
                functionweights = fission_client.models.functionweights.functionweights(),
                name = '',
                type = ''
            )
        else:
            return IoFissionV1KubernetesWatchTriggerSpecFunctionref(
                name = '',
                type = '',
        )
        """

    def testIoFissionV1KubernetesWatchTriggerSpecFunctionref(self):
        """Test IoFissionV1KubernetesWatchTriggerSpecFunctionref"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
