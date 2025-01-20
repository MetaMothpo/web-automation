That's it! The tests will run automatically in sequence:
1. User Registration
2. User Login
3. Product Selection
4. Checkout
5. Payment

## Troubleshooting

If you get any errors:
1. Make sure Chrome browser is installed
2. Verify Python is installed: `python --version`
3. Make sure you installed requirements: `pip install -r requirements.txt`
4. Ensure you're in the project directory when running commands

## Test User
pytest tests/test_e2e_flow.py -v