# IoFissionV1EnvironmentSpecBuilderContainerVolumeDevicesInner

volumeDevice describes a mapping of a raw block device within a container.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_path** | **str** | devicePath is the path inside of the container that the device will be mapped to. | 
**name** | **str** | name must match the name of a persistentVolumeClaim in the pod | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_container_volume_devices_inner import IoFissionV1EnvironmentSpecBuilderContainerVolumeDevicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerVolumeDevicesInner from a JSON string
io_fission_v1_environment_spec_builder_container_volume_devices_inner_instance = IoFissionV1EnvironmentSpecBuilderContainerVolumeDevicesInner.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderContainerVolumeDevicesInner.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_container_volume_devices_inner_dict = io_fission_v1_environment_spec_builder_container_volume_devices_inner_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderContainerVolumeDevicesInner from a dict
io_fission_v1_environment_spec_builder_container_volume_devices_inner_form_dict = io_fission_v1_environment_spec_builder_container_volume_devices_inner.from_dict(io_fission_v1_environment_spec_builder_container_volume_devices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


