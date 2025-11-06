# src/callbacks.py

from langchain_core.callbacks import BaseCallbackHandler
import streamlit as st

class StreamlitCallbackHandler(BaseCallbackHandler):
    """
    A custom callback handler that writes agent activity to a Streamlit container.
    """
    def __init__(self, container):
        super().__init__()
        self.container = container
        self.thinking_message = None

    def on_agent_action(self, action, **kwargs) -> None:
        """
        Called when an agent is about to perform an action.
        """
        # Create a new "thinking" message
        self.thinking_message = self.container.info(f"🤔 Thinking...")

        # Append the thought process to the message
        self.thinking_message.info(f"🤔 Thinking...\n\n```text\n{action.log}\n```")
        
    def on_tool_start(self, serialized, input_str, **kwargs):
        """
        Called when a tool is about to be used.
        """
        # Update the "thinking" message to show the tool is being used
        if self.thinking_message:
            self.thinking_message.info(f"...using tool **{serialized['name']}** with input: `{input_str}`")

    def on_tool_end(self, output, **kwargs):
        """
        Called when a tool has finished running.
        """
        # Clear the "thinking" message
        if self.thinking_message:
            self.thinking_message.empty()
            self.thinking_message = None
        
        # Display the tool's output
        self.container.success(f"Tool finished with output:\n\n```text\n{output}\n```")

    def on_task_end(self, output, **kwargs):
        """
        Called when a task has finished.
        """
        # Display the final output of the task
        self.container.success(f"✅ Task completed!\n\n**Final Output:**\n{output.raw_output}")