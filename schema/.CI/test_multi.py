import pytest
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import json

def test_multi_idfree():
    with open('schema/current/examples/multi_idfree.qc.json') as f:
        data = json.load(f)
    with open('schema/current/schema.json') as f:
        schema = json.load(f)
    validate(instance=data, schema=schema)
    
def test_multi_broken1():
    with open('schema/current/schema.json') as f:
        schema = json.load(f)
    with open('schema/current/examples/multi_broken1.qc.json') as f:
        broken = json.load(f)
    with pytest.raises(ValidationError):
        validate(instance=broken, schema=schema)

