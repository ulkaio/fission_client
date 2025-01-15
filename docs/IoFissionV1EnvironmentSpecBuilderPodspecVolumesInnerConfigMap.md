# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerConfigMap

configMap represents a configMap that should populate this volume

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_mode** | **int** | defaultMode is optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. | [optional] 
**items** | [**List[IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerConfigMapItemsInner]**](IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerConfigMapItemsInner.md) | items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the &#39;..&#39; path or start with &#39;..&#39;. | [optional] 
**name** | **str** | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | [optional] 
**optional** | **bool** | optional specify whether the ConfigMap or its keys must be defined | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_config_map import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerConfigMap

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerConfigMap from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_config_map_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerConfigMap.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerConfigMap.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_config_map_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_config_map_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerConfigMap from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_config_map_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_config_map.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_config_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


