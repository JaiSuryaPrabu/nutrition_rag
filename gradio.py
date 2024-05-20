# Importing gradio
import gradio as gr

# Getting user input
def input_text(user_input):
    return user_input

# Creating the Gradio interface
iface = gr.Interface(
    fn=input_text,
    inputs=gr.Textbox(lines=2, placeholder="Enter your text here..."),  # Input text field
    outputs=gr.Textbox(),  # Output text field
)

#Launching the application
iface.launch(share=True)

