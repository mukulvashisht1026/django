"""Explicit offline demonstration; run from this repository root."""
import json

cache = {}
def geocode(name):
    key = name.strip().lower()
    if not key:
        raise ValueError('location is required')
    if key not in cache:
        cache[key] = {'name': name, 'lat': 0.0, 'lon': 0.0, 'source': 'mock coordinates'}
    return cache[key]
first = geocode('Bangalore')
assert geocode('Bangalore') is first
result = {'mode': 'offline cache mock; coordinates are invented', 'location': first, 'cached_entries': len(cache)}

print(json.dumps(result, indent=2, sort_keys=True))
