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

from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior

class TestIoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior(unittest.TestCase):
    """IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior:
        """Test IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior`
        """
        model = IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior()
        if include_optional:
            return IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior(
                scale_down = fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_down.io_fission_v1_Function_spec_InvokeStrategy_ExecutionStrategy_hpaBehavior_scaleDown(
                    policies = [
                        fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_down_policies_inner.io_fission_v1_Function_spec_InvokeStrategy_ExecutionStrategy_hpaBehavior_scaleDown_policies_inner(
                            period_seconds = 56, 
                            type = '', 
                            value = 56, )
                        ], 
                    select_policy = '', 
                    stabilization_window_seconds = 56, ),
                scale_up = fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_up.io_fission_v1_Function_spec_InvokeStrategy_ExecutionStrategy_hpaBehavior_scaleUp(
                    policies = [
                        fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_down_policies_inner.io_fission_v1_Function_spec_InvokeStrategy_ExecutionStrategy_hpaBehavior_scaleDown_policies_inner(
                            period_seconds = 56, 
                            type = '', 
                            value = 56, )
                        ], 
                    select_policy = '', 
                    stabilization_window_seconds = 56, )
            )
        else:
            return IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior(
        )
        """

    def testIoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior(self):
        """Test IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
