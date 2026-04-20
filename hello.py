def process_chat_result(messages):
    result = chat_model.invoke(messages)
    parser = StrOutputParser()
    response = parser.invoke(result)
    print(type(response))
    print(response)

process_chat_result(messages)