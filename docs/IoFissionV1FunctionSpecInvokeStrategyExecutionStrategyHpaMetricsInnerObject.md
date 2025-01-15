# IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerObject

object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**described_object** | [**IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerObjectDescribedObject**](IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerObjectDescribedObject.md) |  | 
**metric** | [**IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetric**](IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetric.md) |  | 
**target** | [**IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerContainerResourceTarget**](IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerContainerResourceTarget.md) |  | 

## Example

```python
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_object import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerObject

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerObject from a JSON string
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_object_instance = IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerObject.from_json(json)
# print the JSON string representation of the object
print IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerObject.to_json()

# convert the object into a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_object_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_object_instance.to_dict()
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerObject from a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_object_form_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_object.from_dict(io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


