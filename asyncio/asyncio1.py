import asyncio

async def minutes(x):
    for i in range(x, 1, -1):
        print(f'Осталось {i} мин.')
        await asyncio.sleep(60)
    print(f'Осталась 1 мин.')


async def seconds(x):
    for i in range(x, 0, -1):
        print(f'Осталось {i} сек.')
        await asyncio.sleep(1)


async def run_timer():

    await minutes(3)
    await seconds(60)

    print('Время вышло!')

coroutine = run_timer()
asyncio.run(coroutine)
