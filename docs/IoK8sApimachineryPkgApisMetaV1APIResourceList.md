# IoK8sApimachineryPkgApisMetaV1APIResourceList

APIResourceList is a list of APIResource, it is used to expose the name of the resources supported in a specific group and version, and if the resource is namespaced.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**group_version** | **str** | groupVersion is the group and version this APIResourceList is for. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**resources** | [**List[IoK8sApimachineryPkgApisMetaV1APIResource]**](IoK8sApimachineryPkgApisMetaV1APIResource.md) | resources contains the name of the resources and if they are namespaced. | 

## Example

```python
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list import IoK8sApimachineryPkgApisMetaV1APIResourceList

# TODO update the JSON string below
json = "{}"
# create an instance of IoK8sApimachineryPkgApisMetaV1APIResourceList from a JSON string
io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list_instance = IoK8sApimachineryPkgApisMetaV1APIResourceList.from_json(json)
# print the JSON string representation of the object
print IoK8sApimachineryPkgApisMetaV1APIResourceList.to_json()

# convert the object into a dict
io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list_dict = io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list_instance.to_dict()
# create an instance of IoK8sApimachineryPkgApisMetaV1APIResourceList from a dict
io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list_form_dict = io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list.from_dict(io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


