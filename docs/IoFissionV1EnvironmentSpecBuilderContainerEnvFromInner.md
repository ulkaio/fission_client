# IoFissionV1EnvironmentSpecBuilderContainerEnvFromInner

EnvFromSource represents the source of a set of ConfigMaps

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_map_ref** | [**IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerConfigMapRef**](IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerConfigMapRef.md) |  | [optional] 
**prefix** | **str** | An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER. | [optional] 
**secret_ref** | [**IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerSecretRef**](IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerSecretRef.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_env_from_inner import IoFissionV1EnvironmentSpecBuilderContainerEnvFromInner

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerEnvFromInner from a JSON string
io_fission_v1_environment_spec_builder_container_env_from_inner_instance = IoFissionV1EnvironmentSpecBuilderContainerEnvFromInner.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerEnvFromInner.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_env_from_inner_dict = io_fission_v1_environment_spec_builder_container_env_from_inner_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerEnvFromInner from a dict
io_fission_v1_environment_spec_builder_container_env_from_inner_form_dict = io_fission_v1_environment_spec_builder_container_env_from_inner.from_dict(io_fission_v1_environment_spec_builder_container_env_from_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


