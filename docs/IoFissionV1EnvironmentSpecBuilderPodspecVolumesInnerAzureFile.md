# IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerAzureFile

azureFile represents an Azure File Service mount on the host and bind mount to the pod.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_only** | **bool** | readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. | [optional] 
**secret_name** | **str** | secretName is the  name of secret that contains Azure Storage Account Name and Key | 
**share_name** | **str** | shareName is the azure share Name | 

## Example

```python
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_azure_file import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerAzureFile

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerAzureFile from a JSON string
io_fission_v1_environment_spec_builder_podspec_volumes_inner_azure_file_instance = IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerAzureFile.from_json(json)
# print the JSON string representation of the object
print IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerAzureFile.to_json()

# convert the object into a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_azure_file_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_azure_file_instance.to_dict()
# create an instance of IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerAzureFile from a dict
io_fission_v1_environment_spec_builder_podspec_volumes_inner_azure_file_form_dict = io_fission_v1_environment_spec_builder_podspec_volumes_inner_azure_file.from_dict(io_fission_v1_environment_spec_builder_podspec_volumes_inner_azure_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


