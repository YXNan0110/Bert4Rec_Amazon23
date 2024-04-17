import pandas as pd
from .ex_base import AbstractDataset


class DigitalMusicDataset(AbstractDataset):
    @classmethod
    def code(cls):
        return 'Digital_Music'

    @classmethod
    def url(cls):
        pass

    @classmethod
    def zip_file_content_is_folder(cls):
        pass

    @classmethod
    def all_raw_file_names(cls):
        return []

    def load_ratings_df(self):
        """
        从本地文件加载评分数据，并返回DataFrame。

        :return: 包含评分数据的DataFrame。
        """
        file_path = './Data/Digital_Music/Digital_Music_train.csv'
        df = pd.read_csv(file_path)
        columns_to_load = ['user_id', 'parent_asin', 'rating', 'timestamp']
        df = pd.read_csv(file_path, usecols=columns_to_load)
        return df

