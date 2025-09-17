from case_dispatcher import CaseDispatcher
import asyncio

dispatcher = CaseDispatcher()


@dispatcher.case("async")
async def async_case():
    await asyncio.sleep(1)
    print("Handled asynchronously.")

asyncio.run(dispatcher.run("async"))  # Output (after 1s): Handled asynchronously.
