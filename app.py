from fastapi import FastAPI
import uvicorn
from crawler import Crawler

app = FastAPI()
crawler = Crawler()

@app.get("/search/")
async def search(keyword: str):
    result = crawler.GetData(keyword)
    return result
