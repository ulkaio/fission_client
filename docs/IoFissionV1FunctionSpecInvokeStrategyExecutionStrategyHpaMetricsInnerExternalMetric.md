# IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetric

metric identifies the target metric by name and selector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is the name of the given metric | 
**selector** | [**IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetricSelector**](IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetricSelector.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external_metric import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetric

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetric from a JSON string
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external_metric_instance = IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetric.from_json(json)
# print the JSON string representation of the object
print IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetric.to_json()

# convert the object into a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external_metric_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external_metric_instance.to_dict()
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetric from a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external_metric_form_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external_metric.from_dict(io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


