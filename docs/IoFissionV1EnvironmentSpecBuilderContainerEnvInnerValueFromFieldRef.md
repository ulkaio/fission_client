# IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromFieldRef

Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | Version of the schema the FieldPath is written in terms of, defaults to \&quot;v1\&quot;. | [optional] 
**field_path** | **str** | Path of the field to select in the specified API version. | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_env_inner_value_from_field_ref import IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromFieldRef

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromFieldRef from a JSON string
io_fission_v1_environment_spec_builder_container_env_inner_value_from_field_ref_instance = IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromFieldRef.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromFieldRef.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_env_inner_value_from_field_ref_dict = io_fission_v1_environment_spec_builder_container_env_inner_value_from_field_ref_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromFieldRef from a dict
io_fission_v1_environment_spec_builder_container_env_inner_value_from_field_ref_form_dict = io_fission_v1_environment_spec_builder_container_env_inner_value_from_field_ref.from_dict(io_fission_v1_environment_spec_builder_container_env_inner_value_from_field_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


