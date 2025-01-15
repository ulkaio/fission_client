# IoK8sApimachineryPkgVersionInfo

Info contains versioning information. how we'll want to distribute that information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_date** | **str** |  | 
**compiler** | **str** |  | 
**git_commit** | **str** |  | 
**git_tree_state** | **str** |  | 
**git_version** | **str** |  | 
**go_version** | **str** |  | 
**major** | **str** |  | 
**minor** | **str** |  | 
**platform** | **str** |  | 

## Example

```python
from fission_client.models.io_k8s_apimachinery_pkg_version_info import IoK8sApimachineryPkgVersionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IoK8sApimachineryPkgVersionInfo from a JSON string
io_k8s_apimachinery_pkg_version_info_instance = IoK8sApimachineryPkgVersionInfo.from_json(json)
# print the JSON string representation of the object
print IoK8sApimachineryPkgVersionInfo.to_json()

# convert the object into a dict
io_k8s_apimachinery_pkg_version_info_dict = io_k8s_apimachinery_pkg_version_info_instance.to_dict()
# create an instance of IoK8sApimachineryPkgVersionInfo from a dict
io_k8s_apimachinery_pkg_version_info_form_dict = io_k8s_apimachinery_pkg_version_info.from_dict(io_k8s_apimachinery_pkg_version_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


