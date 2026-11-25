# Synthetic example: google-ads-audit

This fixture is fictional and contains no real account data.

## Input

Synthetic search campaigns; same currency (EUR), 30 days; target CPA €50. Brand: spend 300, clicks 300, conversions 15. Nonbrand: spend 900, clicks 450, conversions 9. No search term file.

Apply the skill and return its specified deliverable.

## Expected checks

Brand CPA €20, nonbrand CPA €100, total CPA €50; flag nonbrand for investigation, not automatic pause. Do not invent negative keywords.

The answer should also pass the skill's validation checklist. This is a human-review acceptance fixture, not a recorded model test result.
