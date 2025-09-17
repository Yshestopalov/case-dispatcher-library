from case_dispatcher import CaseDispatcher
import asyncio

dispatcher = CaseDispatcher()


@dispatcher.case("greet")
def say_hello():
    print("Hello!")


@dispatcher.case(lambda x: x > 10)
def handle_large_number():
    print("That's a big number!")


dispatcher.set_default(lambda: print("No match found"))


asyncio.run(dispatcher.run("greet"))  # Output: Hello!
