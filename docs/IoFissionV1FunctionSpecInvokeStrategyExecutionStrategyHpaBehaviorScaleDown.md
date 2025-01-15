# IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleDown

scaleDown is scaling policy for scaling Down. If not set, the default value is to allow to scale down to minReplicas pods, with a 300 second stabilization window (i.e., the highest recommendation for the last 300sec is used).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleDownPoliciesInner]**](IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleDownPoliciesInner.md) | policies is a list of potential scaling polices which can be used during scaling. At least one policy must be specified, otherwise the HPAScalingRules will be discarded as invalid | [optional] 
**select_policy** | **str** | selectPolicy is used to specify which policy should be used. If not set, the default value Max is used. | [optional] 
**stabilization_window_seconds** | **int** | stabilizationWindowSeconds is the number of seconds for which past recommendations should be considered while scaling up or scaling down. StabilizationWindowSeconds must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long). | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_down import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleDown

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleDown from a JSON string
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_down_instance = IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleDown.from_json(json)
# print the JSON string representation of the object
print IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleDown.to_json()

# convert the object into a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_down_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_down_instance.to_dict()
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleDown from a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_down_form_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_down.from_dict(io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_down_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


