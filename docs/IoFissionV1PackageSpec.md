# IoFissionV1PackageSpec

PackageSpec includes source/deploy archives and the reference of environment to build the package.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buildcmd** | **str** | BuildCommand is a custom build command that builder used to build the source archive. | [optional] 
**deployment** | [**IoFissionV1PackageSpecDeployment**](IoFissionV1PackageSpecDeployment.md) |  | [optional] 
**environment** | [**IoFissionV1PackageSpecEnvironment**](IoFissionV1PackageSpecEnvironment.md) |  | 
**source** | [**IoFissionV1PackageSpecSource**](IoFissionV1PackageSpecSource.md) |  | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_package_spec import IoFissionV1PackageSpec

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1PackageSpec from a JSON string
io_fission_v1_package_spec_instance = IoFissionV1PackageSpec.from_json(json)
# print the JSON string representation of the object
print IoFissionV1PackageSpec.to_json()

# convert the object into a dict
io_fission_v1_package_spec_dict = io_fission_v1_package_spec_instance.to_dict()
# create an instance of IoFissionV1PackageSpec from a dict
io_fission_v1_package_spec_form_dict = io_fission_v1_package_spec.from_dict(io_fission_v1_package_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


