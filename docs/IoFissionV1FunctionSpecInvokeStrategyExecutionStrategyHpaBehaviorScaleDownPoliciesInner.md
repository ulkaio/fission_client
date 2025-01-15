# IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleDownPoliciesInner

HPAScalingPolicy is a single policy which must hold true for a specified past interval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_seconds** | **int** | periodSeconds specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min). | 
**type** | **str** | type is used to specify the scaling policy. | 
**value** | **int** | value contains the amount of change which is permitted by the policy. It must be greater than zero | 

## Example

```python
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_down_policies_inner import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleDownPoliciesInner

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleDownPoliciesInner from a JSON string
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_down_policies_inner_instance = IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleDownPoliciesInner.from_json(json)
# print the JSON string representation of the object
print IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleDownPoliciesInner.to_json()

# convert the object into a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_down_policies_inner_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_down_policies_inner_instance.to_dict()
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleDownPoliciesInner from a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_down_policies_inner_form_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_down_policies_inner.from_dict(io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_down_policies_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


