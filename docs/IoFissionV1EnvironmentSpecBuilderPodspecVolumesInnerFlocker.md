# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlocker

flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_name** | **str** | datasetName is Name of the dataset stored as metadata -&gt; name on the dataset for Flocker should be considered as deprecated | [optional] 
**dataset_uuid** | **str** | datasetUUID is the UUID of the dataset. This is unique identifier of a Flocker dataset | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_flocker import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlocker

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlocker from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_flocker_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlocker.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlocker.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_flocker_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_flocker_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlocker from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_flocker_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_flocker.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_flocker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


