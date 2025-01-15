# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerFieldRef

Required: Selects a field of the pod: only annotations, labels, name, namespace and uid are supported.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | Version of the schema the FieldPath is written in terms of, defaults to \&quot;v1\&quot;. | [optional] 
**field_path** | **str** | Path of the field to select in the specified API version. | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_items_inner_field_ref import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerFieldRef

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerFieldRef from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_items_inner_field_ref_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerFieldRef.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerFieldRef.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_items_inner_field_ref_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_items_inner_field_ref_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerFieldRef from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_items_inner_field_ref_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_items_inner_field_ref.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_items_inner_field_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


