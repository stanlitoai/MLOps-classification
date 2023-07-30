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