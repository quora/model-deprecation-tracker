from scraper.openai_scraper import scrape as scrape_openai
from scraper.anthropic_scraper import scrape as scrape_anthropic
from scraper.vertex_scraper import scrape as scrape_vertex
from scraper.bedrock_scraper import scrape as scrape_bedrock
from scraper.gemini_scraper import scrape as scrape_gemini
from scraper.azure_foundry_scraper import scrape as scrape_azure_foundry

ALL_SCRAPERS = [
    ("OpenAI", scrape_openai),
    ("Anthropic", scrape_anthropic),
    ("Vertex AI", scrape_vertex),
    ("Bedrock", scrape_bedrock),
    ("Gemini", scrape_gemini),
    ("Azure Foundry", scrape_azure_foundry),
]
