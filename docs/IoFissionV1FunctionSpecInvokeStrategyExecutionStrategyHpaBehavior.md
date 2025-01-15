# IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior

hpaBehavior is the behavior of HPA when scaling in up/down direction. Applicable for executor type newdeploy and container.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scale_down** | [**IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleDown**](IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleDown.md) |  | [optional] 
**scale_up** | [**IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleUp**](IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleUp.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior from a JSON string
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_instance = IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior.from_json(json)
# print the JSON string representation of the object
print IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior.to_json()

# convert the object into a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_instance.to_dict()
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior from a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_form_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior.from_dict(io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


