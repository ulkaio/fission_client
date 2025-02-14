# IoK8sApimachineryPkgApisMetaV1Status

Status is a return value for calls that don't return other objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**code** | **int** | Suggested HTTP return code for this status, 0 if not set. | [optional] 
**details** | [**IoK8sApimachineryPkgApisMetaV1StatusDetails**](IoK8sApimachineryPkgApisMetaV1StatusDetails.md) |  | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**message** | **str** | A human-readable description of the status of this operation. | [optional] 
**metadata** | [**IoK8sApimachineryPkgApisMetaV1ListMeta**](IoK8sApimachineryPkgApisMetaV1ListMeta.md) |  | [optional] 
**reason** | **str** | A machine-readable description of why this operation is in the \&quot;Failure\&quot; status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it. | [optional] 
**status** | **str** | Status of the operation. One of: \&quot;Success\&quot; or \&quot;Failure\&quot;. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status | [optional] 

## Example

```python
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_status import IoK8sApimachineryPkgApisMetaV1Status

# TODO update the JSON string below
json = "{}"
# create an instance of IoK8sApimachineryPkgApisMetaV1Status from a JSON string
io_k8s_apimachinery_pkg_apis_meta_v1_status_instance = IoK8sApimachineryPkgApisMetaV1Status.from_json(json)
# print the JSON string representation of the object
print IoK8sApimachineryPkgApisMetaV1Status.to_json()

# convert the object into a dict
io_k8s_apimachinery_pkg_apis_meta_v1_status_dict = io_k8s_apimachinery_pkg_apis_meta_v1_status_instance.to_dict()
# create an instance of IoK8sApimachineryPkgApisMetaV1Status from a dict
io_k8s_apimachinery_pkg_apis_meta_v1_status_form_dict = io_k8s_apimachinery_pkg_apis_meta_v1_status.from_dict(io_k8s_apimachinery_pkg_apis_meta_v1_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


