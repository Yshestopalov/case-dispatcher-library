# 🧠 Case Dispatcher

**Case Dispatcher** is a lightweight Python library designed to simplify complex control flow by replacing repetitive `if-elif-else` chains with clean, declarative case mappings. Whether you're writing synchronous or asynchronous code, Case Dispatcher helps you organize logic around values or conditions with minimal boilerplate.

## ✨ Features

- ✅ Register cases using decorators or direct method calls  
- 🔄 Supports both synchronous and asynchronous functions  
- 🧩 Match by exact value or custom predicate function  
- 🧼 Optional default case handling  
- 🧪 Clean separation of logic for readability and maintainability

## 🧩 Example

```python
from case_dispatcher import CaseDispatcher
import asyncio

dispatcher = CaseDispatcher()

# Basic value match
@dispatcher.case("hello")
def greet():
    print("Hello!")

# Predicate (condition) match
@dispatcher.case(lambda x: isinstance(x, int) and x > 5)
def handle_large_number():
    print("That's a large number!")

# Async function match
@dispatcher.case("wait")
async def wait_case():
    await asyncio.sleep(1)
    print("Handled asynchronously.")

# Default fallback
dispatcher.set_default(lambda: print("No match found."))

# Run dispatcher with different inputs
async def run_examples():
    await dispatcher.run("hello")   # Output: Hello!
    await dispatcher.run(10)        # Output: That's a large number!
    await dispatcher.run("wait")    # Output (after 1s): Handled asynchronously.
    await dispatcher.run("unknown") # Output: No match found.

asyncio.run(run_examples())

