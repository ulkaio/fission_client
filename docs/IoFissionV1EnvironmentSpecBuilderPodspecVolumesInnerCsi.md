# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCsi

csi (Container Storage Interface) represents ephemeral storage that is handled by certain external CSI drivers (Beta feature).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver** | **str** | driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster. | 
**fs_type** | **str** | fsType to mount. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply. | [optional] 
**node_publish_secret_ref** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCsiNodePublishSecretRef**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCsiNodePublishSecretRef.md) |  | [optional] 
**read_only** | **bool** | readOnly specifies a read-only configuration for the volume. Defaults to false (read/write). | [optional] 
**volume_attributes** | **Dict[str, str]** | volumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver&#39;s documentation for supported values. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_csi import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCsi

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCsi from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_csi_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCsi.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCsi.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_csi_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_csi_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCsi from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_csi_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_csi.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_csi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


