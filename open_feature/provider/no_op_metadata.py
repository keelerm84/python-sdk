from dataclasses import dataclass

from open_feature.provider.metadata import Metadata


@dataclass
class NoOpMetadata(Metadata):
    name: str = "No-op Provider"
    is_test_class: bool = True
