# Notes

- https://conda-forge.org/packages/
- https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-file-manually
- https://github.com/Zulko/moviepy
- https://github.com/SYSTRAN/faster-whisper
- https://github.com/jiaaro/pydub
- https://github.com/Vaibhavs10/insanely-fast-whisper:
  - https://github.com/Vaibhavs10/insanely-fast-whisper/blob/f8bd18f43caf37cfd9b13cedc247e91c26184010/src/insanely_fast_whisper/cli.py#L130
- https://pytorch.org/docs/stable/generated/torch.mps.empty_cache.html
- https://huggingface.co/docs/transformers/main/en/installation#install-with-conda
- https://www.the-odd-dataguy.com/2024/01/31/podcast-whisper/
- https://ai.meta.com/blog/wav2vec-20-learning-the-structure-of-speech-from-raw-audio/
- https://github.com/huggingface/transformers/releases
- https://huggingface.co/docs/transformers/en/tasks/asr
- https://huggingface.co/tasks/automatic-speech-recognition:
  - Automatic Speech Recognition (ASR) or Speech to Text (STT)
- https://huggingface.co/openai/whisper-base
- https://huggingface.co/openai/whisper-large-v3
- https://huggingface.co/docs/transformers/main_classes/pipelines#transformers.AutomaticSpeechRecognitionPipeline
- https://huggingface.co/docs/transformers/v4.40.2/en/main_classes/pipelines#transformers.Pipeline
- https://huggingface.co/blog/asr-chunking
- https://huggingface.co/docs/transformers/en/main_classes/text_generation
- https://huggingface.co/docs/transformers/model_doc/whisper#transformers.WhisperModel
- https://jupyterlab-realtime-collaboration.readthedocs.io/en/latest/configuration.html:
  - "There is an experimental feature that is currently only supported by the [Jupyverse](https://github.com/jupyter-server/jupyverse) server (not yet with [jupyter-server](https://github.com/jupyter-server/jupyter_server), see the [issue #900](https://github.com/jupyter-server/jupyter_server/issues/900)): server-side execution. With this, running notebook code cells is not done in the frontend through the low-level kernel protocol over WebSocket API, but through a high-level REST API. Communication with the kernel is then delegated to the server, and cell outputs are populated in the notebook shared document. The frontend gets these outputs changes and shows them live. What this means is that the notebook state can be recovered even if the frontend disconnects, because cell outputs are not populated frontend-side but server-side."
- https://pypi.org/project/omegaconf/
- https://omegaconf.readthedocs.io/en/2.3_branch/usage.html#from-a-yaml-file
- https://stackoverflow.com/questions/5214578/print-string-to-text-file

## Commands

```bash
conda env remove --name asr-scripts
```

```bash
conda deactivate && conda env remove --name asr-scripts
```

```bash
conda deactivate && conda env remove --name asr-scripts && conda env create -f environment.yml && conda activate asr-scripts
```
