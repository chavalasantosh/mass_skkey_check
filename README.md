# Stripe API Key Validator

This Python script provides a simple and effective way to validate Stripe API keys. By prompting the user to input their Stripe API keys and then attempting to retrieve Stripe account details, the script can quickly determine whether each key is valid or invalid.

## Features

- **User Input for API Keys**: The script allows users to input multiple Stripe API keys one by one.
- **Validation of Keys**: It checks each key by attempting to connect to the Stripe API and retrieve account details.
- **Immediate Feedback**: For each key, the script provides immediate feedback on whether the key is valid or invalid, including any error messages from the Stripe API for invalid keys.

## Prerequisites

Before running the script, ensure you have Python installed on your system. Additionally, you need the Stripe Python library, which can be installed via pip:

```bash
pip install stripe
