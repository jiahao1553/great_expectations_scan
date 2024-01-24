---
title: Data Source
id: datasource
hoverText: Provides a standard API for accessing and interacting with data from a wide variety of source systems.
---
import TechnicalTag from '../term_tags/_tag.mdx';

A Data Source provides a standard API for accessing and interacting with data from a wide variety of source systems.

Data Sources provide a standard API across multiple backends: the Data Source API remains the same for PostgreSQL, CSV Filesystems, and all other supported data backends.
:::note Important: 

Data Sources do not modify your data.

:::

## Relationship to other objects

Data Sources function by bringing together a way of interacting with Data (an <TechnicalTag relative="../" tag="execution_engine" text="Execution Engine" />) with a definition of the data to access (a Data Asset).  <TechnicalTag relative="../" tag="batch_request" text="Batch Requests" /> utilize a Data Sources' Data Assets to return a <TechnicalTag relative="../" tag="batch" text="Batch" /> of data.

## Use Cases

When connecting to data the Data Source is your primary tool. At this stage, you will create Data Sources to define how Great Expectations can find and access your <TechnicalTag relative="../" tag="data_asset" text="Data Assets" />.  Under the hood, each Data Source uses an Execution Engine (ex: SQLAlchemy, Pandas, and Spark) to connect to and query data. Once a Data Source is configured you will be able to operate with the Data Source's API rather than needing a different API for each possible data backend you may be working with.

When creating <TechnicalTag relative="../" tag="expectation" text="Expectations" />, you'll use your Data Sources to obtain <TechnicalTag relative="../" tag="batch" text="Batches" /> for analysis and for your <TechnicalTag relative="../" tag="expectation_suite" text="Expectation Suites" />. For example, when you use [the interactive workflow](../guides/expectations/how_to_create_and_edit_expectations_with_instant_feedback_from_a_sample_batch_of_data.md) to create new Expectations.

Data Sources are also used to obtain Batches for <TechnicalTag relative="../" tag="validator" text="Validators" /> to run against when you are validating data.

## Standard API

Data Sources support connecting to a variety of different data backends. No matter which Data Source you use, the Data Source's API remains the same.

## No unexpected modifications

Data Sources do not modify your data during profiling or validation, but they may create temporary artifacts to optimize computing Metrics and Validation (this behavior can be configured).

## Create and access

Data Sources can be created and accessed using Python code, which can be executed from a script, a Python console, or a Jupyter Notebook. To access a Data Source all you need is a <TechnicalTag relative="../" tag="data_context" text="Data Context" /> and the name of the Data Source. The below snippet shows how to create a Pandas Data Source for local files:

```python name="tests/integration/docusaurus/connecting_to_your_data/connect_to_your_data_overview add_datasource"
```

This next snippet shows how to retrieve the Data Source from the Data Context.

```python name="tests/integration/docusaurus/connecting_to_your_data/connect_to_your_data_overview config"
```

For detailed instructions on how to create Data Sources that are configured for various backends, see [our documentation on Connecting to Data Sources](../guides/connecting_to_your_data/connect_to_data_lp.md).

