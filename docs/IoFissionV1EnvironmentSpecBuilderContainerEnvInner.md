# IoFissionV1EnvironmentSpecBuilderContainerEnvInner

EnvVar represents an environment variable present in a Container.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the environment variable. Must be a C_IDENTIFIER. | 
**value** | **str** | Variable references $(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \&quot;$$(VAR_NAME)\&quot; will produce the string literal \&quot;$(VAR_NAME)\&quot;. Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to \&quot;\&quot;. | [optional] 
**value_from** | [**IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFrom**](IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFrom.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_env_inner import IoFissionV1EnvironmentSpecBuilderContainerEnvInner

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerEnvInner from a JSON string
io_fission_v1_environment_spec_builder_container_env_inner_instance = IoFissionV1EnvironmentSpecBuilderContainerEnvInner.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerEnvInner.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_env_inner_dict = io_fission_v1_environment_spec_builder_container_env_inner_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerEnvInner from a dict
io_fission_v1_environment_spec_builder_container_env_inner_form_dict = io_fission_v1_environment_spec_builder_container_env_inner.from_dict(io_fission_v1_environment_spec_builder_container_env_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


