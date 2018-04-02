import functools

try:
    import asyncio
    asyncio_enabled = True
except ImportError:
    asyncio_enabled = False


def maybe_await(result):
    if asyncio_enabled:
        z = yield from result
        return z
    return result
