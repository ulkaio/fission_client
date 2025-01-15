# IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerContainerResource

containerResource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod of the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the \"pods\" source. This is an alpha feature and can be enabled by the HPAContainerMetrics feature flag.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **str** | container is the name of the container in the pods of the scaling target | 
**name** | **str** | name is the name of the resource in question. | 
**target** | [**IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerContainerResourceTarget**](IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerContainerResourceTarget.md) |  | 

## Example

```python
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_container_resource import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerContainerResource

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerContainerResource from a JSON string
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_container_resource_instance = IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerContainerResource.from_json(json)
# print the JSON string representation of the object
print IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerContainerResource.to_json()

# convert the object into a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_container_resource_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_container_resource_instance.to_dict()
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerContainerResource from a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_container_resource_form_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_container_resource.from_dict(io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_container_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


