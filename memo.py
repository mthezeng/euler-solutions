def memo(f):
    """Decorator which adds memoization to recursive functions"""
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized
