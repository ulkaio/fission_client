# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.30.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner import IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_required_during_scheduling_ignored_during_execution_inner import IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinity(BaseModel):
    """
    Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).
    """ # noqa: E501
    preferred_during_scheduling_ignored_during_execution: Optional[List[IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner]] = Field(default=None, description="The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding \"weight\" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.", alias="preferredDuringSchedulingIgnoredDuringExecution")
    required_during_scheduling_ignored_during_execution: Optional[List[IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionInner]] = Field(default=None, description="If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.", alias="requiredDuringSchedulingIgnoredDuringExecution")
    __properties: ClassVar[List[str]] = ["preferredDuringSchedulingIgnoredDuringExecution", "requiredDuringSchedulingIgnoredDuringExecution"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in preferred_during_scheduling_ignored_during_execution (list)
        _items = []
        if self.preferred_during_scheduling_ignored_during_execution:
            for _item in self.preferred_during_scheduling_ignored_during_execution:
                if _item:
                    _items.append(_item.to_dict())
            _dict['preferredDuringSchedulingIgnoredDuringExecution'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in required_during_scheduling_ignored_during_execution (list)
        _items = []
        if self.required_during_scheduling_ignored_during_execution:
            for _item in self.required_during_scheduling_ignored_during_execution:
                if _item:
                    _items.append(_item.to_dict())
            _dict['requiredDuringSchedulingIgnoredDuringExecution'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "preferredDuringSchedulingIgnoredDuringExecution": [IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner.from_dict(_item) for _item in obj.get("preferredDuringSchedulingIgnoredDuringExecution")] if obj.get("preferredDuringSchedulingIgnoredDuringExecution") is not None else None,
            "requiredDuringSchedulingIgnoredDuringExecution": [IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionInner.from_dict(_item) for _item in obj.get("requiredDuringSchedulingIgnoredDuringExecution")] if obj.get("requiredDuringSchedulingIgnoredDuringExecution") is not None else None
        })
        return _obj


