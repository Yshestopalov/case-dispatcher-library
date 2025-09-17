from case_dispatcher import CaseDispatcher
import asyncio

dispatcher = CaseDispatcher()


@dispatcher.case(lambda x: isinstance(x, int) and x % 2 == 0)
def even_number():
    print("Even number detected.")


@dispatcher.case(lambda x: isinstance(x, int) and x % 2 != 0)
def odd_number():
    print("Odd number detected.")


asyncio.run(dispatcher.run(7))  # Output: Odd number detected.
