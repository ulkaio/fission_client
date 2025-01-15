# IoFissionV1EnvironmentSpecBuilderContainerResources

Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claims** | [**List[IoFissionV1EnvironmentSpecBuilderContainerResourcesClaimsInner]**](IoFissionV1EnvironmentSpecBuilderContainerResourcesClaimsInner.md) | Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.  This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.  This field is immutable. It can only be set for containers. | [optional] 
**limits** | **Dict[str, object]** | Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | [optional] 
**requests** | **Dict[str, object]** | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_resources import IoFissionV1EnvironmentSpecBuilderContainerResources

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerResources from a JSON string
io_fission_v1_environment_spec_builder_container_resources_instance = IoFissionV1EnvironmentSpecBuilderContainerResources.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerResources.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_resources_dict = io_fission_v1_environment_spec_builder_container_resources_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerResources from a dict
io_fission_v1_environment_spec_builder_container_resources_form_dict = io_fission_v1_environment_spec_builder_container_resources.from_dict(io_fission_v1_environment_spec_builder_container_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


