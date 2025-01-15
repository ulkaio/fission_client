# IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerResource

resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the \"pods\" source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is the name of the resource in question. | 
**target** | [**IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerContainerResourceTarget**](IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerContainerResourceTarget.md) |  | 

## Example

```python
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_resource import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerResource

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerResource from a JSON string
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_resource_instance = IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerResource.from_json(json)
# print the JSON string representation of the object
print IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerResource.to_json()

# convert the object into a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_resource_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_resource_instance.to_dict()
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerResource from a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_resource_form_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_resource.from_dict(io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


