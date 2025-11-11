# Project Reflection
Author: Roopesh Kumar Reddy Kaipa
Date: 11/10/2025
---

This project focused on improving code clarity, hardening authentication by replacing plaintext password storage with a `password_hash` and a write-only `password` setter, and building a reliable test suite (unit, integration, and Playwright e2e) that tolerates environment differences by using an in-memory SQLite fallback when Postgres is unavailable; during CI work I resolved dependency-resolution conflicts (by loosening exact pins for `fastapi`, `httpcore`, and `httpx`) so pip could select compatible versions for `h11` and `starlette`, and addressed container-scanner findings by upgrading vulnerable packages where possible, learning in the process that reproducible lockfiles, automated dependency updates, and resilient tests are essential to keep deployment pipelines secure and stable.
Diagnosis: The conflict tree reported constraints such as


