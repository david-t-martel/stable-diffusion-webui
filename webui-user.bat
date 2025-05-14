@echo off

set PYTHON=
set GIT=
set VENV_DIR=
set COMMANDLINE_ARGS= --opt-channelslast
set TORCH_COMMAND=pip install torch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 --index-url https://download.pytorch.org/whl/cu121
set XFORMERS_PACKAGE=xformers==0.0.23.post1

set CUDA_VISIBLE_DEVICES=0
set PYTORCH_CUDA_ALLOC_CONF=garbage_collection_threshold:0.8,max_split_size_mb:512

call webui.bat
