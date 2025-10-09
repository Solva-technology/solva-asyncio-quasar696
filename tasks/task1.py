import aiohttp
import asyncio
import pytest


async def fetch_status(session, url):
    async with session.get(url) as response:
        return response.status


async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_status(session, url) for url in urls]
        return await asyncio.gather(*tasks)


@pytest.mark.asyncio
async def test_fetch_status_200():
    url = "https://httpbin.org/status/200"
    async with aiohttp.ClientSession() as session:
        status = await fetch_status(session, url)
        assert status == 200
