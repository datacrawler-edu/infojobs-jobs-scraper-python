# InfoJobs Jobs Scraper — Python, JavaScript and cURL examples

Run the [InfoJobs Jobs Scraper on Apify](https://apify.com/datascraperes/infojobs-jobs-scraper?fpr=edudata) without managing scraping infrastructure. This repository contains public integration examples, a complete representative Dataset item, input documentation and small export samples for InfoJobs Spain job research.

## What this repository helps you do

- Search public InfoJobs Spain listings by keyword and optional location.
- Filter by remote work, contract type, work schedule, publication date and sort order.
- Collect unique titles, descriptions, companies, locations, dates, job URLs and promotion fields.
- Optionally request best-effort detail enrichment such as salary, skills, studies, ratings and benefits.
- Read the resulting Dataset from Python, JavaScript or cURL.

[Open the hosted Actor on Apify](https://apify.com/datascraperes/infojobs-jobs-scraper?fpr=edudata)

## Example result

The complete representative Dataset item is available in [data/sample-output.json](data/sample-output.json). A compact tabular export is available in [data/sample-output.csv](data/sample-output.csv).

~~~json
{
  "searchUrl": "https://www.infojobs.net/ofertas-trabajo/espana?keyword=python&page=1&sortBy=RELEVANCE&onlyForeignCountry=false&countryIds=17&sinceDate=ANY&provinceIds=33",
  "scrapedAt": "2026-09-24T09:11:02Z",
  "offer": {
    "code": "694a872eb84b0ba839fa86d91335d9",
    "title": "Desarrollador Senior Python (Híbrido)",
    "description": "Como Desarrollador Senior Python, formarás parte de un equipo ágil centrado en la construcción y evolución de servicios backend escalables y robustos. Colaborarás con DevOps y Product para definir y entregar soluciones basadas en contenedores que se desplieguen en entornos de producción con alta disponibilidad, contribuyendo a la estabilidad y mejora continua del ecosistema tecnológico de la empresa.\nPython: Es el lenguaje principal de desarrollo; necesitamos que domines su ecosistema y buenas prácticas para construir código mantenible y de alto rendimiento.\nFastAPI: Debes tener experiencia en su uso para desarrollar APIs modernas, rápidas y bien documentadas, aprovechando sus capacidades asíncronas y validación de datos.\nAPIs REST y/o GraphQL: Es esencial que hayas diseñado e implementado APIs que se integren con múltiples sistemas, priorizando la claridad, seguridad y escalabilidad.\nContenedores: Debes entender cómo empaquetar y ejecutar aplicaciones en entornos aislados, asegurando consistencia entre desarrollo, prueba y producción.\nLa modalidad de trabajo es híbrida (2 - 3 días en las oficinas del cliente) en la zona de IFEMA.",
    "city": "Madrid",
    "link": "https://www.infojobs.net/madrid/desarrollador-senior-python-hibrido/of-i694a872eb84b0ba839fa86d91335d9?applicationOrigin=search-new&page=1&sortBy=RELEVANCE",
    "contractType": "Contrato indefinido",
    "workday": "Jornada completa",
    "teleworking": "Híbrido",
    "publishedAt": "2026-09-17T08:16:28Z",
    "companyName": "DEVOTEAM",
    "companyLogo": "https://multimedia-logos.infojobs.net/image/upload/c8/c8ec5db1-715e-42b0-88b0-fc43822fc2eb",
    "companyLink": "https://devoteam.ofertas-trabajo.infojobs.net",
    "states": [],
    "upsellings": ["PROMOTED"],
    "executive": false,
    "newBOId": "ab33f2ae-c707-4945-a191-e4fbd970d48c"
  }
}
~~~

## Run without code

1. Open the [InfoJobs Jobs Scraper](https://apify.com/datascraperes/infojobs-jobs-scraper?fpr=edudata).
2. Enter a keyword such as `python` and optionally enter `Madrid` as the location.
3. Choose any filters, set the maximum number of unique jobs, and start the run.
4. Open the Dataset tab and export JSON, CSV or Excel.

The five public task presets provide focused starting points for Madrid Python
jobs, permanent Barcelona jobs, recent jobs, remote jobs and part-time jobs:

- [Madrid Python Jobs](https://apify.com/datascraperes/infojobs-madrid-python-jobs)
- [Permanent Barcelona Jobs](https://apify.com/datascraperes/infojobs-barcelona-permanent-jobs)
- [Recent Jobs by Date](https://apify.com/datascraperes/infojobs-recent-jobs-by-date)
- [Remote Jobs in Spain](https://apify.com/datascraperes/infojobs-remote-jobs-spain)
- [Part-time Jobs in Spain](https://apify.com/datascraperes/infojobs-part-time-jobs-spain)

## Quick start for developers

Install the official client for the language you use and provide an Apify
token through `APIFY_API_TOKEN`. The examples call the hosted Actor and read
its default Dataset; they do not require the private Actor source or any local
network configuration.

### Python

~~~bash
pip install -r examples/python/requirements.txt
export APIFY_API_TOKEN="your-token"
python examples/python/scrape_infojobs.py
~~~

On Windows PowerShell:

~~~powershell
$env:APIFY_API_TOKEN = "your-token"
python examples/python/scrape_infojobs.py
~~~

### JavaScript

~~~bash
npm install --prefix examples/javascript
APIFY_API_TOKEN="your-token" node examples/javascript/request.mjs
~~~

### cURL

See [examples/curl-request.md](examples/curl-request.md) for a synchronous
Dataset request using the official Apify API.

## Input example

~~~json
{
  "keyword": "python",
  "location": "Madrid",
  "remote": "any",
  "contractType": "any",
  "workday": "any",
  "publishedWithinDays": "any",
  "sortBy": "relevance",
  "maxItems": 1,
  "includeDetails": false
}
~~~

See [docs/input-reference.md](docs/input-reference.md) for every field,
default and accepted value.

## Output fields

Each successful Dataset item contains `searchUrl`, `scrapedAt` and one nested
`offer` object. The list fields include:

| Field | Meaning |
| --- | --- |
| `offer.code` | Public InfoJobs offer code used for deduplication when available. |
| `offer.title`, `offer.description` | Job title and public listing description. |
| `offer.city`, `offer.link` | Location and canonical public job URL. |
| `offer.contractType`, `offer.workday`, `offer.teleworking` | Public working-condition fields. |
| `offer.publishedAt` | Publication timestamp when supplied by InfoJobs. |
| `offer.companyName`, `offer.companyLogo`, `offer.companyLink` | Public company information. |
| `offer.states`, `offer.upsellings`, `offer.executive` | Public promotion and state fields. |
| `offer.newBOId` | Public identifier used by the detail contract. |
| `offer.detail` | Optional detail enrichment when the public detail response is available. |

When `includeDetails` is enabled, `offer.detail` can contain salary,
experience, studies, skills, categories, requirements, company ratings,
applications and social benefits. Missing detail fields are returned as null,
empty arrays or omitted according to the source response.

## Request examples

- [Python request](examples/python/scrape_infojobs.py)
- [JavaScript request](examples/javascript/request.mjs)
- [cURL request](examples/curl-request.md)

## Limits and pricing

`keyword` is required and accepts 1–200 characters. `location` is optional.
`maxItems` accepts 1–1,000 unique jobs and is an upper bound, not a guarantee.
The other filters use the choices exposed by the Actor input schema.

The billable unit is one unique job listing successfully delivered to the
default Dataset. Empty runs, failed requests, duplicates and skipped optional
detail fields are not billable events.

| Apify tier | Price per job result | Equivalent per 1,000 results |
| --- | ---: | ---: |
| Free | $0.00100 | $1.00 |
| Bronze | $0.00090 | $0.90 |
| Silver | $0.00080 | $0.80 |
| Gold | $0.00075 | $0.75 |
| Platinum | $0.00075 | $0.75 |
| Diamond | $0.00075 | $0.75 |

The 1,000-result values are comparison equivalents; billing remains per
successful job result. Check the [live Actor pricing](https://apify.com/datascraperes/infojobs-jobs-scraper?fpr=edudata) before a large run.

## Data quality and recovery

The Actor deduplicates offers across result pages. Source results can change
while a run is active, so a smaller Dataset than `maxItems` is valid when fewer
matching public offers are available or duplicates are encountered.

InfoJobs may return a verification page even with HTTP status 200. The Actor
validates the response content instead of treating that page as an empty
result. Optional detail enrichment is best effort: a challenged or unavailable
detail response preserves the main listing.

## FAQ

See [docs/faq.md](docs/faq.md) for answers about filters, details,
deduplication, pricing and incomplete source responses.

## Responsible use

Use the returned public job data lawfully and respect applicable terms,
privacy requirements and the rights of employers and applicants. Do not use
the data for spam, harassment, discrimination or unlawful automated decisions.

## Support

For an example or integration issue, [open a GitHub issue](https://github.com/datacrawler-edu/infojobs-jobs-scraper-python/issues) with sanitized input and error output. For an Actor execution issue, use the [Apify Actor page](https://apify.com/datascraperes/infojobs-jobs-scraper?fpr=edudata) and include the run ID. Never share API tokens.

## License

This repository is released under the MIT License.

