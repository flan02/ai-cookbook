# This AI tool allows us to retrieve some info about a youtube video. We only have to copy the video's link and our AI tool will search the video and will create a recap about what it is about

from SimplerLLM.language.llm import LLM, LLMProvider
from SimplerLLM.tools.generic_loader import load_content

llm_instance = LLM.create(provider=LLMProvider.OPENAI, model_name="gpt-4o")

url = "https://www.youtube.com/watch?v=FukaIPVpmnA" # This var will contain the desired video to be analysed

content = load_content(url).content

summarize_prompt = f"generate a bullet point summary for the following: {content}"

generated_text = llm_instance.generate_response(prompt=summarize_prompt)

print(generate_text)
                                                                      
