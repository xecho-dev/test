result = chat_model.invoke(messages)

parser = StrOutputParser()
#使用parser处理model返回的结果
response = parser.invoke(result)
print(type(response))
print(response)
