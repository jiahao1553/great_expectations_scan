---
title: Update Data Docs after Validating a Checkpoint
---

import Prerequisites from '../../../guides/connecting_to_your_data/components/prerequisites.jsx';
import TechnicalTag from '@site/docs/term_tags/_tag.mdx';

This guide will explain how to use an <TechnicalTag tag="action" text="Action" /> to update <TechnicalTag tag="data_docs" text="Data Docs" /> sites with new <TechnicalTag tag="validation_result" text="Validation Results" /> from running a <TechnicalTag tag="checkpoint" text="Checkpoint" />.

## Prerequisites

<Prerequisites>

 - [A minimum of one Expectation Suite](../../expectations/expectations_lp.md)
 - [A minimum of one Checkpoint](../checkpoints/how_to_create_a_new_checkpoint.md).

</Prerequisites>

## Update your Checkpoint

A Checkpoint's ``action_list`` contains a list of Actions.  After the Checkpoint is <TechnicalTag tag="validation" text="Validated" />, these Actions are called in order. 

Add an Action to the end of the ``action_list`` and name it ``update_data_docs``.

Actions are required to have a single field, ``action``.  Inside the ``action`` field, a ``class_name`` field must be defined, which determines which class will be instantiated to execute this Action. 

Add ``class_name: UpdateDataDocsAction`` to the Action.

:::note Note:
The ``StoreValidationResultAction`` Action must appear before  ``UpdateDataDocsAction`` Action, since Data Docs are rendered from Validation Results from the <TechnicalTag tag="store" text="Store" />.
:::

```yaml
 action_list:
   - name: store_validation_result
     action:
       class_name: StoreValidationResultAction
   - name: store_evaluation_params
     action:
       class_name: StoreEvaluationParametersAction
   - name: update_data_docs
     action:
       class_name: UpdateDataDocsAction
```

## Specify Data Docs sites (Optional)

- By default, the ``UpdateDataDocsAction`` updates all Data Docs sites found within your project. 
  To specify which Data Docs sites to update, provide a ``site_names`` key to the ``action`` config inside your ``UpdateDataDocsAction``.
  This field accepts a list of Data Docs site names, and when provided, will only update the specified sites.

```yaml
 action_list:
   - name: store_validation_result
     action:
       class_name: StoreValidationResultAction
   - name: store_evaluation_params
     action:
       class_name: StoreEvaluationParametersAction
   - name: update_data_docs
     action:
       class_name: UpdateDataDocsAction
       site_names:
         - team_site
```

## Test your configuration

Test that your new Action is configured correctly:

Run the following command to run the Checkpoint and verify that no errors are returned:

```python
import great_expectations as gx
context = gx.get_context()
checkpoint_name = "your checkpoint name here"
context.run_checkpoint(checkpoint_name=checkpoint_name)
```

Finally, check your Data Docs sites to confirm that a new Validation Result has been added.

## Additional notes

The ``UpdateDataDocsAction`` generates an HTML file for the latest Validation Result and updates the index page to link to the new file, and re-renders pages for the <TechnicalTag tag="expectation_suite" text="Expectation Suite" /> used for that Validation. It does not perform a full rebuild of Data Docs sites. This means that if you wish to render older Validation Results, you should run full Data Docs rebuild (via CLI's ``great_expectations docs build`` command or by calling ``context.build_data_docs()``).


## Related documentation

- [Checkpoints overview page](../../../terms/checkpoint.md)
- [Actions overview page](../../../terms/action.md)
