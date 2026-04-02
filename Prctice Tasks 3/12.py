"""
Write a Python program that builds a concurrent task scheduler using asyncio.
"""
import asyncio

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, coro):
        self.tasks.append(coro)

    async def run(self):
        print("Running tasks...\n")
        results = await asyncio.gather(*self.tasks)
        return results


async def task1():
    await asyncio.sleep(2)
    print("Task 1 done")
    return "Result 1"

async def task2():
    await asyncio.sleep(1)
    print("Task 2 done")
    return "Result 2"


async def main():
    scheduler = TaskScheduler()
    
    scheduler.add_task(task1())
    scheduler.add_task(task2())
    
    results = await scheduler.run()
    print("\nResults:", results)


asyncio.run(main())