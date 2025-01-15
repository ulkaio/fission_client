# IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerPods

pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | [**IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetric**](IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetric.md) |  | 
**target** | [**IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerContainerResourceTarget**](IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerContainerResourceTarget.md) |  | 

## Example

```python
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_pods import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerPods

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerPods from a JSON string
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_pods_instance = IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerPods.from_json(json)
# print the JSON string representation of the object
print IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerPods.to_json()

# convert the object into a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_pods_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_pods_instance.to_dict()
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerPods from a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_pods_form_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_pods.from_dict(io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_pods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


