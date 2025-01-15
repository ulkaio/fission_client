# IoFissionV1FunctionSpec

FunctionSpec describes the contents of the function.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoke_strategy** | [**IoFissionV1FunctionSpecInvokeStrategy**](IoFissionV1FunctionSpecInvokeStrategy.md) |  | 
**concurrency** | **int** | Maximum number of pods to be specialized which will serve requests This is optional. If not specified default value will be taken as 500 | [optional] 
**configmaps** | **object** | Reference to a list of configmaps. | [optional] 
**environment** | [**IoFissionV1FunctionSpecEnvironment**](IoFissionV1FunctionSpecEnvironment.md) |  | 
**function_timeout** | **int** | FunctionTimeout provides a maximum amount of duration within which a request for a particular function execution should be complete. This is optional. If not specified default value will be taken as 60s | [optional] 
**idletimeout** | **int** | IdleTimeout specifies the length of time that a function is idle before the function pod(s) are eligible for deletion. If no traffic to the function is detected within the idle timeout, the executor will then recycle the function pod(s) to release resources. | [optional] 
**once_only** | **bool** | OnceOnly specifies if specialized pod will serve exactly one request in its lifetime and would be garbage collected after serving that one request This is optional. If not specified default value will be taken as false | [optional] 
**package** | [**IoFissionV1FunctionSpecPackage**](IoFissionV1FunctionSpecPackage.md) |  | 
**podspec** | [**IoFissionV1FunctionSpecPodspec**](IoFissionV1FunctionSpecPodspec.md) |  | [optional] 
**requests_per_pod** | **int** | RequestsPerPod indicates the maximum number of concurrent requests that can be served by a specialized pod This is optional. If not specified default value will be taken as 1 | [optional] 
**resources** | [**IoFissionV1FunctionSpecResources**](IoFissionV1FunctionSpecResources.md) |  | [optional] 
**retain_pods** | **int** | RetainPods specifies the number of specialized pods that should be retained after serving requests This is optional. If not specified default value will be taken as 0 | [optional] 
**secrets** | **object** | Reference to a list of secrets. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_function_spec import IoFissionV1FunctionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1FunctionSpec from a JSON string
io_fission_v1_function_spec_instance = IoFissionV1FunctionSpec.from_json(json)
# print the JSON string representation of the object
print IoFissionV1FunctionSpec.to_json()

# convert the object into a dict
io_fission_v1_function_spec_dict = io_fission_v1_function_spec_instance.to_dict()
# create an instance of IoFissionV1FunctionSpec from a dict
io_fission_v1_function_spec_form_dict = io_fission_v1_function_spec.from_dict(io_fission_v1_function_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


