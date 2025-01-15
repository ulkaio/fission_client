# IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternal

external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | [**IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetric**](IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetric.md) |  | 
**target** | [**IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerContainerResourceTarget**](IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerContainerResourceTarget.md) |  | 

## Example

```python
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternal

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternal from a JSON string
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external_instance = IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternal.from_json(json)
# print the JSON string representation of the object
print IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternal.to_json()

# convert the object into a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external_instance.to_dict()
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternal from a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external_form_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external.from_dict(io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


