module.exports = {
  docs: [
    'intro',
    {
      type: 'category',
      label: 'GX Cloud',
      link: { type: 'doc', id: 'cloud/gx_cloud_lp' },
      items: [
        {
          type: 'category',
          label: 'About GX Cloud',
          link: { type: 'doc', id: 'cloud/about_gx' },
          items: [
            {
              type: 'link',
              label: 'GX Cloud architecture',
              href: '/docs/cloud/about_gx#gx-cloud-architecture',
            },
            {
              type: 'link',
              label: 'GX Cloud deployment patterns',
              href: '/docs/cloud/about_gx#gx-cloud-deployment-patterns',
            },
            {
              type: 'link',
              label: 'Workflow optimization',
              href: '/docs/cloud/about_gx#workflow-optimization',
            },
            {
              type: 'link',
              label: 'GX Cloud workflow',
              href: '/docs/cloud/about_gx#gx-cloud-workflow',
            },
            {
              type: 'link',
              label: 'Roles and responsibilities',
              href: '/docs/cloud/about_gx#roles-and-responsibilities',
            },
            {
              type: 'link',
              label: 'Supported browsers',
              href: '/docs/cloud/about_gx#supported-browsers',
            },
            {
              type: 'link',
              label: 'Get support',
              href: '/docs/cloud/about_gx#get-support',
            },
          ]
        },
        {
          type: 'category',
          label: 'Set up GX Cloud',
          link: { type: 'doc', id: 'cloud/set_up_gx_cloud' },
          items: [
            {
              type: 'link',
              label: 'Request a GX Cloud Beta account',
              href: '/docs/cloud/set_up_gx_cloud#request-a-gx-cloud-beta-account',
            },
            {
              type: 'link',
              label: 'Prepare your environment',
              href: '/docs/cloud/set_up_gx_cloud#prepare-your-environment',
            },
            {
              type: 'link',
              label: 'Get your user access token and organization ID',
              href: '/docs/cloud/set_up_gx_cloud#get-your-user-access-token-and-organization-id',
            },
            {
              type: 'link',
              label: 'Set the environment variables and start the GX Cloud agent',
              href: '/docs/cloud/set_up_gx_cloud#set-the-environment-variables-and-start-the-gx-cloud-agent',
            },
          ]
        },
        {
          type: 'category',
          label: 'Quickstarts',
          link: { type: 'doc', id: 'cloud/quickstarts/quickstart_lp' },
          items: [
            'cloud/quickstarts/snowflake_quickstart',
            'cloud/quickstarts/airflow_quickstart',
          ]
        },
        {
          type: 'category',
          label: 'Manage Data Assets',
          link: { type: 'doc', id: 'cloud/data_assets/manage_data_assets' },
          items: [
            {
              type: 'link',
              label: 'Create a Data Asset',
              href: '/docs/cloud/data_assets/manage_data_assets#create-a-data-asset',
            },
            {
              type: 'link',
              label: 'View Data Asset metrics',
              href: '/docs/cloud/data_assets/manage_data_assets#view-data-asset-metrics',
            },
            {
              type: 'link',
              label: 'Add a Data Asset to an Existing Data Source',
              href: '/docs/cloud/data_assets/manage_data_assets#add-a-data-asset-to-an-existing-data-source',
            },
            {
              type: 'link',
              label: 'Edit a Data Asset',
              href: '/docs/cloud/data_assets/manage_data_assets#edit-a-data-asset',
            },
            {
              type: 'link',
              label: 'Delete a Data Asset',
              href: '/docs/cloud/data_assets/manage_data_assets#delete-a-data-asset',
            },
          ]
        },
        {
          type: 'category',
          label: 'Manage Expectations',
          link: { type: 'doc', id: 'cloud/expectations/manage_expectations' },
          items: [
            {
              type: 'link',
              label: 'Add an Expectation',
              href: '/docs/cloud/expectations/manage_expectations#create-an-expectation',
            },
            {
              type: 'link',
              label: 'Edit an Expectation',
              href: '/docs/cloud/expectations/manage_expectations#edit-an-expectation',
            },
            {
              type: 'link',
              label: 'Delete an Expectation',
              href: '/docs/cloud/expectations/manage_expectations#delete-an-expectation',
            },
          ]
        },
        {
          type: 'category',
          label: 'Manage Expectation Suites',
          link: { type: 'doc', id: 'cloud/expectation_suites/manage_expectation_suites' },
          items: [
            {
              type: 'link',
              label: 'Automatically create an Expectation Suite that tests for missing data',
              href: '/docs/cloud/expectation_suites/manage_expectation_suites#automatically-create-an-expectation-suite-that-tests-for-missing-data',
            },
            {
              type: 'link',
              label: 'Create an empty Expectation Suite ',
              href: '/docs/cloud/expectation_suites/manage_expectation_suites#manually-create-an-empty-expectation-suite',
            },
            {
              type: 'link',
              label: 'Delete an Expectation Suite',
              href: '/docs/cloud/expectation_suites/manage_expectation_suites#delete-an-expectation-suite',
            },
          ]
        },
        {
          type: 'category',
          label: 'Manage Validations',
          link: { type: 'doc', id: 'cloud/validations/manage_validations' },
          items: [
            {
              type: 'link',
              label: 'Run a Validation',
              href: '/docs/cloud/validations/manage_validations#run-a-validation',
            },
            {
              type: 'link',
              label: 'View Validation run history',
              href: '/docs/cloud/validations/manage_validations#view-validation-run-history',
            },
          ]
        },
        {
          type: 'category',
          label: 'Manage Checkpoints',
          link: { type: 'doc', id: 'cloud/checkpoints/manage_checkpoints' },
          items: [
            {
              type: 'link',
              label: 'Add a Checkpoint',
              href: '/docs/cloud/checkpoints/manage_checkpoints#add-a-checkpoint',
            },
            {
              type: 'link',
              label: 'Run a Checkpoint',
              href: '/docs/cloud/checkpoints/manage_checkpoints#run-a-checkpoint',
            },
            {
              type: 'link',
              label: 'Edit a Checkpoint configuration',
              href: '/docs/cloud/checkpoints/manage_checkpoints#edit-a-checkpoint-configuration',
            },
            {
              type: 'link',
              label: 'Delete a Checkpoint',
              href: '/docs/cloud/checkpoints/manage_checkpoints#delete-a-checkpoint',
            },
          ]
        },
        {
          type: 'category',
          label: 'Manage users and access tokens',
          link: { type: 'doc', id: 'cloud/users/manage_users' },
          items: [
            {
              type: 'link',
              label: 'Invite a user',
              href: '/docs/cloud/users/manage_users#invite-a-user',
            },
            {
              type: 'link',
              label: 'Edit a user role',
              href: '/docs/cloud/users/manage_users#edit-a-user-role',
            },
            {
              type: 'link',
              label: 'Delete a user',
              href: '/docs/cloud/users/manage_users#delete-a-user',
            },
            {
              type: 'link',
              label: 'Create a user access token',
              href: '/docs/cloud/users/manage_users#create-a-user-access-token',
            },
            {
              type: 'link',
              label: 'Create an organization access token',
              href: '/docs/cloud/users/manage_users#create-an-organization-access-token',
            },
            {
              type: 'link',
              label: 'Delete a user or organization access token',
              href: '/docs/cloud/users/manage_users#delete-a-user-or-organization-access-token',
            },
          ]
        },
      ]
    },
    {
      type: 'category',
      label: 'Get started with GX',
      link: { type: 'doc', id: 'guides/setup/get_started_lp' },
      items: [
        'tutorials/quickstart/quickstart',
        {
          type: 'doc', id: 'conceptual_guides/gx_overview', label: 'GX Overview'
        },
        'tutorials/getting_started/how_to_use_great_expectations_in_databricks',
        'tutorials/getting_started/how_to_use_great_expectations_with_sql',
      ]
    },
    {
      type: 'category',
      label: 'Configure your GX environment',
      link: { type: 'doc', id: 'guides/setup/setup_overview_lp' },
      items: [
        'guides/setup/setup_overview',
        'guides/setup/installation/install_gx',
        {
          type: 'category',
          label: 'Configure Data Contexts',
          link: { type: 'doc', id: 'guides/setup/configure_data_contexts_lp' },
          items: [
            'guides/setup/configuring_data_contexts/instantiating_data_contexts/instantiate_data_context',
            'guides/setup/configuring_data_contexts/how_to_convert_an_ephemeral_data_context_to_a_filesystem_data_context',
            'guides/setup/configuring_data_contexts/how_to_configure_credentials',
          ]
        },
        'guides/setup/configuring_metadata_stores/configure_expectation_stores',
        'guides/setup/configuring_metadata_stores/configure_result_stores',
        'guides/setup/configuring_metadata_stores/how_to_configure_a_metricsstore',
        'guides/setup/configuring_data_docs/host_and_share_data_docs',
      ]
    },
    {
      type: 'category',
      label: 'Connect to a Data Source',
      link: { type: 'doc', id: 'guides/connecting_to_your_data/connect_to_data_lp' },
      items: [
        'guides/connecting_to_your_data/fluent/filesystem/connect_filesystem_source_data',
        'guides/connecting_to_your_data/fluent/in_memory/connect_in_memory_data',
        'guides/connecting_to_your_data/fluent/database/connect_sql_source_data',
        {
          type: 'category',
          label: 'Manage Data Assets',
          link: { type: 'doc', id: 'guides/connecting_to_your_data/manage_data_assets_lp' },
          items: [
            'guides/connecting_to_your_data/fluent/batch_requests/how_to_request_data_from_a_data_asset',
            'guides/connecting_to_your_data/fluent/data_assets/how_to_organize_batches_in_a_file_based_data_asset',
            'guides/connecting_to_your_data/fluent/database/sql_data_assets',
          ]
        },
      ]
    },
    {
      type: 'category',
      label: 'Create Expectations',
      link: { type: 'doc', id: 'guides/expectations/expectations_lp' },
      items: [
        'guides/expectations/create_expectations_overview',
        {
          type: 'category',
          label: 'Manage Expectations and Expectation Suites',
          link: { type: 'doc', id: 'guides/expectations/create_manage_expectations_lp' },
          items: [
            'guides/expectations/how_to_create_and_edit_expectations_based_on_domain_knowledge_without_inspecting_data_directly',
            'guides/expectations/how_to_create_and_edit_expectations_with_instant_feedback_from_a_sample_batch_of_data',
            'guides/expectations/how_to_edit_an_existing_expectationsuite',
            'guides/expectations/how_to_use_auto_initializing_expectations',
            'guides/expectations/advanced/how_to_create_expectations_that_span_multiple_batches_using_evaluation_parameters',
            'guides/expectations/advanced/how_to_dynamically_load_evaluation_parameters_from_a_database',
            'guides/expectations/advanced/identify_failed_rows_expectations',
          ]
        },
        {
          type: 'category',
          label: 'Data Assistants',
          link: { type: 'doc', id: 'guides/expectations/data_assistants_lp' },
          items: [
            'guides/expectations/data_assistants/how_to_create_an_expectation_suite_with_the_onboarding_data_assistant',
            'guides/expectations/advanced/how_to_compare_two_tables_with_the_onboarding_data_assistant',
            'guides/expectations/data_assistants/how_to_create_an_expectation_suite_with_the_missingness_data_assistant',
            
          ]
        },
        {
          type: 'category',
          label: 'Create Custom Expectations',
          link: { type: 'doc', id: 'guides/expectations/custom_expectations_lp' },
          items: [
            'guides/expectations/creating_custom_expectations/how_to_create_custom_column_aggregate_expectations',
            'guides/expectations/creating_custom_expectations/how_to_create_custom_column_map_expectations',
            'guides/expectations/creating_custom_expectations/how_to_create_custom_batch_expectations',
            'guides/expectations/creating_custom_expectations/how_to_create_custom_column_pair_map_expectations',
            'guides/expectations/creating_custom_expectations/how_to_create_custom_multicolumn_map_expectations',
            'guides/expectations/creating_custom_expectations/how_to_create_custom_regex_based_column_map_expectations',
            'guides/expectations/creating_custom_expectations/how_to_create_custom_set_based_column_map_expectations',
            'guides/expectations/creating_custom_expectations/how_to_create_custom_query_expectations',
            'guides/expectations/creating_custom_expectations/how_to_create_custom_parameterized_expectations',
            'guides/expectations/creating_custom_expectations/how_to_add_support_for_the_auto_initializing_framework_to_a_custom_expectation',
          ]
        },
        {
          type: 'category',
          label: 'Add Features to Custom Expectations',
          link: { type: 'doc', id: 'guides/expectations/add_features_custom_expectations_lp' },
          items: [
            'guides/expectations/advanced/how_to_add_comments_to_expectations_and_display_them_in_data_docs',
            'guides/expectations/features_custom_expectations/how_to_add_example_cases_for_an_expectation',
            'guides/expectations/features_custom_expectations/how_to_add_input_validation_for_an_expectation',
            'guides/expectations/features_custom_expectations/how_to_add_spark_support_for_an_expectation',
            'guides/expectations/features_custom_expectations/how_to_add_sqlalchemy_support_for_an_expectation',
            'guides/expectations/creating_custom_expectations/add_custom_parameters',
          ]
        },
        'guides/expectations/creating_custom_expectations/how_to_use_custom_expectations',
      ]
    },
    {
      type: 'category',
      label: 'Validate Data',
      link: { type: 'doc', id: 'guides/validation/validate_data_lp' },
      items: [
        'guides/validation/validate_data_overview',
        {
          type: 'category',
          label: 'Manage Checkpoints',
          link: { type: 'doc', id: 'guides/validation/checkpoints/checkpoint_lp' },
          items: [
            'guides/validation/checkpoints/how_to_create_a_new_checkpoint',
            'guides/validation/checkpoints/how_to_add_validations_data_or_suites_to_a_checkpoint',
            'guides/validation/checkpoints/how_to_validate_multiple_batches_within_single_checkpoint',
            'guides/validation/checkpoints/how_to_pass_an_in_memory_dataframe_to_a_checkpoint',
            'guides/validation/advanced/how_to_deploy_a_scheduled_checkpoint_with_cron',
          ]
        },
        {
          type: 'category',
          label: 'Configure Actions',
          link: { type: 'doc', id: 'guides/validation/validation_actions/actions_lp' },
          items: [
            'guides/validation/validation_actions/how_to_trigger_email_as_a_validation_action',
            'guides/validation/validation_actions/how_to_collect_openlineage_metadata_using_a_validation_action',
            'guides/validation/validation_actions/how_to_trigger_opsgenie_notifications_as_a_validation_action',
            'guides/validation/validation_actions/how_to_trigger_slack_notifications_as_a_validation_action',
            'guides/validation/validation_actions/how_to_update_data_docs_as_a_validation_action',
            'guides/validation/advanced/how_to_get_data_docs_urls_for_custom_validation_actions',
          ]
        },
        'guides/validation/limit_validation_results',
      ]
    },
    {
      type: 'category',
      label: 'Integrations',
      link: {
        type: 'generated-index',
        title: 'Integrations',
        description: 'Integrate Great Expectations (GX) with commonly used data engineering tools.',
      },
      items: [
        {
          type: 'category',
          label: 'Amazon Web Services (AWS)',
          link: {
            type: 'doc',
            id: 'deployment_patterns/aws_lp',
          },
          items: [
            'deployment_patterns/how_to_use_great_expectations_in_aws_glue',
            'deployment_patterns/how_to_instantiate_a_data_context_on_an_emr_spark_cluster',
            'deployment_patterns/how_to_use_great_expectations_in_emr_serverless',
            'deployment_patterns/how_to_use_gx_with_aws/how_to_use_gx_with_aws_using_cloud_storage_and_pandas',
            'deployment_patterns/how_to_use_gx_with_aws/how_to_use_gx_with_aws_using_s3_and_spark',
            'deployment_patterns/how_to_use_gx_with_aws/how_to_use_gx_with_aws_using_athena',
            'deployment_patterns/how_to_use_gx_with_aws/how_to_use_gx_with_aws_using_redshift',
          ],
        },
        'deployment_patterns/how_to_instantiate_a_data_context_hosted_environments',
        'deployment_patterns/how_to_use_great_expectations_with_airflow',
        'integrations/integration_datahub',
        'deployment_patterns/how_to_use_great_expectations_in_deepnote',
        'deployment_patterns/how_to_use_great_expectations_in_flyte',
        'deployment_patterns/how_to_use_great_expectations_with_meltano',
        'deployment_patterns/how_to_use_great_expectations_with_prefect',
        'deployment_patterns/how_to_use_great_expectations_with_ydata_synthetic',
        'integrations/integration_zenml',
      ]
    },
    {
      type: 'category',
      label: 'Concepts',
      link: { 
        type: 'doc', 
        id: 'conceptual_guides/learn_lp' 
      },
      items: [
        'conceptual_guides/expectation_classes',
        'conceptual_guides/metricproviders',
      ]
    },
    {
      type: 'category',
      label: 'Reference',
      link: { type: 'doc', id: 'reference/reference_overview' },
      items: [
        'contributing/contributing_maturity',
        'reference/customize_your_deployment',
        'reference/usage_statistics',
        {
          type: 'category',
          label: 'API documentation',
          link: { type: 'doc', id: 'reference/api_reference' },
          items: [
            {
              type: 'autogenerated',
              dirName: 'reference/api'
            }
          ]
        },
        {
          type: 'category',
          label: 'Glossary',
          link: { type: 'doc', id: 'glossary' },
          items: [
            'terms/action',
            'terms/batch',
            'terms/batch_request',
            'terms/custom_expectation',
            'terms/checkpoint',
            'terms/cli',
            'terms/datasource',
            'terms/data_context',
            'terms/data_asset',
            'terms/data_assistant',
            'terms/data_docs',
            'terms/evaluation_parameter',
            'terms/execution_engine',
            {
              type: 'category',
              label: 'Expectations',
              link: { type: 'doc', id: 'terms/expectation' },
              collapsed: true,
              items: [
                { type: 'doc', id: 'reference/expectations/conditional_expectations' },
                { type: 'doc', id: 'reference/expectations/distributional_expectations' },
                { type: 'doc', id: 'reference/expectation_suite_operations' },
                { type: 'doc', id: 'reference/expectations/result_format' },
                { type: 'doc', id: 'reference/expectations/standard_arguments' }
              ]
            },
            'terms/expectation_suite',
            'terms/metric',
            {
              type: 'category',
              label: 'Stores',
              link: { type: 'doc', id: 'terms/store' },
              items: [
                'terms/checkpoint_store',
                'terms/data_docs_store',
                'terms/evaluation_parameter_store',
                'terms/expectation_store',
                'terms/metric_store',
                'terms/validation_result_store'
              ]
            },
            'terms/renderer',
            'terms/supporting_resource',
            'terms/validator',
            'terms/validation_result'
          ]
        }
      ]
    },
    { type: 'doc', id: 'changelog' },
    { type: 'doc', id: 'troubleshooting' },
    { type: 'doc', id: 'guides/miscellaneous/migration_guide' },
    'get_support',
    'contributing/contributing',
  ]
}
