# Architecture

```mermaid
flowchart TD
    A[main.py] --> B[domains]
    A --> C[utils]
    B --> B1[arithmetic.py]
    B --> B2[algebra.py]
    B --> B3[geometry.py]
    B --> B4[word_numbers.py]
    B --> B5[story_single_step.py]
    B --> B6[story_multi_step.py]
    B --> B7[units_rates.py]
    B --> B8[proportional.py]
    B --> B9[mixed_domain.py]
    C --> C1[randomizers.py]
    C --> C2[expression_builder.py]
    C --> C3[reasoning_steps.py]
    C --> C4[templates.py]
    C --> C5[noise.py]
    C --> C6[word_to_number.py]
    C --> C7[stress_generators.py]
    C --> C8[config.py]
```

- `math_dataset_generator/main.py`:
  - CLI entry point
  - Dispatches to domains
- `math_dataset_generator/domains/`:
  - Each file implements a domain-specific generator
- `math_dataset_generator/utils/`:
  - Shared utilities for randomization, expressions, reasoning, noise, config
- `tests/`:
  - Unit tests for core utilities and domains
