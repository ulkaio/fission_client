# IoK8sApimachineryPkgApisMetaV1WatchEvent

Event represents a single event to a watched resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **object** | RawExtension is used to hold extensions in external versions.  To use this, make a field which has RawExtension as its type in your external, versioned struct, and Object in your internal struct. You also need to register your various plugin types.  // Internal package:   type MyAPIObject struct {   runtime.TypeMeta &#x60;json:\&quot;,inline\&quot;&#x60;   MyPlugin runtime.Object &#x60;json:\&quot;myPlugin\&quot;&#x60;  }   type PluginA struct {   AOption string &#x60;json:\&quot;aOption\&quot;&#x60;  }  // External package:   type MyAPIObject struct {   runtime.TypeMeta &#x60;json:\&quot;,inline\&quot;&#x60;   MyPlugin runtime.RawExtension &#x60;json:\&quot;myPlugin\&quot;&#x60;  }   type PluginA struct {   AOption string &#x60;json:\&quot;aOption\&quot;&#x60;  }  // On the wire, the JSON will look something like this:   {   \&quot;kind\&quot;:\&quot;MyAPIObject\&quot;,   \&quot;apiVersion\&quot;:\&quot;v1\&quot;,   \&quot;myPlugin\&quot;: {    \&quot;kind\&quot;:\&quot;PluginA\&quot;,    \&quot;aOption\&quot;:\&quot;foo\&quot;,   },  }  So what happens? Decode first uses json or yaml to unmarshal the serialized data into your external MyAPIObject. That causes the raw JSON to be stored, but not unpacked. The next step is to copy (using pkg/conversion) into the internal struct. The runtime package&#39;s DefaultScheme has conversion functions installed which will unpack the JSON stored in RawExtension, turning it into the correct object type, and storing it in the Object. (TODO: In the case where the object is of an unknown type, a runtime.Unknown object will be created and stored.) | 
**type** | **str** |  | 

## Example

```python
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_watch_event import IoK8sApimachineryPkgApisMetaV1WatchEvent

# TODO update the JSON string below
json = "{}"
# create an instance of IoK8sApimachineryPkgApisMetaV1WatchEvent from a JSON string
io_k8s_apimachinery_pkg_apis_meta_v1_watch_event_instance = IoK8sApimachineryPkgApisMetaV1WatchEvent.from_json(json)
# print the JSON string representation of the object
print IoK8sApimachineryPkgApisMetaV1WatchEvent.to_json()

# convert the object into a dict
io_k8s_apimachinery_pkg_apis_meta_v1_watch_event_dict = io_k8s_apimachinery_pkg_apis_meta_v1_watch_event_instance.to_dict()
# create an instance of IoK8sApimachineryPkgApisMetaV1WatchEvent from a dict
io_k8s_apimachinery_pkg_apis_meta_v1_watch_event_form_dict = io_k8s_apimachinery_pkg_apis_meta_v1_watch_event.from_dict(io_k8s_apimachinery_pkg_apis_meta_v1_watch_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


