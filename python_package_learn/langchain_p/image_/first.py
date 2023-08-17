from steamship import Block, Steamship
import re
from IPython.display import Image
from langchain import OpenAI
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.tools import SteamshipImageGenerationTool

llm = OpenAI(temperature=0)
# AFD8DD6C-2DFF-4B70-B2A8-F39228AFD230
tools = [SteamshipImageGenerationTool(model_name="dall-e")]
mrkl = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)
output = mrkl.run("How would you visualize a parot playing soccer?")


def show_output(output):
    """Display the multi-modal output from the agent."""
    UUID_PATTERN = re.compile(
        r"([0-9A-Za-z]{8}-[0-9A-Za-z]{4}-[0-9A-Za-z]{4}-[0-9A-Za-z]{4}-[0-9A-Za-z]{12})"
    )

    outputs = UUID_PATTERN.split(output)
    outputs = [
        re.sub(r"^\W+", "", el) for el in outputs
    ]  # Clean trailing and leading non-word characters

    for output in outputs:
        maybe_block_id = UUID_PATTERN.search(output)
        if maybe_block_id:
            Image(Block.get(Steamship(), _id=maybe_block_id.group()).raw())
        else:
            print(output, end="\n\n")


show_output(output)
