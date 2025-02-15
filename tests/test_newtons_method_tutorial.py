import sys
from pathlib import Path

# Ensure Python recognizes src/ as a module
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

import Newtons_Method.newtons_method_tutorial as tutorial

def test_run_examples():
    tutorial.run_examples()  # Ensure this executes properly
