# Author: Roopesh Kumar Reddy Kaipa
# Date: 11/10/2025
import pytest

@pytest.mark.e2e
def test_hello_world(page, fastapi_server):
    page.goto('http://localhost:8000')
    page.wait_for_selector('h1')
    assert page.inner_text('h1') == 'Hello World'

@pytest.mark.e2e
def test_calculator_add(page, fastapi_server):
    page.goto('http://localhost:8000')
    page.fill('#a', '10')
    page.fill('#b', '5')
    page.click('button:text("Add")')
    # wait for the result to be updated by client-side JavaScript
    page.wait_for_selector('#result:has-text("Result:")', timeout=3000)
    assert page.inner_text('#result') == 'Result: 15'

@pytest.mark.e2e
def test_calculator_divide_by_zero(page, fastapi_server):
    page.goto('http://localhost:8000')
    page.fill('#a', '10')
    page.fill('#b', '0')
    page.click('button:text("Divide")')
    page.wait_for_selector('#result:has-text("Error:")', timeout=3000)
    assert page.inner_text('#result') == 'Error: Cannot divide by zero!'
