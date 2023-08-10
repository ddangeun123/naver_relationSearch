from fastapi import FastAPI
from crawler import Crawler

app = FastAPI()
crawler = Crawler()

@app.get("/search/")
async def search(keyword: str):
    result = crawler.GetData(keyword)
    return result
