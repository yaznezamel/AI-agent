import os
from dotenv import load_dotenv
from openai import OpenAI
import json
import argparse


load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
parser = argparse.ArgumentParser(description="Chatbot")


def generate_content(client, messages):
    response = client.chat.completions.create(
    model="openrouter/free",
    messages= messages,
        )

    return response



def main():
    
    client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=api_key,
            )
        
    parser.add_argument("user_prompt", type=str , help="User prompt")
    parser.add_argument("--verbose" , action="store_true", help= "Enable verbose output")
    args = parser.parse_args()
        
    messages = [
        {"role": "user" , "content": args.user_prompt}
    ]

    response = generate_content(client,messages)

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print("Prompt tokens: " , response.usage.prompt_tokens)
        print("Response tokens: ", response.usage.completion_tokens)
    print(response.choices[0].message.content)
    

if __name__ == "__main__":
    main()
