import launch

if not launch.is_installed("huggingface_hub"):
    launch.run_pip("install huggingface-hub==0.11.1", "requirements for Push to Hugging Face extension")
