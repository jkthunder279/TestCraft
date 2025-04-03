
import os
import argparse
import json
import requests
import pandas as pd


API_KEY = "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"

def generate_test_cases(elements, model, num_tests):
    url = f"https://api-inference.huggingface.co/models/{model}"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    test_cases = []
    for _ in range(num_tests):
        
        payload = {"inputs": json.dumps(elements)}

        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 200:
            try:
                test_case = response.json()
                test_cases.append(test_case if isinstance(test_case, dict) else {"output": test_case})
            except json.JSONDecodeError:
                print("Error: Invalid JSON response")
        else:
            print("Error generating test cases:", response.text)

    return test_cases


def main():
    parser = argparse.ArgumentParser(description="Generate 3 to 5 meaningful test cases from elements.json")
    parser.add_argument('--input', required=True, help='Path to elements.json file')
    parser.add_argument('--output', required=True, help='Path to output Excel file')
    parser.add_argument('--model', required=True, help='Hugging Face model')
    parser.add_argument('--num_tests', type=int, required=True, help='Number of test cases')

    args = parser.parse_args()

    with open(args.input, 'r', encoding='utf-8') as f:
        elements = json.load(f)

    test_cases = generate_test_cases(elements, args.model, args.num_tests)

    df = pd.DataFrame(test_cases)
    df.to_excel(args.output, index=False)
    print(f"Exported to {args.output}")

if __name__ == "__main__":
    main()

