import sys
import pytest
from pydantic import ValidationError

sys.path.insert(0, r"C:\swarali\vs code folder\lerning-folder\fastapi-lerning\practice\03_request-body-pydantic")

from schemas import Item

# Test 1: Valid data
def test_correct_data():
    item = Item(name="Laptop", price=999.99)
    assert item.name == "Laptop"
    assert item.price == 999.99
    assert item.description is None
    assert item.in_stock == True

# Test 2: Invalid data
def test_wrong_data():
    with pytest.raises(ValidationError):
        Item(name="Laptop", price="wrong_data")

# Test 3: model_dump
def test_model_dump():
    item = Item(name="Laptop", price=999.99)
    result = item.model_dump()
    assert result["name"] == "Laptop"
    assert result["price"] == 999.99

# Test 4: exclude_unset
def test_exclude_unset():
    item = Item(name="Laptop", price=999.99)
    result = item.model_dump(exclude_unset=True)
    assert "description" not in result
    assert "in_stock" not in result