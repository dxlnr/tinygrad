from dataclasses import dataclass, field
from typing import Tuple

DATASET_SIZE = 168


@dataclass
class Conf:
    data_dir: str = "./extra/dataset/kits19/data"
    log_dir: str = ""
    save_ckpt_path: str = ""
    load_ckpt_path: str = ""
    val_split: float = 0.1

    epochs: int = 20
    quality_threshold: float = 0.908
    ga_steps: int = 1
    warmup_step: int = 4
    batch_size: int = 2
    layout: str = "NCDHW"
    # input_shape: Tuple[int, int, int] = (128, 128, 128)
    # val_input_shape: Tuple[int, int, int] = (128, 128, 128)
    input_shape: Tuple[int, int, int] = (64,64,64)
    val_input_shape: Tuple[int, int, int] = (64,64,64)
    seed: int = 0
    num_workers: int = 8
    exec_mode: str = "train"

    benchmark: bool = False
    amp: bool = False
    optimizer: str = "sgd"
    lr: float = 0.01 # 1e-3
    init_lr: float = 1e-4
    lr_warmup_epochs: int = 1
    lr_decay_epochs: int = field(default_factory=lambda: [])
    lr_decay_factor: float = 0.1
    momentum: float = 0.9
    weight_decay: float = 0.0
    eval_every: int = 10
    start_eval_at: int = 10
    verbose: bool = True
    normalization: str = "instancenorm"
    activation: str = "relu"

    oversampling: float = 0.4
