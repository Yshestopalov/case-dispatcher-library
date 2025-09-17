from typing import Callable, Any, Optional, Union, List, Tuple
import inspect
import asyncio
import sys


class CaseDispatcher:
    def __init__(self):
        self.case_map: List[Tuple[Union[Any, Callable[[Any], bool]], Callable]] = []
        self.default_case: Optional[Callable] = None

    def set_default(self, default_func: Callable):
        self.default_case = default_func

    def case(self, key: Union[Any, Callable[[Any], bool]]):
        def decorator(func: Callable):
            self.case_map.append((key, func))
            return func
        return decorator

    def add_case(self, key: Union[Any, Callable[[Any], bool]], func: Callable):
        self.case_map.append((key, func))

    async def run(self, value: Any, *args, **kwargs) -> Any:
        for key, func in self.case_map:
            match = key(value) if callable(key) else key == value
            if match:
                return await self._maybe_await(func, *args, **kwargs)

        if self.default_case:
            return await self._maybe_await(self.default_case, *args, **kwargs)
        return None

    async def _maybe_await(self, func: Callable, *args, **kwargs):
        if inspect.iscoroutinefunction(func):
            return await func(*args, **kwargs)
        return func(*args, **kwargs)

