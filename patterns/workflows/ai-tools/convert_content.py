from SimplerLLM.language.llm import LLM, LLMProvider
from SimplerLLM.tools.generic_loader import load_content

llm_instance = LLM.create(provider=LLMProvider.OPENAI, model_name="gpt-4o")

url = "https://www.youtube.com/watch?v=FukaIPVpmnA" # This var will contain the desired video to be analysed

content = load_content(url).content

convert_to_tweet_prompt = f"""Extract the key info from the following post, and convert to an engaging 280 chars tweet. post content : {content}"""

generated_text = llm_instance.generate_response(prompt=convert_to_tweet_prompt)

print(generate_text)
