# IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetricSelector

selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_expressions** | [**List[IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelectorMatchExpressionsInner]**](IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelectorMatchExpressionsInner.md) | matchExpressions is a list of label selector requirements. The requirements are ANDed. | [optional] 
**match_labels** | **Dict[str, str]** | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \&quot;key\&quot;, the operator is \&quot;In\&quot;, and the values array contains only \&quot;value\&quot;. The requirements are ANDed. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external_metric_selector import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetricSelector

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetricSelector from a JSON string
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external_metric_selector_instance = IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetricSelector.from_json(json)
# print the JSON string representation of the object
print IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetricSelector.to_json()

# convert the object into a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external_metric_selector_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external_metric_selector_instance.to_dict()
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetricSelector from a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external_metric_selector_form_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external_metric_selector.from_dict(io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external_metric_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


