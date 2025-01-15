# IoK8sApimachineryPkgApisMetaV1ServerAddressByClientCIDR

ServerAddressByClientCIDR helps the client to determine the server address that they should use, depending on the clientCIDR that they match.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_cidr** | **str** | The CIDR with which clients can match their IP to figure out the server address that they should use. | 
**server_address** | **str** | Address of this server, suitable for a client that matches the above CIDR. This can be a hostname, hostname:port, IP or IP:port. | 

## Example

```python
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_server_address_by_client_cidr import IoK8sApimachineryPkgApisMetaV1ServerAddressByClientCIDR

# TODO update the JSON string below
json = "{}"
# create an instance of IoK8sApimachineryPkgApisMetaV1ServerAddressByClientCIDR from a JSON string
io_k8s_apimachinery_pkg_apis_meta_v1_server_address_by_client_cidr_instance = IoK8sApimachineryPkgApisMetaV1ServerAddressByClientCIDR.from_json(json)
# print the JSON string representation of the object
print IoK8sApimachineryPkgApisMetaV1ServerAddressByClientCIDR.to_json()

# convert the object into a dict
io_k8s_apimachinery_pkg_apis_meta_v1_server_address_by_client_cidr_dict = io_k8s_apimachinery_pkg_apis_meta_v1_server_address_by_client_cidr_instance.to_dict()
# create an instance of IoK8sApimachineryPkgApisMetaV1ServerAddressByClientCIDR from a dict
io_k8s_apimachinery_pkg_apis_meta_v1_server_address_by_client_cidr_form_dict = io_k8s_apimachinery_pkg_apis_meta_v1_server_address_by_client_cidr.from_dict(io_k8s_apimachinery_pkg_apis_meta_v1_server_address_by_client_cidr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


