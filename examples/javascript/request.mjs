import { ApifyClient } from 'apify-client';

const token = process.env.APIFY_API_TOKEN;
if (!token) {
    throw new Error('Set APIFY_API_TOKEN before running this example.');
}

const input = {
    keyword: 'python',
    location: 'Madrid',
    remote: 'any',
    contractType: 'any',
    workday: 'any',
    publishedWithinDays: 'any',
    sortBy: 'relevance',
    maxItems: 5,
    includeDetails: false,
};

const client = new ApifyClient({ token });
const run = await client.actor('datascraperes/infojobs-jobs-scraper').call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(JSON.stringify(items, null, 2));

