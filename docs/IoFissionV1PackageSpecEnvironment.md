# IoFissionV1PackageSpecEnvironment

Environment is a reference to the environment for building source archive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**namespace** | **str** |  | 

## Example

```python
from fission_client.models.io_fission_v1_package_spec_environment import IoFissionV1PackageSpecEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1PackageSpecEnvironment from a JSON string
io_fission_v1_package_spec_environment_instance = IoFissionV1PackageSpecEnvironment.from_json(json)
# print the JSON string representation of the object
print IoFissionV1PackageSpecEnvironment.to_json()

# convert the object into a dict
io_fission_v1_package_spec_environment_dict = io_fission_v1_package_spec_environment_instance.to_dict()
# create an instance of IoFissionV1PackageSpecEnvironment from a dict
io_fission_v1_package_spec_environment_form_dict = io_fission_v1_package_spec_environment.from_dict(io_fission_v1_package_spec_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


