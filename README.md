# ChatGPTBulkQuestions
A script that takes a list of questions and exports a csv with Questions and Answer from ChatGPT

## How to Use the ChatGPT bulk content script
1. **Create a prompt to replace in the "prompt" string variable.**
    - Go to [ChatGPT](https://chatgpt.com/) and create a prompt that will work for your content needs when you insert any topic from your list in the sentence like a madlib.
    - You will use this prompt and leave a variable where the topic goes.
      - **Example:** *Give me a list of 20 places with descriptions to visit in* [city]*. Don't be conversational.
    - Tell ChatGPT not to be "conversational", so you don't get things like "Sure, I can do that ..." in your answers
    - You can also tell ChatGPT to format the answer in html, if thats helpful for you.
2. **Create a list of topics you want content for in a csv**
     - For this example, we used a list of cities and asked chatgpt for adivce on things to visit. Get creative!
