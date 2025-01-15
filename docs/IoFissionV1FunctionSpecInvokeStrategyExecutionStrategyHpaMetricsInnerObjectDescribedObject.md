# IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerObjectDescribedObject

describedObject specifies the descriptions of a object,such as kind,name apiVersion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | apiVersion is the API version of the referent | [optional] 
**kind** | **str** | kind is the kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | 
**name** | **str** | name is the name of the referent; More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | 

## Example

```python
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_object_described_object import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerObjectDescribedObject

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerObjectDescribedObject from a JSON string
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_object_described_object_instance = IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerObjectDescribedObject.from_json(json)
# print the JSON string representation of the object
print IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerObjectDescribedObject.to_json()

# convert the object into a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_object_described_object_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_object_described_object_instance.to_dict()
# create an instance of IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerObjectDescribedObject from a dict
io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_object_described_object_form_dict = io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_object_described_object.from_dict(io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_object_described_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


