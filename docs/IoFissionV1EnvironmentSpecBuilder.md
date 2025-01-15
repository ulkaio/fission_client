# IoFissionV1EnvironmentSpecBuilder

(Optional) Builder is configuration for builder manager to launch environment builder to build source code into deployable binary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** | (Optional) Default build command to run for this build environment. | [optional] 
**container** | [**IoFissionV1EnvironmentSpecBuilderContainer**](IoFissionV1EnvironmentSpecBuilderContainer.md) |  | [optional] 
**image** | **str** | Image for containing the language compilation environment. | [optional] 
**podspec** | [**IoFissionV1EnvironmentSpecBuilderPodspec**](IoFissionV1EnvironmentSpecBuilderPodspec.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder import IoFissionV1EnvironmentSpecBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilder from a JSON string
io_fission_v1_environment_spec_builder_instance = IoFissionV1EnvironmentSpecBuilder.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilder.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_dict = io_fission_v1_environment_spec_builder_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilder from a dict
io_fission_v1_environment_spec_builder_form_dict = io_fission_v1_environment_spec_builder.from_dict(io_fission_v1_environment_spec_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


