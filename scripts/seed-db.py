#!/usr/bin/env python3
"""
Development seed entrypoint.

Keep this as a stable command for future seed data. The script does not mutate
the database until the application's explicit seed endpoint/service exists.
"""

import os
import sys

def main() -> int:
    enabled = os.getenv("ENABLE_DEV_SEED", "false").lower() == "true"

    if not enabled:
        print("Development seeding is disabled.")
        print("Set ENABLE_DEV_SEED=true when the seed service is implemented.")
        return 0

    print("Seed service is enabled, but no seed implementation is registered yet.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
