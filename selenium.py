import json
import pandas as pd
import requests

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-alpha"
HEADERS = {"Authorization": "Bearer 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"}

df_test_cases = pd.read_excel("test_cases.xlsx")

def generate_selenium_script(test_case):
    # giving prompt
    prompt = f"""
    You are an expert in Python and Selenium. Generate a Selenium test script based on the following test case:

    **Test Case ID**: {test_case['Test Case ID']}
    **Test Scenario**: {test_case['Test Scenario']}
    **Steps to Execute**:
    {test_case['Steps to Execute']}

    The script should:
    - Use `selenium` with `webdriver.Chrome()`
    - Include necessary imports
    - Implement steps logically
    - Handle expected results using `assert`
    
    Output format:
    ```python
    <code here>
    ```
    **DO NOT return any extra text, only return a valid Python script.**
    """

    response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})

    try:
        raw_response = response.text

       
        script_start = raw_response.find("```python") + len("```python")
        script_end = raw_response.rfind("```")
        selenium_script = raw_response[script_start:script_end].strip()

        return selenium_script
    except Exception as e:
        print(f"Error generating script for {test_case['Test Case ID']}: {e}")
        return ""


df_test_cases["Python Selenium Code"] = df_test_cases.apply(generate_selenium_script, axis=1)


df_test_cases.to_excel("test_scripts.xlsx", index=False)

print("Selenium scripts successfully generated and saved to test_scripts.xlsx")
