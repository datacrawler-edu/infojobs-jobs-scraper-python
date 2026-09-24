# cURL request

Set `APIFY_API_TOKEN` in the environment and call the hosted Actor through
Apify's synchronous Dataset endpoint:

```bash
curl --request POST \
  --url "https://api.apify.com/v2/acts/datascraperes~infojobs-jobs-scraper/run-sync-get-dataset-items?token=${APIFY_API_TOKEN}" \
  --header "Content-Type: application/json" \
  --data '{
    "keyword": "python",
    "location": "Madrid",
    "remote": "any",
    "contractType": "any",
    "workday": "any",
    "publishedWithinDays": "any",
    "sortBy": "relevance",
    "maxItems": 5,
    "includeDetails": false
  }'
```

The response is the JSON array returned by the Actor's default Dataset. Keep
the token in an environment variable and never commit it to a repository.

