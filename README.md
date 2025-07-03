# TestCraft || crafting test based on UI

This project is an AI-driven prototype that:
1. Scrapes and analyzes website elements
2. Generates test cases using GenAI
3. Generates corresponding Selenium test scripts

## Requirements

- Python 3.8+
- Chrome browser
- ChromeDriver (compatible with your Chrome version)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/jkthunder279/AI-ML-Intern-Task-Assignment.git
cd AI-ML-Intern-Task-Assignment
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```



## Usage

Run each script individually

#### Task 1: Web Scraping & UI Element Extraction
```bash
python web_scraper.py
```

#### Task 2: Test Case Generation
```bash
python test_case.py --input elements.json --output test_cases.xlsx --model HuggingFaceH4/zephyr-7b-alpha --num_tests 5
```

#### Task 3: Selenium Script Generation
```bash
python selenium.py
```



## File Structure

- `web_scraper.py`: Script for Task 1 - Extracts UI elements
- `test_case.py`: Script for Task 2 - Generates test cases
- `selenium.py`: Script for Task 3 - Generates Selenium scripts
- `elements.json`: Output from Task 1 - Extracted UI elements
- `test_cases.xlsx`: Output from Task 2 - Generated test cases
- `test_scripts.xlsx`: Output from Task 3 - Generated Selenium scripts
- `requirements.txt`: Project dependencies

## Approach & Methodology

### Task 1: Web Scraping
- Used BeautifulSoup for efficient HTML parsing
- Extracted four types of UI elements: buttons, links, inputs, and forms
- Saved structured data in JSON format

### Task 2: Test Case Generation
- Used GenAI (huggingface HuggingFaceH4/zephyr-7b-alpha model) to analyze UI elements
- Generated meaningful test cases based on identified elements
- Focused on key user journeys and typical interactions
- Structured test cases with ID, scenario, steps, and expected results

### Task 3: Selenium Script Generation
- Converted test cases into executable Selenium scripts
- Used GenAI to write Python code that implements each test case
- Added proper error handling and assertions
- Formatted scripts for easy integration into test frameworks

## Challenges & Solutions

- **AI Response Parsing**: Implemented robust parsing logic to handle variations in AI output format
- **Model Availability**: Added fallback mechanisms to ensure the system works even if the AI model is unavailable
- **Script Reliability**: Generated scripts with proper waits and error handling to improve test stability

## Improvements

- **Multi-page Scraping**: Extend the scraper to follow links and analyze multiple pages
- **Test Prioritization**: Add logic to prioritize critical user journeys
- **Execution Framework**: Add a test runner to execute the generated scripts


