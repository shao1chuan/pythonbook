import asyncio
from asyncio.exceptions import TimeoutError


async def play_music(music: str):
    print(f"Start playing {music}")
    await asyncio.sleep(3)
    print(f"Finished playing {music}")

    return music


async def call_api():
    print("calling api.....")
    raise Exception("Error calling")


async def my_cancel():
    task = asyncio.create_task(play_music("A"))

    await asyncio.sleep(3)

    if not task.done():
        task.cancel()


async def my_cancel_with_timeout():
    task = asyncio.create_task(play_music("B"))

    try:
        await asyncio.wait_for(task, timeout=2)
    except TimeoutError:
        print("timeout")


async def my_timeout():
    task = asyncio.create_task(play_music("B"))

    try:
        await asyncio.wait_for(asyncio.shield(task), timeout=2)
    except TimeoutError:
        print("timeout")
        await task


async def my_gather():
    results = await asyncio.gather(play_music("A"), play_music("B"))
    print(results)


async def my_gather_with_exception():
    results = await asyncio.gather(play_music("A"), play_music("B"), call_api(),
                                   return_exceptions=True)
    print(results)

if __name__ == "__main__":
    asyncio.run(my_gather_with_exception())
