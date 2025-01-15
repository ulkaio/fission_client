# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerScaleIO

scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_type** | **str** | fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \&quot;ext4\&quot;, \&quot;xfs\&quot;, \&quot;ntfs\&quot;. Default is \&quot;xfs\&quot;. | [optional] 
**gateway** | **str** | gateway is the host address of the ScaleIO API Gateway. | 
**protection_domain** | **str** | protectionDomain is the name of the ScaleIO Protection Domain for the configured storage. | [optional] 
**read_only** | **bool** | readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 
**secret_ref** | [**IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerScaleIOSecretRef**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerScaleIOSecretRef.md) |  | 
**ssl_enabled** | **bool** | sslEnabled Flag enable/disable SSL communication with Gateway, default false | [optional] 
**storage_mode** | **str** | storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned. | [optional] 
**storage_pool** | **str** | storagePool is the ScaleIO Storage Pool associated with the protection domain. | [optional] 
**system** | **str** | system is the name of the storage system as configured in ScaleIO. | 
**volume_name** | **str** | volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_scale_io import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerScaleIO

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerScaleIO from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_scale_io_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerScaleIO.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerScaleIO.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_scale_io_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_scale_io_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerScaleIO from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_scale_io_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_scale_io.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_scale_io_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


