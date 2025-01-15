# IoFissionV1FunctionSpecPackagePackageref

Package reference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**resourceversion** | **str** | Including resource version in the reference forces the function to be updated on package update, making it possible to cache the function based on its metadata. | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_function_spec_package_packageref import IoFissionV1FunctionSpecPackagePackageref

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1FunctionSpecPackagePackageref from a JSON string
io_fission_v1_function_spec_package_packageref_instance = IoFissionV1FunctionSpecPackagePackageref.from_json(json)
# print the JSON string representation of the object
print IoFissionV1FunctionSpecPackagePackageref.to_json()

# convert the object into a dict
io_fission_v1_function_spec_package_packageref_dict = io_fission_v1_function_spec_package_packageref_instance.to_dict()
# create an instance of IoFissionV1FunctionSpecPackagePackageref from a dict
io_fission_v1_function_spec_package_packageref_form_dict = io_fission_v1_function_spec_package_packageref.from_dict(io_fission_v1_function_spec_package_packageref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


