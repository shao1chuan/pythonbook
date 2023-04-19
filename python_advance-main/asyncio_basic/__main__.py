import asyncio


async def calculate(n_1: int, n_2: int):
    res = n_1 + n_2
    print(res)


async def main():
    print("main -step 1")
    await calculate(1, 2)
    print("main -step 2")


asyncio.run(main())
