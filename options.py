from templates import set_template
from datasets import DATASETS
from dataloaders import DATALOADERS
from models import MODELS
from trainers import TRAINERS


class Config:
    mode = 'train'
    template = 'train_bert'
    test_model_path = None

    dataset_code = 'All_Beauty'
    min_rating = 4
    min_uc = 0
    min_sc = 0
    split = 'leave_one_out'
    dataset_split_seed = 98765
    eval_set_size = 500

    dataloader_code = 'bert'
    dataloader_random_seed = 0.0
    train_batch_size = 64
    val_batch_size = 64
    test_batch_size = 64

    train_negative_sampler_code = 'random'
    train_negative_sample_size = 100
    train_negative_sampling_seed = None
    test_negative_sampler_code = 'random'
    test_negative_sample_size = 100
    test_negative_sampling_seed = None

    trainer_code = 'bert'
    device = 'cpu'
    num_gpu = 1
    device_idx = '0'
    optimizer = 'Adam'
    lr = 0.001
    weight_decay = 0
    momentum = None
    decay_step = 15
    gamma = 0.1
    num_epochs = 50
    log_period_as_iter = 12800
    metric_ks = [10, 20, 50]
    best_metric = 'NDCG@10'

    find_best_beta = False
    total_anneal_steps = 2000
    anneal_cap = 0.2

    model_code = 'bert'
    model_init_seed = None
    bert_max_len = None
    bert_num_items = None
    bert_hidden_units = None
    bert_num_blocks = None
    bert_num_heads = None
    bert_dropout = None
    bert_mask_prob = None
    dae_num_items = None
    dae_num_hidden = 0
    dae_hidden_dim = 600
    dae_latent_dim = 200
    dae_dropout = 0.5
    vae_num_items = None
    vae_num_hidden = 0
    vae_hidden_dim = 600
    vae_latent_dim = 200
    vae_dropout = 0.5

    experiment_dir = 'experiments'
    experiment_description = 'test'


args = Config()
set_template(args)

