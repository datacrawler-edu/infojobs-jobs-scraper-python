# Output reference

Each successful Dataset row has this shape:

```json
{
  "searchUrl": "https://www.infojobs.net/ofertas-trabajo/espana?...",
  "scrapedAt": "2026-09-24T09:11:02Z",
  "offer": {
    "code": "public-offer-code",
    "title": "Job title",
    "description": "Public description",
    "city": "Madrid",
    "link": "https://www.infojobs.net/...",
    "contractType": "Contrato indefinido",
    "workday": "Jornada completa",
    "teleworking": "Híbrido",
    "publishedAt": "2026-09-17T08:16:28Z",
    "companyName": "Company",
    "companyLogo": "https://...",
    "companyLink": "https://...",
    "states": [],
    "upsellings": [],
    "executive": false,
    "newBOId": "public-infojobs-identifier",
    "detail": null
  }
}
```

The complete real item is in [../data/sample-output.json](../data/sample-output.json).
The `detail` object is `null` unless `includeDetails` is enabled and the public
detail response contains valid data. It can include salary, requirements,
skills, studies, company ratings, applications, categories and benefits.

The default Key-Value Store also contains a `SUMMARY` record with completion
status, page counts, saved-item counts, duplicate counts and detail skips.

