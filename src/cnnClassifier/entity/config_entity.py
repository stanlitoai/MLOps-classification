"""Configuration for entity."""

from dataclasses import dataclass, field

from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    """Configuration for data ingestion."""
    root_dir: Path
    """Path to the directory containing the data."""
    source_URL: str
    """URL of the data source."""
    local_data_file: Path
    """Path to the local file containing the data."""
    unzip_dir: Path
    """Path to the directory containing the unzipped data."""



@dataclass(frozen=True)
class PrepareBaseModelConfig:
    """Configuration for data ingestion."""
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weight: str
    params_classes: int