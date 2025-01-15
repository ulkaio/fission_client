# IoK8sApimachineryPkgApisMetaV1DeleteOptions

DeleteOptions may be provided when deleting an API object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**dry_run** | **List[str]** | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional] 
**grace_period_seconds** | **int** | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**orphan_dependents** | **bool** | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
**preconditions** | [**IoK8sApimachineryPkgApisMetaV1Preconditions**](IoK8sApimachineryPkgApisMetaV1Preconditions.md) |  | [optional] 
**propagation_policy** | **str** | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional] 

## Example

```python
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_delete_options import IoK8sApimachineryPkgApisMetaV1DeleteOptions

# TODO update the JSON string below
json = "{}"
# create an instance of IoK8sApimachineryPkgApisMetaV1DeleteOptions from a JSON string
io_k8s_apimachinery_pkg_apis_meta_v1_delete_options_instance = IoK8sApimachineryPkgApisMetaV1DeleteOptions.from_json(json)
# print the JSON string representation of the object
print IoK8sApimachineryPkgApisMetaV1DeleteOptions.to_json()

# convert the object into a dict
io_k8s_apimachinery_pkg_apis_meta_v1_delete_options_dict = io_k8s_apimachinery_pkg_apis_meta_v1_delete_options_instance.to_dict()
# create an instance of IoK8sApimachineryPkgApisMetaV1DeleteOptions from a dict
io_k8s_apimachinery_pkg_apis_meta_v1_delete_options_form_dict = io_k8s_apimachinery_pkg_apis_meta_v1_delete_options.from_dict(io_k8s_apimachinery_pkg_apis_meta_v1_delete_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


