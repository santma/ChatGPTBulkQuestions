import os
from openai import OpenAI
import csv


# Define your OpenAI API Key
client = OpenAI(
    # This is the default and can be omitted
    api_key='[Your API KEY]',
)

# File to read the store names from
input_filename = 'topics.csv'

# File to save the HTML responses to
output_filename = 'about_topics.csv'

def ask_gpt3(topic):
    try:
        response = client.chat.completions.create(
            messages=[
                {
                "role":"user",
                "content":f"tell me five things about {topic}. put answer in html ordered list. Include links to sources. Do not be conversational"
                }
            ],
            model="gpt-4",
            # don't be conversational
#return response.choices[0].message["content"]
        )
        print(topic)
        answer = response.choices[0].message.content
        print(answer)
        return(answer)
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

with open(input_filename, 'r', newline='', encoding='utf-8') as input_csvfile, \
     open(output_filename, 'w', newline='', encoding='utf-8') as output_csvfile:

    # CSV reader for input file
    reader = csv.DictReader(input_csvfile)

    # Define the fieldnames for the output CSV
    fieldnames = ['topic', 'about_topic']
    writer = csv.DictWriter(output_csvfile, fieldnames=fieldnames)

    # Write the header for the output CSV
    writer.writeheader()

    # Loop through each store in the input CSV and get the HTML snippet from GPT-3
    for row in reader:
        topic = row['topic']
        about_topic = ask_gpt3(topic)
        writer.writerow({'topic': topic, 'about_topic': about_topic})

print(f'HTML snippets successfully written to {output_filename}')
