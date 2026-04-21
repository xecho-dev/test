def process_chat_response(messages):
    result = chat_model.invoke(messages)
    parser = StrOutputParser()
    response = parser.invoke(result)
    return response

response = process_chat_response(messages)
print(type(response))
print(response)