---
title: Create a new Checkpoint
---

import TechnicalTag from '@site/docs/term_tags/_tag.mdx';
import Preface from './components_how_to_create_a_new_checkpoint/_preface.mdx'
import StepsForCheckpoints from './components_how_to_create_a_new_checkpoint/_steps_for_checkpoints_.mdx'
import AdditionalResources from './components_how_to_create_a_new_checkpoint/_additional_resources.mdx'

<Preface />

<StepsForCheckpoints />

## Create a Checkpoint

To modify the following code for your use case, replace `batch_request` and `expectation_suite_name` with your own paremeters.

```python name="tests/integration/docusaurus/validation/checkpoints/how_to_create_a_new_checkpoint.py create checkpoint batch_request"
```

For other Checkpoint configuration options, see [Manage Checkpoints](../../../guides/validation/checkpoints/checkpoint_lp.md).


## Run your Checkpoint (Optional)

```python name="tests/integration/docusaurus/validation/checkpoints/how_to_create_a_new_checkpoint.py run checkpoint batch_request"
```

The returned `checkpoint_result` contains information about the checkpoint run.

## Build Data Docs (Optional)

Run the following Python code to build <TechnicalTag tag="data_docs" text="Data Docs" /> with the latest checkpoint run results:

```python name="tests/integration/docusaurus/validation/checkpoints/how_to_create_a_new_checkpoint.py build data docs"
```

## Retrieve your Checkpoint (Optional)

Run the following Python code to retrieve the Checkpoint:

```python name="tests/integration/docusaurus/validation/checkpoints/how_to_create_a_new_checkpoint.py get checkpoint"
```

## Related documentation
<AdditionalResources />
