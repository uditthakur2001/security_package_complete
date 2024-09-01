"""
TruffleHog - Find secrets in your code.

This module serves as the entry point for the TruffleHog command-line tool.
"""

import sys
import os
from .trufflehog import main

def run():
    """Run the TruffleHog tool."""
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

# If this script is executed directly, run the tool
if __name__ == "__main__":
    run()
