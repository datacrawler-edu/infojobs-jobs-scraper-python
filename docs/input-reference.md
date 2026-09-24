# Input reference

The hosted Actor accepts one JSON object. `keyword` is required; all other
fields are optional and have the defaults shown below.

| Field | Type | Default | Accepted values or limit |
| --- | --- | --- | --- |
| `keyword` | string | required | 1–200 characters. |
| `location` | string | empty | City or province in Spain, up to 100 characters. |
| `remote` | select | `any` | `any`, `remote`, `hybrid`, `onsite`, `unspecified`. |
| `contractType` | select | `any` | `any`, `permanent`, `temporary`, `training`, `discontinuous`, `self_employed`, `part_time`, `other`. |
| `workday` | select | `any` | `any`, `full_time`, `morning_part_time`, `afternoon_part_time`, `intensive_morning`, `indifferent`. |
| `publishedWithinDays` | select | `any` | `any`, `1`, `7`, `15`. |
| `sortBy` | select | `relevance` | `relevance` or `date`. |
| `maxItems` | integer | `30` | 1–1,000 unique jobs. |
| `includeDetails` | boolean | `false` | Best-effort detail enrichment when `true`. |

`maxItems` is a maximum rather than a guaranteed count. Public search results
can change during collection, and duplicate offers are removed globally.

