# IoK8sApimachineryPkgApisMetaV1APIGroupList

APIGroupList is a list of APIGroup, to allow clients to discover the API at /apis.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**groups** | [**List[IoK8sApimachineryPkgApisMetaV1APIGroup]**](IoK8sApimachineryPkgApisMetaV1APIGroup.md) | groups is a list of APIGroup. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 

## Example

```python
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_group_list import IoK8sApimachineryPkgApisMetaV1APIGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of IoK8sApimachineryPkgApisMetaV1APIGroupList from a JSON string
io_k8s_apimachinery_pkg_apis_meta_v1_api_group_list_instance = IoK8sApimachineryPkgApisMetaV1APIGroupList.from_json(json)
# print the JSON string representation of the object
print IoK8sApimachineryPkgApisMetaV1APIGroupList.to_json()

# convert the object into a dict
io_k8s_apimachinery_pkg_apis_meta_v1_api_group_list_dict = io_k8s_apimachinery_pkg_apis_meta_v1_api_group_list_instance.to_dict()
# create an instance of IoK8sApimachineryPkgApisMetaV1APIGroupList from a dict
io_k8s_apimachinery_pkg_apis_meta_v1_api_group_list_form_dict = io_k8s_apimachinery_pkg_apis_meta_v1_api_group_list.from_dict(io_k8s_apimachinery_pkg_apis_meta_v1_api_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


