# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerQuobyte

quobyte represents a Quobyte mount on the host that shares a pod's lifetime

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | group to map volume access to Default is no group | [optional] 
**read_only** | **bool** | readOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false. | [optional] 
**registry** | **str** | registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes | 
**tenant** | **str** | tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin | [optional] 
**user** | **str** | user to map volume access to Defaults to serivceaccount user | [optional] 
**volume** | **str** | volume is a string that references an already created Quobyte volume by name. | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_quobyte import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerQuobyte

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerQuobyte from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_quobyte_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerQuobyte.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerQuobyte.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_quobyte_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_quobyte_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerQuobyte from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_quobyte_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_quobyte.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_quobyte_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


