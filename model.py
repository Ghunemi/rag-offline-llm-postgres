from llama_cpp import Llama

class LocalLLM:
    def __init__(self, model_path: str):
        self.model = Llama(
            model_path=model_path,
            n_ctx=4096,
            n_threads=8,
            n_gpu_layers=20,
            verbose=False
        )

    def __call__(self, prompt: str, max_tokens=256, stop=None) -> str:
        output = self.model(prompt, max_tokens=max_tokens, stop=stop or ["\n\n"])
        return output["choices"][0]["text"].strip()