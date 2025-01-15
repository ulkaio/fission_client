# IoFissionV1EnvironmentSpecBuilderContainerResourcesClaimsInner

ResourceClaim references one entry in PodSpec.ResourceClaims.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container. | 
**request** | **str** | Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_resources_claims_inner import IoFissionV1EnvironmentSpecBuilderContainerResourcesClaimsInner

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerResourcesClaimsInner from a JSON string
io_fission_v1_environment_spec_builder_container_resources_claims_inner_instance = IoFissionV1EnvironmentSpecBuilderContainerResourcesClaimsInner.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerResourcesClaimsInner.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_resources_claims_inner_dict = io_fission_v1_environment_spec_builder_container_resources_claims_inner_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerResourcesClaimsInner from a dict
io_fission_v1_environment_spec_builder_container_resources_claims_inner_form_dict = io_fission_v1_environment_spec_builder_container_resources_claims_inner.from_dict(io_fission_v1_environment_spec_builder_container_resources_claims_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


