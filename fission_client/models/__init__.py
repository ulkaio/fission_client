# coding: utf-8

# flake8: noqa
"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.30.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from fission_client.models.io_fission_v1_canary_config import IoFissionV1CanaryConfig
from fission_client.models.io_fission_v1_canary_config_list import IoFissionV1CanaryConfigList
from fission_client.models.io_fission_v1_canary_config_spec import IoFissionV1CanaryConfigSpec
from fission_client.models.io_fission_v1_canary_config_status import IoFissionV1CanaryConfigStatus
from fission_client.models.io_fission_v1_environment import IoFissionV1Environment
from fission_client.models.io_fission_v1_environment_list import IoFissionV1EnvironmentList
from fission_client.models.io_fission_v1_environment_spec import IoFissionV1EnvironmentSpec
from fission_client.models.io_fission_v1_environment_spec_builder import IoFissionV1EnvironmentSpecBuilder
from fission_client.models.io_fission_v1_environment_spec_builder_container import IoFissionV1EnvironmentSpecBuilderContainer
from fission_client.models.io_fission_v1_environment_spec_builder_container_env_from_inner import IoFissionV1EnvironmentSpecBuilderContainerEnvFromInner
from fission_client.models.io_fission_v1_environment_spec_builder_container_env_from_inner_config_map_ref import IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerConfigMapRef
from fission_client.models.io_fission_v1_environment_spec_builder_container_env_from_inner_secret_ref import IoFissionV1EnvironmentSpecBuilderContainerEnvFromInnerSecretRef
from fission_client.models.io_fission_v1_environment_spec_builder_container_env_inner import IoFissionV1EnvironmentSpecBuilderContainerEnvInner
from fission_client.models.io_fission_v1_environment_spec_builder_container_env_inner_value_from import IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFrom
from fission_client.models.io_fission_v1_environment_spec_builder_container_env_inner_value_from_config_map_key_ref import IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromConfigMapKeyRef
from fission_client.models.io_fission_v1_environment_spec_builder_container_env_inner_value_from_field_ref import IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromFieldRef
from fission_client.models.io_fission_v1_environment_spec_builder_container_env_inner_value_from_resource_field_ref import IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromResourceFieldRef
from fission_client.models.io_fission_v1_environment_spec_builder_container_env_inner_value_from_secret_key_ref import IoFissionV1EnvironmentSpecBuilderContainerEnvInnerValueFromSecretKeyRef
from fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle import IoFissionV1EnvironmentSpecBuilderContainerLifecycle
from fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle_post_start import IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStart
from fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle_post_start_exec import IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartExec
from fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle_post_start_http_get import IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGet
from fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle_post_start_http_get_http_headers_inner import IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartHttpGetHttpHeadersInner
from fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle_post_start_sleep import IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartSleep
from fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle_post_start_tcp_socket import IoFissionV1EnvironmentSpecBuilderContainerLifecyclePostStartTcpSocket
from fission_client.models.io_fission_v1_environment_spec_builder_container_lifecycle_pre_stop import IoFissionV1EnvironmentSpecBuilderContainerLifecyclePreStop
from fission_client.models.io_fission_v1_environment_spec_builder_container_liveness_probe import IoFissionV1EnvironmentSpecBuilderContainerLivenessProbe
from fission_client.models.io_fission_v1_environment_spec_builder_container_liveness_probe_grpc import IoFissionV1EnvironmentSpecBuilderContainerLivenessProbeGrpc
from fission_client.models.io_fission_v1_environment_spec_builder_container_liveness_probe_tcp_socket import IoFissionV1EnvironmentSpecBuilderContainerLivenessProbeTcpSocket
from fission_client.models.io_fission_v1_environment_spec_builder_container_ports_inner import IoFissionV1EnvironmentSpecBuilderContainerPortsInner
from fission_client.models.io_fission_v1_environment_spec_builder_container_readiness_probe import IoFissionV1EnvironmentSpecBuilderContainerReadinessProbe
from fission_client.models.io_fission_v1_environment_spec_builder_container_resize_policy_inner import IoFissionV1EnvironmentSpecBuilderContainerResizePolicyInner
from fission_client.models.io_fission_v1_environment_spec_builder_container_resources import IoFissionV1EnvironmentSpecBuilderContainerResources
from fission_client.models.io_fission_v1_environment_spec_builder_container_resources_claims_inner import IoFissionV1EnvironmentSpecBuilderContainerResourcesClaimsInner
from fission_client.models.io_fission_v1_environment_spec_builder_container_security_context import IoFissionV1EnvironmentSpecBuilderContainerSecurityContext
from fission_client.models.io_fission_v1_environment_spec_builder_container_security_context_app_armor_profile import IoFissionV1EnvironmentSpecBuilderContainerSecurityContextAppArmorProfile
from fission_client.models.io_fission_v1_environment_spec_builder_container_security_context_capabilities import IoFissionV1EnvironmentSpecBuilderContainerSecurityContextCapabilities
from fission_client.models.io_fission_v1_environment_spec_builder_container_security_context_se_linux_options import IoFissionV1EnvironmentSpecBuilderContainerSecurityContextSeLinuxOptions
from fission_client.models.io_fission_v1_environment_spec_builder_container_security_context_seccomp_profile import IoFissionV1EnvironmentSpecBuilderContainerSecurityContextSeccompProfile
from fission_client.models.io_fission_v1_environment_spec_builder_container_security_context_windows_options import IoFissionV1EnvironmentSpecBuilderContainerSecurityContextWindowsOptions
from fission_client.models.io_fission_v1_environment_spec_builder_container_startup_probe import IoFissionV1EnvironmentSpecBuilderContainerStartupProbe
from fission_client.models.io_fission_v1_environment_spec_builder_container_volume_devices_inner import IoFissionV1EnvironmentSpecBuilderContainerVolumeDevicesInner
from fission_client.models.io_fission_v1_environment_spec_builder_container_volume_mounts_inner import IoFissionV1EnvironmentSpecBuilderContainerVolumeMountsInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec import IoFissionV1EnvironmentSpecBuilderPodspec
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity import IoFissionV1EnvironmentSpecBuilderPodspecAffinity
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity import IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinity
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner import IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_preference import IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreference
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_preferred_during_scheduling_ignored_during_execution_inner_preference_match_expressions_inner import IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPreferenceMatchExpressionsInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_required_during_scheduling_ignored_during_execution import IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_node_affinity_required_during_scheduling_ignored_during_execution_node_selector_terms_inner import IoFissionV1EnvironmentSpecBuilderPodspecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTermsInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity import IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinity
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner import IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term import IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTerm
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_label_selector import IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelector
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_label_selector_match_expressions_inner import IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermLabelSelectorMatchExpressionsInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_preferred_during_scheduling_ignored_during_execution_inner_pod_affinity_term_namespace_selector import IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityPreferredDuringSchedulingIgnoredDuringExecutionInnerPodAffinityTermNamespaceSelector
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_affinity_required_during_scheduling_ignored_during_execution_inner import IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAffinityRequiredDuringSchedulingIgnoredDuringExecutionInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_affinity_pod_anti_affinity import IoFissionV1EnvironmentSpecBuilderPodspecAffinityPodAntiAffinity
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_containers_inner import IoFissionV1EnvironmentSpecBuilderPodspecContainersInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_dns_config import IoFissionV1EnvironmentSpecBuilderPodspecDnsConfig
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_dns_config_options_inner import IoFissionV1EnvironmentSpecBuilderPodspecDnsConfigOptionsInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_ephemeral_containers_inner import IoFissionV1EnvironmentSpecBuilderPodspecEphemeralContainersInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_ephemeral_containers_inner_lifecycle import IoFissionV1EnvironmentSpecBuilderPodspecEphemeralContainersInnerLifecycle
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_ephemeral_containers_inner_liveness_probe import IoFissionV1EnvironmentSpecBuilderPodspecEphemeralContainersInnerLivenessProbe
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_ephemeral_containers_inner_resources import IoFissionV1EnvironmentSpecBuilderPodspecEphemeralContainersInnerResources
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_ephemeral_containers_inner_security_context import IoFissionV1EnvironmentSpecBuilderPodspecEphemeralContainersInnerSecurityContext
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_host_aliases_inner import IoFissionV1EnvironmentSpecBuilderPodspecHostAliasesInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_image_pull_secrets_inner import IoFissionV1EnvironmentSpecBuilderPodspecImagePullSecretsInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_os import IoFissionV1EnvironmentSpecBuilderPodspecOs
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_readiness_gates_inner import IoFissionV1EnvironmentSpecBuilderPodspecReadinessGatesInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_resource_claims_inner import IoFissionV1EnvironmentSpecBuilderPodspecResourceClaimsInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_scheduling_gates_inner import IoFissionV1EnvironmentSpecBuilderPodspecSchedulingGatesInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_security_context import IoFissionV1EnvironmentSpecBuilderPodspecSecurityContext
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_security_context_app_armor_profile import IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextAppArmorProfile
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_security_context_se_linux_options import IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextSeLinuxOptions
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_security_context_seccomp_profile import IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextSeccompProfile
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_security_context_sysctls_inner import IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextSysctlsInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_security_context_windows_options import IoFissionV1EnvironmentSpecBuilderPodspecSecurityContextWindowsOptions
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_tolerations_inner import IoFissionV1EnvironmentSpecBuilderPodspecTolerationsInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_topology_spread_constraints_inner import IoFissionV1EnvironmentSpecBuilderPodspecTopologySpreadConstraintsInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_topology_spread_constraints_inner_label_selector import IoFissionV1EnvironmentSpecBuilderPodspecTopologySpreadConstraintsInnerLabelSelector
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_aws_elastic_block_store import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerAwsElasticBlockStore
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_azure_disk import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerAzureDisk
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_azure_file import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerAzureFile
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_cephfs import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfs
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_cephfs_secret_ref import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCephfsSecretRef
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_cinder import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCinder
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_cinder_secret_ref import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCinderSecretRef
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_config_map import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerConfigMap
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_config_map_items_inner import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerConfigMapItemsInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_csi import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCsi
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_csi_node_publish_secret_ref import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerCsiNodePublishSecretRef
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPI
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_items_inner import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_items_inner_field_ref import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerFieldRef
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_downward_api_items_inner_resource_field_ref import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerDownwardAPIItemsInnerResourceFieldRef
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_empty_dir import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEmptyDir
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeral
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplate
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpec
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_data_source import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecDataSource
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_data_source_ref import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecDataSourceRef
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_resources import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecResources
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_ephemeral_volume_claim_template_spec_selector import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerEphemeralVolumeClaimTemplateSpecSelector
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_fc import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFc
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_flex_volume import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolume
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_flex_volume_secret_ref import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlexVolumeSecretRef
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_flocker import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerFlocker
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_gce_persistent_disk import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGcePersistentDisk
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_git_repo import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGitRepo
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_glusterfs import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerGlusterfs
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_host_path import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerHostPath
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_image import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerImage
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_iscsi import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerIscsi
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_iscsi_secret_ref import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerIscsiSecretRef
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_nfs import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerNfs
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_persistent_volume_claim import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPersistentVolumeClaim
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_photon_persistent_disk import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPhotonPersistentDisk
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_portworx_volume import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerPortworxVolume
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjected
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInner
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_cluster_trust_bundle import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerClusterTrustBundle
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_cluster_trust_bundle_label_selector import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerClusterTrustBundleLabelSelector
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_config_map import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerConfigMap
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_downward_api import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerDownwardAPI
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_secret import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerSecret
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_projected_sources_inner_service_account_token import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerProjectedSourcesInnerServiceAccountToken
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_quobyte import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerQuobyte
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_rbd import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerRbd
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_rbd_secret_ref import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerRbdSecretRef
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_scale_io import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerScaleIO
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_scale_io_secret_ref import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerScaleIOSecretRef
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_secret import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerSecret
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_storageos import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerStorageos
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_storageos_secret_ref import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerStorageosSecretRef
from fission_client.models.io_fission_v1_environment_spec_builder_podspec_volumes_inner_vsphere_volume import IoFissionV1EnvironmentSpecBuilderPodspecVolumesInnerVsphereVolume
from fission_client.models.io_fission_v1_environment_spec_resources import IoFissionV1EnvironmentSpecResources
from fission_client.models.io_fission_v1_environment_spec_runtime import IoFissionV1EnvironmentSpecRuntime
from fission_client.models.io_fission_v1_environment_spec_runtime_container import IoFissionV1EnvironmentSpecRuntimeContainer
from fission_client.models.io_fission_v1_environment_spec_runtime_podspec import IoFissionV1EnvironmentSpecRuntimePodspec
from fission_client.models.io_fission_v1_function import IoFissionV1Function
from fission_client.models.io_fission_v1_function_list import IoFissionV1FunctionList
from fission_client.models.io_fission_v1_function_spec import IoFissionV1FunctionSpec
from fission_client.models.io_fission_v1_function_spec_environment import IoFissionV1FunctionSpecEnvironment
from fission_client.models.io_fission_v1_function_spec_invoke_strategy import IoFissionV1FunctionSpecInvokeStrategy
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategy
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehavior
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_down import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleDown
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_down_policies_inner import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleDownPoliciesInner
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_behavior_scale_up import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaBehaviorScaleUp
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInner
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_container_resource import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerContainerResource
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_container_resource_target import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerContainerResourceTarget
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternal
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external_metric import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetric
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_external_metric_selector import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerExternalMetricSelector
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_object import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerObject
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_object_described_object import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerObjectDescribedObject
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_pods import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerPods
from fission_client.models.io_fission_v1_function_spec_invoke_strategy_execution_strategy_hpa_metrics_inner_resource import IoFissionV1FunctionSpecInvokeStrategyExecutionStrategyHpaMetricsInnerResource
from fission_client.models.io_fission_v1_function_spec_package import IoFissionV1FunctionSpecPackage
from fission_client.models.io_fission_v1_function_spec_package_packageref import IoFissionV1FunctionSpecPackagePackageref
from fission_client.models.io_fission_v1_function_spec_podspec import IoFissionV1FunctionSpecPodspec
from fission_client.models.io_fission_v1_function_spec_resources import IoFissionV1FunctionSpecResources
from fission_client.models.io_fission_v1_http_trigger import IoFissionV1HTTPTrigger
from fission_client.models.io_fission_v1_http_trigger_list import IoFissionV1HTTPTriggerList
from fission_client.models.io_fission_v1_http_trigger_spec import IoFissionV1HTTPTriggerSpec
from fission_client.models.io_fission_v1_http_trigger_spec_functionref import IoFissionV1HTTPTriggerSpecFunctionref
from fission_client.models.io_fission_v1_http_trigger_spec_ingressconfig import IoFissionV1HTTPTriggerSpecIngressconfig
from fission_client.models.io_fission_v1_kubernetes_watch_trigger import IoFissionV1KubernetesWatchTrigger
from fission_client.models.io_fission_v1_kubernetes_watch_trigger_list import IoFissionV1KubernetesWatchTriggerList
from fission_client.models.io_fission_v1_kubernetes_watch_trigger_spec import IoFissionV1KubernetesWatchTriggerSpec
from fission_client.models.io_fission_v1_kubernetes_watch_trigger_spec_functionref import IoFissionV1KubernetesWatchTriggerSpecFunctionref
from fission_client.models.io_fission_v1_message_queue_trigger import IoFissionV1MessageQueueTrigger
from fission_client.models.io_fission_v1_message_queue_trigger_list import IoFissionV1MessageQueueTriggerList
from fission_client.models.io_fission_v1_message_queue_trigger_spec import IoFissionV1MessageQueueTriggerSpec
from fission_client.models.io_fission_v1_message_queue_trigger_spec_functionref import IoFissionV1MessageQueueTriggerSpecFunctionref
from fission_client.models.io_fission_v1_message_queue_trigger_spec_podspec import IoFissionV1MessageQueueTriggerSpecPodspec
from fission_client.models.io_fission_v1_package import IoFissionV1Package
from fission_client.models.io_fission_v1_package_list import IoFissionV1PackageList
from fission_client.models.io_fission_v1_package_spec import IoFissionV1PackageSpec
from fission_client.models.io_fission_v1_package_spec_deployment import IoFissionV1PackageSpecDeployment
from fission_client.models.io_fission_v1_package_spec_deployment_checksum import IoFissionV1PackageSpecDeploymentChecksum
from fission_client.models.io_fission_v1_package_spec_environment import IoFissionV1PackageSpecEnvironment
from fission_client.models.io_fission_v1_package_spec_source import IoFissionV1PackageSpecSource
from fission_client.models.io_fission_v1_package_status import IoFissionV1PackageStatus
from fission_client.models.io_fission_v1_time_trigger import IoFissionV1TimeTrigger
from fission_client.models.io_fission_v1_time_trigger_list import IoFissionV1TimeTriggerList
from fission_client.models.io_fission_v1_time_trigger_spec import IoFissionV1TimeTriggerSpec
from fission_client.models.io_fission_v1_time_trigger_spec_functionref import IoFissionV1TimeTriggerSpecFunctionref
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_group import IoK8sApimachineryPkgApisMetaV1APIGroup
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_group_list import IoK8sApimachineryPkgApisMetaV1APIGroupList
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_resource import IoK8sApimachineryPkgApisMetaV1APIResource
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_resource_list import IoK8sApimachineryPkgApisMetaV1APIResourceList
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_api_versions import IoK8sApimachineryPkgApisMetaV1APIVersions
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_condition import IoK8sApimachineryPkgApisMetaV1Condition
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_delete_options import IoK8sApimachineryPkgApisMetaV1DeleteOptions
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_group_version_for_discovery import IoK8sApimachineryPkgApisMetaV1GroupVersionForDiscovery
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_label_selector import IoK8sApimachineryPkgApisMetaV1LabelSelector
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_label_selector_requirement import IoK8sApimachineryPkgApisMetaV1LabelSelectorRequirement
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_list_meta import IoK8sApimachineryPkgApisMetaV1ListMeta
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_managed_fields_entry import IoK8sApimachineryPkgApisMetaV1ManagedFieldsEntry
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_object_meta import IoK8sApimachineryPkgApisMetaV1ObjectMeta
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_owner_reference import IoK8sApimachineryPkgApisMetaV1OwnerReference
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_preconditions import IoK8sApimachineryPkgApisMetaV1Preconditions
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_server_address_by_client_cidr import IoK8sApimachineryPkgApisMetaV1ServerAddressByClientCIDR
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_status import IoK8sApimachineryPkgApisMetaV1Status
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_status_cause import IoK8sApimachineryPkgApisMetaV1StatusCause
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_status_details import IoK8sApimachineryPkgApisMetaV1StatusDetails
from fission_client.models.io_k8s_apimachinery_pkg_apis_meta_v1_watch_event import IoK8sApimachineryPkgApisMetaV1WatchEvent
from fission_client.models.io_k8s_apimachinery_pkg_version_info import IoK8sApimachineryPkgVersionInfo
