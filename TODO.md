# Concrete follow-up work

- [x] Repair request.body.name (now reads request.POST). Still TODO: validate via LocationModelForm.
- [x] Use cache.get/cache.set instead of attribute access.
- [ ] Implement geocoder response handling, timeouts, and missing-template behavior.
- [x] Add supported Django pins (requirements.txt: Django 2.2.28; Redis cache is mocked by USE_MOCKS=1).
