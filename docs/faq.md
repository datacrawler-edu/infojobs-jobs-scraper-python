# FAQ

## Does this use an external jobs API?

No. The hosted Actor reads public InfoJobs search and detail responses. It does
not require an InfoJobs API key or login.

## Why did I receive fewer jobs than `maxItems`?

`maxItems` is an upper bound. The search can contain fewer matching public
offers, pagination can end, or duplicate offers can be removed.

## Are duplicate jobs returned across pages?

No. Offers are deduplicated by public offer code, with the listing URL as a
fallback when no code is available.

## Is detail enrichment guaranteed?

No. Detail enrichment is optional and best effort. The main listing remains
available when a detail response is unavailable or challenged.

## What happens when InfoJobs returns a verification page?

The Actor validates response content instead of accepting an HTTP 200 page as
successful data. A problem with the main search is reported in `SUMMARY`; a
problem limited to optional detail enrichment preserves the listing.

## What is billed?

One event is billed for each unique job listing delivered to the default
Dataset. Empty runs, duplicates, failed requests and skipped optional detail
fields are not billable result events.

