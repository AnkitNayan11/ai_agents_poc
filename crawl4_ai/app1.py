import json
import asyncio
from crawl4_ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4_ai import JsonCssExtractionStrategy


ecommerce_schema = {
    "name": "E-commerce Product Catalog",
    "baseSelector": "div.category",
    # (1) We can define optional baseFields if we want to extract attributes 
    # from the category container
    "baseFields": [
        {"name": "data_cat_id", "type": "attribute", "attribute": "data-cat-id"}, 
    ],
    "fields": [
        {
            "name": "category_name",
            "selector": "h2.category-name",
            "type": "text"
        },
        {
            "name": "products",
            "selector": "div.product",
            "type": "nested_list",    # repeated sub-objects
            "fields": [
                {
                    "name": "name",
                    "selector": "h3.product-name",
                    "type": "text"
                },
                {
                    "name": "price",
                    "selector": "p.product-price",
                    "type": "text"
                },
                {
                    "name": "details",
                    "selector": "div.product-details",
                    "type": "nested",  # single sub-object
                    "fields": [
                        {
                            "name": "brand",
                            "selector": "span.brand",
                            "type": "text"
                        },
                        {
                            "name": "model",
                            "selector": "span.model",
                            "type": "text"
                        }
                    ]
                },
                {
                    "name": "features",
                    "selector": "ul.product-features li",
                    "type": "list",
                    "fields": [
                        {"name": "feature", "type": "text"} 
                    ]
                },
                {
                    "name": "reviews",
                    "selector": "div.review",
                    "type": "nested_list",
                    "fields": [
                        {
                            "name": "reviewer", 
                            "selector": "span.reviewer", 
                            "type": "text"
                        },
                        {
                            "name": "rating", 
                            "selector": "span.rating", 
                            "type": "text"
                        },
                        {
                            "name": "comment", 
                            "selector": "p.review-text", 
                            "type": "text"
                        }
                    ]
                },
                {
                    "name": "related_products",
                    "selector": "ul.related-products li",
                    "type": "list",
                    "fields": [
                        {
                            "name": "name", 
                            "selector": "span.related-name", 
                            "type": "text"
                        },
                        {
                            "name": "price", 
                            "selector": "span.related-price", 
                            "type": "text"
                        }
                    ]
                }
            ]
        }
    ]
}


async def extract_ecommerce_data():
    strategy = JsonCssExtractionStrategy(ecommerce_schema, verbose=True)

    config = CrawlerRunConfig()

    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(
            url="https://gist.githubusercontent.com/githubusercontent/2d7b8ba3cd8ab6cf3c8da771ddb36878/raw/1ae2f90c6861ce7dd84cc50d3df9920dee5e1fd2/sample_ecommerce.html",
            extraction_strategy=strategy,
            config=config
        )

        if not result.success:
            print("Crawl failed:", result.error_message)
            return

        # Parse the JSON output
        data = json.loads(result.extracted_content)
        print(json.dumps(data, indent=2) if data else "No data found.")

asyncio.run(extract_ecommerce_data())
