import requests
import json
import gradio as gr

url = 'http://localhost:11434/api/generate'

# To initialise the code

headers = {

    'Content-Type': 'application/json'
}

# below line will save the chat history

history = []


# To generate the response


def response_generate(prompt):
    history.append(prompt)
    fin_prompt = '\n'.join(history)
    data = {
        'model': 'Code_Prototype',
        'prompt': fin_prompt,
        'stream': False
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response = response.text
        data = json.loads(response)
        act_r = data['response']
        return act_r
    else:
        print('Error Message:', response.text)


# Developing Gradio Front End

interface = gr.Interface(
    fn=response_generate,
    inputs=gr.Textbox(lines=5, placeholder='I can solve any coding problem. Try me now!!'),
    outputs='text'
)
interface.launch(share=True)
