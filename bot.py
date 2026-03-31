import os
import sys

# Evita conflito entre bot.py e pacote bot/
package_dir = os.path.join(os.path.dirname(__file__), "bot")
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

from app import main

if __name__ == "__main__":
    main()
