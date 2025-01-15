# IoFissionV1PackageStatus

Status indicates the build status of package.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buildlog** | **str** | BuildLog stores build log during the compilation. | [optional] 
**buildstatus** | **str** | BuildStatus is the package build status. | [optional] 
**last_update_timestamp** | **object** | LastUpdateTimestamp will store the timestamp the package was last updated metav1.Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. https://github.com/kubernetes/apimachinery/blob/44bd77c24ef93cd3a5eb6fef64e514025d10d44e/pkg/apis/meta/v1/time.go#L26-L35 | [optional] 

## Example

```python
from fission_client.models.io_fission_v1_package_status import IoFissionV1PackageStatus

# TODO update the JSON string below
json = "{}"
# create an instance of IoFissionV1PackageStatus from a JSON string
io_fission_v1_package_status_instance = IoFissionV1PackageStatus.from_json(json)
# print the JSON string representation of the object
print IoFissionV1PackageStatus.to_json()

# convert the object into a dict
io_fission_v1_package_status_dict = io_fission_v1_package_status_instance.to_dict()
# create an instance of IoFissionV1PackageStatus from a dict
io_fission_v1_package_status_form_dict = io_fission_v1_package_status.from_dict(io_fission_v1_package_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


