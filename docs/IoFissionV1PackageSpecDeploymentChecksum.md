# IoFissionV1PackageSpecDeploymentChecksum

Checksum ensures the integrity of packages referenced by URL. Ignored for literals.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sum** | **str** |  | [optional] 
**type** | **str** | ChecksumType specifies the checksum algorithm, such as sha256, used for a checksum. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_package_spec_deployment_checksum import IoFissionV1PackageSpecDeploymentChecksum

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1PackageSpecDeploymentChecksum from a JSON string
io_fission_v1_package_spec_deployment_checksum_instance = IoFissionV1PackageSpecDeploymentChecksum.from_json(json)
# print the JSON string representation of the object
print IoFissionV1PackageSpecDeploymentChecksum.to_json()

# convert the object into a dict
io_fission_v1_package_spec_deployment_checksum_dict = io_fission_v1_package_spec_deployment_checksum_instance.to_dict()
# create an instance of IoFissionV1PackageSpecDeploymentChecksum from a dict
io_fission_v1_package_spec_deployment_checksum_form_dict = io_fission_v1_package_spec_deployment_checksum.from_dict(io_fission_v1_package_spec_deployment_checksum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


