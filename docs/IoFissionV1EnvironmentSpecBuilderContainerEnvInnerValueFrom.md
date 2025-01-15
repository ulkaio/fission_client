# IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFrom

Source for the environment variable's value. Cannot be used if value is not empty.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_map_key_ref** | [**IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromConfigMapKeyRef**](IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromConfigMapKeyRef.md) |  | [optional] 
**field_ref** | [**IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromFieldRef**](IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromFieldRef.md) |  | [optional] 
**resource_field_ref** | [**IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromResourceFieldRef**](IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromResourceFieldRef.md) |  | [optional] 
**secret_key_ref** | [**IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromSecretKeyRef**](IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromSecretKeyRef.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_env_inner_value_from import IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFrom

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFrom from a JSON string
io_fission_v1_environment_spec_builder_container_env_inner_value_from_instance = IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFrom.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFrom.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_env_inner_value_from_dict = io_fission_v1_environment_spec_builder_container_env_inner_value_from_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFrom from a dict
io_fission_v1_environment_spec_builder_container_env_inner_value_from_form_dict = io_fission_v1_environment_spec_builder_container_env_inner_value_from.from_dict(io_fission_v1_environment_spec_builder_container_env_inner_value_from_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


