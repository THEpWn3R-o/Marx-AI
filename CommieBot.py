import openai
import os
import time
here = os.path.dirname(os.path.abspath(__file__))

def openfile(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        return f.read()
apikey = os.path.join(here, 'api-key.txt')
openai.api_key = openfile(apikey) # API key is stored in a file called api-key.txt


def gpt3_completion(prompt, engine='text-davinci-003', temp=0.8, top_p=1.0, tokens=256, freq_pen=0.0, pres_pen=0.0, stop=['Student:', 'Marx:']):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop)
    text = response['choices'][0]['text'].strip()
    return text

if __name__ == "__main__":
    conversation = list()

    while True:
        user_query = input("Student: ")
        conversation.append("Student: %s" % user_query)
        text_block = '\n'.join(conversation)
        persona = os.path.join(here, 'persona-isms/MarxPersona')
        prompt = openfile(persona).replace("<<block>>", text_block)
        prompt = prompt +'\nMarx:'
        response = gpt3_completion(prompt)
        print('Marx:', response)
        conversation.append("Marx: %s" % response)
        if user_query.lower() == 'goodbye marx!':
            exit(0)
        else:
            pass