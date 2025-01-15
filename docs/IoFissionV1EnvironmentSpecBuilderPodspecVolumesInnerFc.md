# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFc

fc represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_type** | **str** | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Implicitly inferred to be \&quot;ext4\&quot; if unspecified. | [optional] 
**lun** | **int** | lun is Optional: FC target lun number | [optional] 
**read_only** | **bool** | readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 
**target_wwns** | **List[str]** | targetWWNs is Optional: FC target worldwide names (WWNs) | [optional] 
**wwids** | **List[str]** | wwids Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_fc import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFc

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFc from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_fc_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFc.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFc.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_fc_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_fc_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFc from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_fc_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_fc.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_fc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


