from datasets.builders.base_dataset_builder import BaseDatasetBuilder
from datasets.datasets.image_text_pair_datasets import ImageTextPairDataset

from common.registry import registry


@registry.register_builder("vg_caption")
class VGCaptionBuilder(BaseDatasetBuilder):
    train_dataset_cls = ImageTextPairDataset

    vis_urls = {
        "images": {
            "train": [
                "https://cs.stanford.edu/people/rak248/VG_100K_2/images.zip",
                "https://cs.stanford.edu/people/rak248/VG_100K_2/images2.zip",
            ]
        }
    }

    def __init__(self, cfg):
        super().__init__(cfg)

    @classmethod
    def default_config_path(cls):
        return "configs/datasets/vg/defaults_caption.yaml"
