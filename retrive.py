from pydantic import BaseModel
from openai import OpenAI
import json
import re


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",  # Ensure you replace this with your actual API key
)

class TamilResponse(BaseModel): 
    records: list

def get_tamil_data(equation: str, number_of_records: int) -> TamilResponse:
    # Using a more structured prompt to get clean JSON
    prompt = """Generate {n} Tamil language question-answer pairs in the following JSON format:
[
    {{
        "question": "தமிழ் கேள்வி",
        "answer": "பதில்",
        "context": "சூழல்"
    }}
]
Only respond with the JSON array, no additional text."""

    response = client.completions.create(
        model="gpt-4",  # Make sure to use a supported model
        prompt=prompt.format(n=number_of_records),
        max_tokens=100000000,  # Increased token limit for more data
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Get the response text
    data = response.choices[0].text.strip()
    
    try:
        # Try to parse the entire response as JSON first
        parsed_data = json.loads(data)
    except json.JSONDecodeError:
        # If that fails, try to extract JSON using regex
        json_match = re.search(r'\[.*?\]', data, re.DOTALL)
        if not json_match:
            print("Error: No JSON data found in the response.")
            return TamilResponse(records=[])
        
        try:
            parsed_data = json.loads(json_match.group(0))
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
            return TamilResponse(records=[])

    # Ensure the data is in the desired format
    records = [
        {
            "question": item.get("question", ""),
            "answer": item.get("answer", ""),
            "context": item.get("context", "")
        }
        for item in parsed_data[:number_of_records]
    ]
    
    # Print the records
    print("Retrieved records:")
    for record in records:
        print(record)
    
    return TamilResponse(records=records)


# Example usage
number_of_records = int(input("Enter the number of records you want: "))
response = get_tamil_data("Provide the required data in Tamil.", number_of_records)

# Save response to a local JSON file
with open('tamil_data.json', 'w', encoding='utf-8') as f:
    json.dump(response.records, f, ensure_ascii=False, indent=4)

print(f"Saved {len(response.records)} records in tamil_data.json")