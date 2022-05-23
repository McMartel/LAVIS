from datasets.builders.base_dataset_builder import BaseDatasetBuilder

from common.registry import registry
from datasets.datasets.coco_vqa_datasets import COCOVQADataset, COCOVQAEvalDataset


@registry.register_builder("coco_vqa")
class COCOVQABuilder(BaseDatasetBuilder):
    train_dataset_cls = COCOVQADataset
    eval_dataset_cls = COCOVQAEvalDataset

    vis_urls = {
        "images": {
            "train": [
                "http://images.cocodataset.org/zips/train2014.zip",  # md5: 0da8c0bd3d6becc4dcb32757491aca88
                "http://images.cocodataset.org/zips/val2014.zip",  # md5: a3d79f5ed8d289b7a7554ce06a5782b3
            ],
            "test": "http://images.cocodataset.org/zips/test2015.zip",  # md5: 04127eef689ceac55e3a572c2c92f264
        }
    }

    def __init__(self, cfg):
        super().__init__(cfg)

    @classmethod
    def default_config_path(cls):
        return "configs/datasets/coco/defaults_vqa.yaml"
