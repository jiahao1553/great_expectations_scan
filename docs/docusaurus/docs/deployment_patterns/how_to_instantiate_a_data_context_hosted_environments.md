---
title: "Deploy Great Expectations in hosted environments without a file system"
sidebar_label: "Hosted environments"
description: "Use Great Expectations in hosted environments"
id: how_to_instantiate_a_data_context_hosted_environments
sidebar_custom_props: { icon: 'img/integrations/hosted_icon.svg' }
---

The components in the ``great_expectations.yml`` file define the Validation Results Stores, Data Source connections, and Data Docs hosts for a Data Context. These components might be inaccessible in hosted environments, such as Databricks, Amazon EMR, and Google Cloud Composer. The information provided here is intended to help you use Great Expectations in hosted environments.

## Configure your Data Context
 
To use code to create a Data Context, see [Instantiate an Ephemeral Data Context](/docs/guides/setup/configuring_data_contexts/instantiating_data_contexts/instantiate_data_context).

To configure a Data Context for a specific environment, see one of the following resources:

- [How to instantiate a Data Context on an EMR Spark cluster](./how_to_instantiate_a_data_context_on_an_emr_spark_cluster.md)
- [How to use Great Expectations in Databricks](../tutorials/getting_started/how_to_use_great_expectations_in_databricks.md)

## Create Expectation Suites and add Expectations

To add a Data Source and an Expectation Suite, see [How to connect to a PostgreSQL database](/docs/0.15.50/guides/connecting_to_your_data/database/postgres#5-configure-your-datasource).

To add Expectations to your Suite individually, use the following code:

```
validator.expect_column_values_to_not_be_null("my_column")
validator.save_expectation_suite(discard_failed_expectations=False)
```

To configure your Expectation store to load a Suite at a later time, see [Configure Expectation Stores](../guides/setup/configuring_metadata_stores/configure_expectation_stores.md).

## Run validation

To create and run a Checkpoint in code, see [How to create a new Checkpoint](../guides/validation/checkpoints/how_to_create_a_new_checkpoint.md).  In a hosted environment you will not be able to store the Checkpoint for repeated use across Python sessions, but you can recreate it each time your scripts run.

## Use Data Docs

To build and view Data Docs in your environment, see [Options for hosting Data Docs](../reference/customize_your_deployment.md#options-for-hosting-data-docs).
