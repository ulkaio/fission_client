# IoFissionV1PackageSpecSource

Source is the archive contains source code and dependencies file. If the package status is in PENDING state, builder manager will then notify builder to compile source and save the result as deployable archive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checksum** | [**IoFissionV1PackageSpecDeploymentChecksum**](IoFissionV1PackageSpecDeploymentChecksum.md) |  | [optional] 
**literal** | **bytearray** | Literal contents of the package. Can be used for encoding packages below TODO (256 KB?) size. | [optional] 
**type** | **str** | Type defines how the package is specified: literal or URL. Available value:  - literal  - url | [optional] 
**url** | **str** | URL references a package. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_package_spec_source import IoFissionV1PackageSpecSource

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1PackageSpecSource from a JSON string
io_fission_v1_package_spec_source_instance = IoFissionV1PackageSpecSource.from_json(json)
# print the JSON string representation of the object
print IoFissionV1PackageSpecSource.to_json()

# convert the object into a dict
io_fission_v1_package_spec_source_dict = io_fission_v1_package_spec_source_instance.to_dict()
# create an instance of IoFissionV1PackageSpecSource from a dict
io_fission_v1_package_spec_source_form_dict = io_fission_v1_package_spec_source.from_dict(io_fission_v1_package_spec_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


