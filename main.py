import os
from langchain_community.llms import DeepInfra

auth_token="MXJ7lgLgrdxGnSy9g6lI03Hjy7o8jfRx"
os.environ["DEEPINFRA_API_TOKEN"] = auth_token

llm = DeepInfra(model_id="mistralai/Mixtral-8x7B-Instruct-v0.1")
llm.model_kwargs = {
    "temperature": 0.5,
    "repetition_penalty": 1.2,
    "max_new_tokens": 250,
    "top_p": 0.9,
}

print(llm("who let the dogs out?"))

