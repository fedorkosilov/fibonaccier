#!/usr/bin/env python3

import asyncio
import random
import time
from typing import Tuple, Union


async def fib(n: int, readable_output: bool = False) -> Union[int, Tuple[int, float]]:
    start_time = time.time()

    # Add a random delay
    delay = random.uniform(0, 1)
    await asyncio.sleep(delay)

    # Calculate the Fibonacci number using recursion
    if n <= 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = await fib(n - 1) + await fib(n - 2)

    end_time = time.time()

    if readable_output:
        return f"fib({n}) = {result}, time = {end_time - start_time:.2f} seconds"
    else:
        return result


async def main(number: int) -> None:
    # Run two Fibonacci calculations concurrently
    group = asyncio.gather(fib(number, True), fib(number, True))
    # Wait for both calculations to finish
    await group
    # Print the results
    print("Results:")
    for result in group.result():
        print(result)


if __name__ == "__main__":
    while True:
        # Get a positive integer from the user
        try:
            number = int(input("Enter an integer: "))
            if number > 0:
                break
            else:
                print("Invalid input. Please, enter a positive integer (>0).")
        except ValueError:
            print("Invalid input. Please, enter a valid positive integer.")
    asyncio.run(main(number))
