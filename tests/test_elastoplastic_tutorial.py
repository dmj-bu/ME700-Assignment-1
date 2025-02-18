import pytest
from Elasto_Plastic_Model.elastoplastic_tutorial import run_examples

def test_tutorial_execution():
    """ Ensure the tutorial script runs without errors. """
    try:
        run_examples()
    except Exception as e:
        pytest.fail(f"Tutorial script failed with error: {e}")
