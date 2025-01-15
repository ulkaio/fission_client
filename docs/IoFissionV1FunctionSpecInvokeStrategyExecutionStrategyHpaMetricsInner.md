# IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInner

MetricSpec specifies how to scale based on a single metric (only `type` and one other matching field should be set at once).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_resource** | [**IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerContainerResource**](IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerContainerResource.md) |  | [optional] 
**external** | [**IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternal**](IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternal.md) |  | [optional] 
**object** | [**IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerObject**](IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerObject.md) |  | [optional] 
**pods** | [**IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerPods**](IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerPods.md) |  | [optional] 
**resource** | [**IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerResource**](IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerResource.md) |  | [optional] 
**type** | **str** | type is the type of metric source.  It should be one of \&quot;ContainerResource\&quot;, \&quot;External\&quot;, \&quot;Object\&quot;, \&quot;Pods\&quot; or \&quot;Resource\&quot;, each mapping to a matching field in the object. Note: \&quot;ContainerResource\&quot; type is available on when the feature-gate HPAContainerMetrics is enabled | 

## Example

```python
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInner

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInner from a JSON string
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_instance = IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInner.from_json(json)
# print the JSON string representation of the object
print IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInner.to_json()

# convert the object into a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_instance.to_dict()
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInner from a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_form_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner.from_dict(io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


