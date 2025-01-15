# IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromSecretKeyRef

Selects a key of a secret in the pod's namespace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the secret to select from.  Must be a valid secret key. | 
**name** | **str** | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | [optional] 
**optional** | **bool** | Specify whether the Secret or its key must be defined | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_env_inner_value_from_secret_key_ref import IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromSecretKeyRef

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromSecretKeyRef from a JSON string
io_fission_v1_environment_spec_builder_container_env_inner_value_from_secret_key_ref_instance = IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromSecretKeyRef.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromSecretKeyRef.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_env_inner_value_from_secret_key_ref_dict = io_fission_v1_environment_spec_builder_container_env_inner_value_from_secret_key_ref_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromSecretKeyRef from a dict
io_fission_v1_environment_spec_builder_container_env_inner_value_from_secret_key_ref_form_dict = io_fission_v1_environment_spec_builder_container_env_inner_value_from_secret_key_ref.from_dict(io_fission_v1_environment_spec_builder_container_env_inner_value_from_secret_key_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


