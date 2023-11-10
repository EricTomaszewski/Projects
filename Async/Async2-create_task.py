# This one is:
# asyncio.create_task()

# In summary, 
# if you need to start a coroutine and continue with the rest of your code without waiting for it to complete, use asyncio.create_task. 
# If you have multiple coroutines and want to wait for all of them to complete before proceeding, use asyncio.gather. The choice between them depends on the specific requirements of your code.

import asyncio
import time

async def brewCoffee():
    print("Start brewCoffee()")
    # time.sleep(3)
    await asyncio.sleep(3)
    print("End brewCoffee()")
    return "Coffee ready"

async def toastBagel():
    print("Start toastBagel()")
    # time.sleep(2)
    await asyncio.sleep(2)
    print("End toastBagel()")
    return "Bagel toasted"

async def main():
    start_time = time.time()
    
    # result_coffee = brewCoffee()
    # result_bagel = toastBagel()
    # batch = asyncio.gather(brewCoffee(), toastBagel())
    # result_coffee, result_bagel = await batch
    coffee_task = asyncio.create_task(brewCoffee())
    toast_task = asyncio.create_task(toastBagel())
    result_coffee = await coffee_task
    result_bagel = await toast_task
    
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    print(f"Result of brewCoffee: {result_coffee}")
    print(f"Result of toastBagel: {result_bagel}")
    print(f"Total execution time: {elapsed_time:.2f} seconds")
    
if __name__ == "__main__":
    # main()
    asyncio.run(main())