from case_dispatcher import CaseDispatcher
import asyncio

dispatcher = CaseDispatcher()


@dispatcher.case("start")
def start():
    print("Starting...")


@dispatcher.case("stop")
def stop():
    print("Stopping...")


asyncio.run(dispatcher.run("start"))  # Output: Starting...
