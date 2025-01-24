from pathlib import Path
import os

from .transcribe import cli

cudnn_path = Path(__file__).parents[1] / "/nvidia/cudnn/lib/"

os.environ["LD_LIBRARY_PATH"] = cudnn_path

cli()
