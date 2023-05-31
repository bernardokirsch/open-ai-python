import openai

openai.api_key = 'SUA-API-KEY'

def request(message):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"{message}"}
        ]
    )
    return completion.choices[0].message['content']

while True:
    print('---------------------------------PERGUNTA-------------------------------------')
    message = input('Você: ')
    print('---------------------------------RESPOSTA-------------------------------------')

    if message.lower() == 'adeus':
        print('ChatGPT: Até logo!')
        break

    response = request(message)

    print('ChatGPT:', response)
    print('')