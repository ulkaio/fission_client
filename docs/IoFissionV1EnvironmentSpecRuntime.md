# IoFissionV1EnvironmentSpecRuntime

Runtime is configuration for running function, like container image etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | [**IoFissionV1EnvironmentSpecRuntimeContainer**](IoFissionV1EnvironmentSpecRuntimeContainer.md) |  | [optional] 
**image** | **str** | Image for containing the language runtime. | 
**podspec** | [**IoFissionV1EnvironmentSpecRuntimePodspec**](IoFissionV1EnvironmentSpecRuntimePodspec.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_runtime import IoFissionV1EnvironmentSpecRuntime

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecRuntime from a JSON string
io_fission_v1_environment_spec_runtime_instance = IoFissionV1EnvironmentSpecRuntime.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecRuntime.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_runtime_dict = io_fission_v1_environment_spec_runtime_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecRuntime from a dict
io_fission_v1_environment_spec_runtime_form_dict = io_fission_v1_environment_spec_runtime.from_dict(io_fission_v1_environment_spec_runtime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


