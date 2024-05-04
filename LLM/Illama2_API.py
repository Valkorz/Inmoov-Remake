import os 
import replicate
os.environ["REPLICATE_API_TOKEN"] = "r8_BA8ZZg3EIH1VdJHR92xvwW13bBXJbEv2lPAH7" #Update the tokken, cause the new LLAMA 3 version
prompt_input = "Talk about the Inmoov project."
pre_prompt = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."


for event in replicate.stream(
    "meta/llama-2-70b-chat",
    input={
        "debug": False,
        "top_p": 1,
        "prompt": prompt_input,
        "temperature": 0.5,
        "system_prompt": pre_prompt,
        "max_new_tokens": 500,
        "min_new_tokens": -1,
        "prompt_template": "[INST] <<SYS>>\n{system_prompt}\n<</SYS>>\n\n{prompt} [/INST]",
        "repetition_penalty": 1.15
    },
):
    
    print(str(event), end="")
    #This will be a function that return the ai response
