# IoK8sApimachineryPkgApisMetaV1Preconditions

Preconditions must be fulfilled before an operation (update, delete, etc.) is carried out.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_version** | **str** | Specifies the target ResourceVersion | [optional] 
**uid** | **str** | Specifies the target UID. | [optional] 

## Example

```python
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_preconditions import IoK8sApimachineryPkgApisMetaV1Preconditions

# TODO update the JSON string below
json = "{}"
# create an instance of IoK8sApimachineryPkgApisMetaV1Preconditions from a JSON string
io_k8s_apimachinery_pkg_apis_meta_v1_preconditions_instance = IoK8sApimachineryPkgApisMetaV1Preconditions.from_json(json)
# print the JSON string representation of the object
print IoK8sApimachineryPkgApisMetaV1Preconditions.to_json()

# convert the object into a dict
io_k8s_apimachinery_pkg_apis_meta_v1_preconditions_dict = io_k8s_apimachinery_pkg_apis_meta_v1_preconditions_instance.to_dict()
# create an instance of IoK8sApimachineryPkgApisMetaV1Preconditions from a dict
io_k8s_apimachinery_pkg_apis_meta_v1_preconditions_form_dict = io_k8s_apimachinery_pkg_apis_meta_v1_preconditions.from_dict(io_k8s_apimachinery_pkg_apis_meta_v1_preconditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


