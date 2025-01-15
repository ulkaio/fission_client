# IoK8sApimachineryPkgApisMetaV1APIGroup

APIGroup contains the name, the supported versions, and the preferred version of a group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**name** | **str** | name is the name of the group. | 
**preferred_version** | [**IoK8sApimachineryPkgApisMetaV1GroupVersionForDiscovery**](IoK8sApimachineryPkgApisMetaV1GroupVersionForDiscovery.md) |  | [optional] 
**server_address_by_client_cidrs** | [**List[IoK8sApimachineryPkgApisMetaV1ServerAddressByClientCIDR]**](IoK8sApimachineryPkgApisMetaV1ServerAddressByClientCIDR.md) | a map of client CIDR to server address that is serving this group. This is to help clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the client can match. For example: the master will return an internal IP CIDR only, if the client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the client IP. | [optional] 
**versions** | [**List[IoK8sApimachineryPkgApisMetaV1GroupVersionForDiscovery]**](IoK8sApimachineryPkgApisMetaV1GroupVersionForDiscovery.md) | versions are the versions supported in this group. | 

## Example

```python
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_group import IoK8sApimachineryPkgApisMetaV1APIGroup

# TODO update the JSON string below
json = "{}"
# create an instance of IoK8sApimachineryPkgApisMetaV1APIGroup from a JSON string
io_k8s_apimachinery_pkg_apis_meta_v1_api_group_instance = IoK8sApimachineryPkgApisMetaV1APIGroup.from_json(json)
# print the JSON string representation of the object
print IoK8sApimachineryPkgApisMetaV1APIGroup.to_json()

# convert the object into a dict
io_k8s_apimachinery_pkg_apis_meta_v1_api_group_dict = io_k8s_apimachinery_pkg_apis_meta_v1_api_group_instance.to_dict()
# create an instance of IoK8sApimachineryPkgApisMetaV1APIGroup from a dict
io_k8s_apimachinery_pkg_apis_meta_v1_api_group_form_dict = io_k8s_apimachinery_pkg_apis_meta_v1_api_group.from_dict(io_k8s_apimachinery_pkg_apis_meta_v1_api_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


