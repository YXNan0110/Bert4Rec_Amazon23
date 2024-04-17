from .ml_1m import ML1MDataset
from .ml_20m import ML20MDataset
from .All_Beauty import AllBeautyDataset
from .Digital_Music import DigitalMusicDataset
from .Video_Games import VideoGamesDataset

DATASETS = {
    ML1MDataset.code(): ML1MDataset,
    ML20MDataset.code(): ML20MDataset,
    AllBeautyDataset.code(): AllBeautyDataset,
    DigitalMusicDataset.code(): DigitalMusicDataset,
    VideoGamesDataset.code(): VideoGamesDataset
}


def dataset_factory(args):
    dataset = DATASETS[args.dataset_code]
    return dataset(args)
