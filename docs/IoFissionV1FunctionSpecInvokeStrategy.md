# IoFissionV1FunctionSpecInvokeStrategy

InvokeStrategy is a set of controls which affect how function executes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_strategy** | [**IoFissionV1FunctionSpecInvokeStrategyExecutionStrategy**](IoFissionV1FunctionSpecInvokeStrategyExecutionStrategy.md) |  | [optional] 
**strategy_type** | **str** | StrategyType is the strategy type of function. Now it only supports &#39;execution&#39;. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_function_spec_invoke_strategy import IoFissionV1FunctionSpecInvokeStrategy

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1FunctionSpecInvokeStrategy from a JSON string
io_fission_v1_function_spec_invoke_strategy_instance = IoFissionV1FunctionSpecInvokeStrategy.from_json(json)
# print the JSON string representation of the object
print IoFissionV1FunctionSpecInvokeStrategy.to_json()

# convert the object into a dict
io_fission_v1_function_spec_invoke_strategy_dict = io_fission_v1_function_spec_invoke_strategy_instance.to_dict()
# create an instance of IoFissionV1FunctionSpecInvokeStrategy from a dict
io_fission_v1_function_spec_invoke_strategy_form_dict = io_fission_v1_function_spec_invoke_strategy.from_dict(io_fission_v1_function_spec_invoke_strategy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


