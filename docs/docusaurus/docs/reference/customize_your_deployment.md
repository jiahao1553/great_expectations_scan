---
title: Customize your deployment
---
Customizing your deployment by upgrading specific components of your deployment is a straight forward task. Data Contexts make this modular, so that you can add or swap out one component at a time. Most of these changes are quick, incremental steps—so you can upgrade from a basic demo deployment to a full production deployment at your own pace and be confident that your Data Context will continue to work at every step along the way.

This reference guide is designed to present you with clear options for upgrading your deployment. For specific implementation steps, please check out the linked How-to guides.

## Components

Here’s an overview of the components of a typical Great Expectations deployment:

* Great Expectations configs and metadata
  * [Options for storing Great Expectations configuration](#options-for-storing-great-expectations-configuration)
  * [Options for storing Expectations](#options-for-storing-expectations)
  * [Options for storing Validation Results](#options-for-storing-validation-results)
  * [Options for customizing generated notebooks](#options-for-customizing-generated-notebooks)

* Integrations to related systems
  * [Connecting to Data](#connecting-to-data)
  * [Options for hosting Data Docs](#options-for-hosting-data-docs)
  * [Additional Checkpoints and Actions](#additional-checkpoints-and-actions)
  * [How to update Data Docs as a Validation Action](../guides/validation/validation_actions/how_to_update_data_docs_as_a_validation_action.md)

## Options for storing Great Expectations configuration
The simplest way to manage your Great Expectations configuration is usually by committing great_expectations/great_expectations.yml to Git. However, it’s not usually a good idea to commit credentials to source control. In some situations, you might need to deploy without access to source control (or maybe even a file system).

Here’s how to handle each of those cases:

* [Configure credentials](../guides/setup/configuring_data_contexts/how_to_configure_credentials.md)
* [Instantiate an Ephemeral Data Context](/docs/guides/setup/configuring_data_contexts/instantiating_data_contexts/instantiate_data_context)

## Options for storing Expectations

Many teams find it convenient to store Expectations in Git. Essentially, this approach treats Expectations like test fixtures: they live adjacent to code and are stored within version control. Git acts as a collaboration tool and source of record.

Alternatively, you can treat Expectations like configs, and store them in a blob store. Finally, you can store them in a database. See [Configure Expectation Stores](../guides/setup/configuring_metadata_stores/configure_expectation_stores.md).

## Options for storing Validation Results

By default, Validation Results are stored locally, in an uncommitted directory. This is great for individual work, but not good for collaboration. The most common pattern is to use a cloud-based blob store such as S3, GCS, or Azure blob store. You can also store Validation Results in a database. See [Configure Validation Result Stores](../guides/setup/configuring_metadata_stores/configure_result_stores.md).


## Reference Architectures

* [How to instantiate a Data Context on an EMR Spark cluster](../deployment_patterns/how_to_instantiate_a_data_context_on_an_emr_spark_cluster.md)
* [How to use Great Expectations in Databricks](../tutorials/getting_started/how_to_use_great_expectations_in_databricks.md)

## Connecting to Data

Great Expectations allows you to connect to data in a wide variety of sources, and the list is constantly getting longer. If you have an idea for a source not listed here, please speak up in the public discussion forum.

* [How to connect to a Athena database](/docs/0.15.50/guides/connecting_to_your_data/database/athena)
* [How to connect to a BigQuery database](/docs/0.15.50/guides/connecting_to_your_data/database/bigquery)
* [How to connect to a MSSQL database](/docs/0.15.50/guides/connecting_to_your_data/database/mssql)
* [How to connect to a MySQL database](/docs/0.15.50/guides/connecting_to_your_data/database/mysql)
* [How to connect to a Postgres database](/docs/0.15.50/guides/connecting_to_your_data/database/postgres)
* [How to connect to a Redshift database](/docs/0.15.50/guides/connecting_to_your_data/database/redshift)
* [How to connect to a Snowflake database](/docs/0.15.50/guides/connecting_to_your_data/database/snowflake)
* [How to connect to a SQLite database](/docs/0.15.50/guides/connecting_to_your_data/database/sqlite)
* [How to connect to data on a filesystem using Spark](/docs/0.15.50/guides/connecting_to_your_data/filesystem/spark)
* [How to connect to data on S3 using Spark](/docs/0.15.50/guides/connecting_to_your_data/cloud/s3/spark)
* [How to connect to data on GCS using Spark](/docs/0.15.50/guides/connecting_to_your_data/cloud/gcs/spark)

## Options for hosting Data Docs

By default, Data Docs are stored locally, in an uncommitted directory. This is great for individual work, but not good for collaboration. A better solution is to deploy to a cloud-based blob store (S3, GCS, or Azure Blob Storage), configured to share a static website. See [Host and share Data Docs](../guides/setup/configuring_data_docs/host_and_share_data_docs.md).


## Additional Checkpoints and Actions

Most teams will want to configure various Checkpoints and Validation Actions as part of their deployment. There are two primary patterns for deploying Checkpoints. Sometimes Checkpoints are executed during data processing (e.g. as a task within Airflow). From this vantage point, they can control program flow. Sometimes Checkpoints are executed against materialized data. Great Expectations supports both patterns. There are also some rare instances where you may want to validate data without using a Checkpoint.

* [How to trigger Slack notifications as a Validation Action](../guides/validation/validation_actions/how_to_trigger_slack_notifications_as_a_validation_action.md)
* [How to trigger Opsgenie notifications as a Validation Action](../guides/validation/validation_actions/how_to_trigger_opsgenie_notifications_as_a_validation_action.md)
* [How to trigger Email as a Validation Action](../guides/validation/validation_actions/how_to_trigger_email_as_a_validation_action.md)
* [How to deploy a scheduled Checkpoint with cron](../guides/validation/advanced/how_to_deploy_a_scheduled_checkpoint_with_cron.md)
* [How to get Data Docs URLs for custom Validation Actions](../guides/validation/advanced/how_to_get_data_docs_urls_for_custom_validation_actions.md)
* [How to pass an in-memory DataFrame to a Checkpoint](../guides/validation/checkpoints/how_to_pass_an_in_memory_dataframe_to_a_checkpoint.md)
* [How to run a Checkpoint in Airflow](../deployment_patterns/how_to_use_great_expectations_with_airflow.md)

## Not interested in managing your own configuration or infrastructure?
Learn more about Great Expectations Cloud — our fully managed SaaS offering. Sign up for [our weekly cloud workshop](https://greatexpectations.io/cloud)! You’ll get to see our newest features and apply for our private Alpha program!
