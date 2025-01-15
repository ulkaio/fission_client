# IoK8sApimachineryPkgApisMetaV1GroupVersionForDiscovery

GroupVersion contains the \"group/version\" and \"version\" string of a version. It is made a struct to keep extensibility.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_version** | **str** | groupVersion specifies the API group and version in the form \&quot;group/version\&quot; | 
**version** | **str** | version specifies the version in the form of \&quot;version\&quot;. This is to save the clients the trouble of splitting the GroupVersion. | 

## Example

```python
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_group_version_for_discovery import IoK8sApimachineryPkgApisMetaV1GroupVersionForDiscovery

# TODO update the JSON string below
json = "{}"
# create an instance of IoK8sApimachineryPkgApisMetaV1GroupVersionForDiscovery from a JSON string
io_k8s_apimachinery_pkg_apis_meta_v1_group_version_for_discovery_instance = IoK8sApimachineryPkgApisMetaV1GroupVersionForDiscovery.from_json(json)
# print the JSON string representation of the object
print IoK8sApimachineryPkgApisMetaV1GroupVersionForDiscovery.to_json()

# convert the object into a dict
io_k8s_apimachinery_pkg_apis_meta_v1_group_version_for_discovery_dict = io_k8s_apimachinery_pkg_apis_meta_v1_group_version_for_discovery_instance.to_dict()
# create an instance of IoK8sApimachineryPkgApisMetaV1GroupVersionForDiscovery from a dict
io_k8s_apimachinery_pkg_apis_meta_v1_group_version_for_discovery_form_dict = io_k8s_apimachinery_pkg_apis_meta_v1_group_version_for_discovery.from_dict(io_k8s_apimachinery_pkg_apis_meta_v1_group_version_for_discovery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


