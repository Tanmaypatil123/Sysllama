from sysllama import SysllamaConfig
from sysllama.prompts.sys_info import SysInfoPrompt
from sysllama.prompts.main_prompt import Mainprompt
from sysllama import OllamaLLM
from sysllama.prompts.operation_check import OperationCheckPrompt
from sysllama import OllamaAssistant

# # obj = Mainprompt(prompt="how to go to the root directory ?")
# obj = OperationCheckPrompt(prompt="How to go to the root directory ?")
# llm = OllamaLLM(
#     model="orca-mini",
# )

# print(obj.template())
# data = llm.generate(prompt=obj.template())
# print(data.json()["response"])

# # print(obj.template())
# print(llm)
config = SysllamaConfig(model="orca-mini")
assistant = OllamaAssistant()
print(assistant)
print(assistant.get_config)
