# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.30.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_preference_match_expressions_inner import IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner

class TestIoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner(unittest.TestCase):
    """IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner:
        """Test IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner`
        """
        model = IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner()
        if include_optional:
            return IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner(
                key = '',
                operator = '',
                values = [
                    ''
                    ]
            )
        else:
            return IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner(
                key = '',
                operator = '',
        )
        """

    def testIoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner(self):
        """Test IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
