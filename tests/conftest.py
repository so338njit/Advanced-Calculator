"""faker testing file"""
# pylint: disable=unused-import
from decimal import Decimal
import pytest
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    """function for operations mapping for Calculator and Calculation tests"""
    operation_mapping = {
        'add' : add,
        'subtract' : subtract,
        'multiply' : multiply,
        'divide' : divide
    }

    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mapping.keys()))
        operation_func = operation_mapping[operation_name]

        if operation_name == 'divide':
            b = Decimal('1') if b == Decimal('0') else b

        try:
            if operation_name == 'divide' and b == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"

        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    """generic addoption parameters"""
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """Check if the test is expecting any of the dynamically generated fixtures"""
    if{"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)
