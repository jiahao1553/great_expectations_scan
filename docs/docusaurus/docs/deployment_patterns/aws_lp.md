---
title: "Integrate Great Expectations with AWS"
sidebar_label: "Amazon Web Services (AWS)"
description: "Integrate Great Expectations with AWS"
id: aws_lp
---

import LinkCardGrid from '/docs/components/LinkCardGrid';
import LinkCard from '/docs/components/LinkCard';

<p class="DocItem__header-description">Integrate Great Expectations (GX) with AWS Glue, AWS with S3 and Pandas, AWS with S3 and Spark, AWS with Athena, AWS with Redshift, AWS EMR Serverless, and EMR Spark.</p>

<LinkCardGrid>
  <LinkCard topIcon label="Use Great Expectations with AWS Glue" description="Set up, initialize and run validations against your data on AWS Glue Spark Job" href="/docs/deployment_patterns/how_to_use_great_expectations_in_aws_glue" icon="/img/integrations/aws_glue_icon.svg" />
  <LinkCard topIcon label="Use GX with an Amazon EMR Spark cluster" description="Instantiate a Data Context on an EMR Spark cluster" href="/docs/deployment_patterns/how_to_instantiate_a_data_context_on_an_emr_spark_cluster" icon="/img/integrations/spark_icon.png" />
<LinkCard topIcon label="Use GX with AWS EMR Serverless" description="Use GX with a serverless Amazon EMR deployment" href="/docs/deployment_patterns/how_to_use_great_expectations_in_emr_serverless" icon="/img/integrations/emr_serverless_icon.png" />
  <LinkCard topIcon label="Use GX with AWS using S3 and Pandas" description="Use GX with AWS and cloud storage" href="/docs/deployment_patterns/how_to_use_gx_with_aws/how_to_use_gx_with_aws_using_cloud_storage_and_pandas" icon="/img/integrations/pandas_icon.png" />
  <LinkCard topIcon label="Use GX with AWS using S3 and Spark" description="Configure a local GX project to store Expectations, Validation Results, and Data Docs in Amazon S3 buckets" href="/docs/deployment_patterns/how_to_use_gx_with_aws/how_to_use_gx_with_aws_using_s3_and_spark" icon="/img/integrations/aws_logo.svg" />
  <LinkCard topIcon label="Use GX with AWS using Athena" description="Store Expectations, Validation Results, and Data Docs in Amazon S3 buckets and  access data stored in an Athena database" href="/docs/deployment_patterns/how_to_use_gx_with_aws/how_to_use_gx_with_aws_using_s3_and_spark" icon="/img/integrations/athena_logo.svg" />
  <LinkCard topIcon label="Use GX with AWS using Redshift" description="Store Expectations, Validation Results, and Data Docs in Amazon S3 buckets and access data data from a Redshift database" href="/docs/deployment_patterns/how_to_use_gx_with_aws/how_to_use_gx_with_aws_using_s3_and_spark" icon="/img/integrations/aws_redshift_icon.svg" />
</LinkCardGrid>