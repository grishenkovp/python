from time import time
import asyncio

start = time()

async def spider(site_name):
    for page in range(1,4):
        await asyncio.sleep(1)
        print(site_name, page)

spider = [
    asyncio.ensure_future(spider("Blog")),
    asyncio.ensure_future(spider("News")),
    asyncio.ensure_future(spider("Forum"))
]

event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(asyncio.gather(*spider))
event_loop.close()

print("{:.2F}".format(time()-start))