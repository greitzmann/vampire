from environments.random_search import RandomSearch
from environments.datasets import DATASETS

HATESPEECH_CLASSIFIER = {
        "LAZY_DATASET_READER": 0,
        "CUDA_DEVICE": 0,
        "EVALUATE_ON_TEST": 1,
        "NUM_EPOCHS": 50,
        "SEED": 158361,
        "SEQUENCE_LENGTH": 400,
        "TRAIN_PATH": "s3://suching-dev/final-datasets/hatespeech/train_pretokenized.jsonl",
        "DEV_PATH": "s3://suching-dev/final-datasets/hatespeech/dev_pretokenized.jsonl",
        "TEST_PATH": "s3://suching-dev/final-datasets/hatespeech/test_pretokenized.jsonl",
        "THROTTLE": 10000,
        "USE_SPACY_TOKENIZER": 0,
        "FREEZE_EMBEDDINGS": ["VAMPIRE"],
        "EMBEDDINGS": ["VAMPIRE", "RANDOM"],
        "ENCODER": "AVERAGE",
        "EMBEDDING_DROPOUT": 0.5,
        "LEARNING_RATE": 0.004,
        "DROPOUT": 0.5,
        "VAMPIRE_DIRECTORY": "saved_vampires/hatespeech_vampire 94",
        "BATCH_SIZE": 32,
        "NUM_ENCODER_LAYERS": 1,
        "NUM_OUTPUT_LAYERS": 2, 
        "MAX_FILTER_SIZE": RandomSearch.random_integer(3, 6),
        "NUM_FILTERS": RandomSearch.random_integer(64, 512),
        "HIDDEN_SIZE": RandomSearch.random_integer(64, 512),
        "AGGREGATIONS": RandomSearch.random_subset("maxpool", "meanpool", "attention", "final_state"),
        "MAX_CHARACTER_FILTER_SIZE": RandomSearch.random_integer(3, 6),
        "NUM_CHARACTER_FILTERS": RandomSearch.random_integer(16, 64),
        "CHARACTER_HIDDEN_SIZE": RandomSearch.random_integer(16, 128),
        "CHARACTER_EMBEDDING_DIM": RandomSearch.random_integer(16, 64),
        "CHARACTER_ENCODER": RandomSearch.random_choice("LSTM", "CNN", "AVERAGE"),
        "NUM_CHARACTER_ENCODER_LAYERS": RandomSearch.random_choice(1, 2),
}

YAHOO_CLASSIFIER = {
        "LAZY_DATASET_READER": 0,
        "CUDA_DEVICE": 0,
        "EVALUATE_ON_TEST": 1,
        "NUM_EPOCHS": 50,
        "SEED": 158361,
        "SEQUENCE_LENGTH": 400,
        "TRAIN_PATH": "s3://suching-dev/final-datasets/yahoo/train_pretokenized.jsonl",
        "DEV_PATH": "s3://suching-dev/final-datasets/yahoo/dev_pretokenized.jsonl",
        "TEST_PATH": "s3://suching-dev/final-datasets/yahoo/test_pretokenized.jsonl",
        "THROTTLE": 10000,
        "USE_SPACY_TOKENIZER": 0,
        "FREEZE_EMBEDDINGS": ["VAMPIRE"],
        "EMBEDDINGS": ["VAMPIRE", "RANDOM"],
        "ENCODER": "AVERAGE",
        "EMBEDDING_DROPOUT": 0.5,
        "LEARNING_RATE": 0.004,
        "DROPOUT": 0.5,
        "VAMPIRE_DIRECTORY": "saved_vampires/yahoo_vampire 121",
        "BATCH_SIZE": 32,
        "NUM_ENCODER_LAYERS": 1,
        "NUM_OUTPUT_LAYERS": 2, 
        "MAX_FILTER_SIZE": RandomSearch.random_integer(3, 6),
        "NUM_FILTERS": RandomSearch.random_integer(64, 512),
        "HIDDEN_SIZE": RandomSearch.random_integer(64, 512),
        "AGGREGATIONS": RandomSearch.random_subset("maxpool", "meanpool", "attention", "final_state"),
        "MAX_CHARACTER_FILTER_SIZE": RandomSearch.random_integer(3, 6),
        "NUM_CHARACTER_FILTERS": RandomSearch.random_integer(16, 64),
        "CHARACTER_HIDDEN_SIZE": RandomSearch.random_integer(16, 128),
        "CHARACTER_EMBEDDING_DIM": RandomSearch.random_integer(16, 64),
        "CHARACTER_ENCODER": RandomSearch.random_choice("LSTM", "CNN", "AVERAGE"),
        "NUM_CHARACTER_ENCODER_LAYERS": RandomSearch.random_choice(1, 2),
}

IMDB_CLASSIFIER = {
        "LAZY_DATASET_READER": 0,
        "CUDA_DEVICE": 0,
        "EVALUATE_ON_TEST": 1,
        "NUM_EPOCHS": 50,
        "SEED": 158361,
        "SEQUENCE_LENGTH": 400,
        "TRAIN_PATH": "s3://suching-dev/final-datasets/imdb/train_pretokenized.jsonl",
        "DEV_PATH": "s3://suching-dev/final-datasets/imdb/dev_pretokenized.jsonl",
        "TEST_PATH": "s3://suching-dev/final-datasets/imdb/test_pretokenized.jsonl",
        "THROTTLE": 10000,
        "USE_SPACY_TOKENIZER": 0,
        "FREEZE_EMBEDDINGS": ["VAMPIRE"],
        "EMBEDDINGS": ["VAMPIRE", "RANDOM"],
        "ENCODER": "AVERAGE",
        "EMBEDDING_DROPOUT": 0.5,
        "LEARNING_RATE": 0.004,
        "DROPOUT": 0.5,
        "VAMPIRE_DIRECTORY": "saved_vampires/imdb_vampire 72",
        "BATCH_SIZE": 32,
        "NUM_ENCODER_LAYERS": 1,
        "NUM_OUTPUT_LAYERS": 2, 
        "MAX_FILTER_SIZE": RandomSearch.random_integer(3, 6),
        "NUM_FILTERS": RandomSearch.random_integer(64, 512),
        "HIDDEN_SIZE": RandomSearch.random_integer(64, 512),
        "AGGREGATIONS": RandomSearch.random_subset("maxpool", "meanpool", "attention", "final_state"),
        "MAX_CHARACTER_FILTER_SIZE": RandomSearch.random_integer(3, 6),
        "NUM_CHARACTER_FILTERS": RandomSearch.random_integer(16, 64),
        "CHARACTER_HIDDEN_SIZE": RandomSearch.random_integer(16, 128),
        "CHARACTER_EMBEDDING_DIM": RandomSearch.random_integer(16, 64),
        "CHARACTER_ENCODER": RandomSearch.random_choice("LSTM", "CNN", "AVERAGE"),
        "NUM_CHARACTER_ENCODER_LAYERS": RandomSearch.random_choice(1, 2),
}


AG_CLASSIFIER = {
        "LAZY_DATASET_READER": 0,
        "CUDA_DEVICE": 0,
        "EVALUATE_ON_TEST": 1,
        "NUM_EPOCHS": 50,
        "SEED": 158361,
        "SEQUENCE_LENGTH": 400,
        "TRAIN_PATH": "s3://suching-dev/final-datasets/ag-news/train_pretokenized.jsonl",
        "DEV_PATH": "s3://suching-dev/final-datasets/ag-news/dev_pretokenized.jsonl",
        "TEST_PATH": "s3://suching-dev/final-datasets/ag-news/test_pretokenized.jsonl",
        "THROTTLE": 10000,
        "USE_SPACY_TOKENIZER": 0,
        "FREEZE_EMBEDDINGS": ["VAMPIRE"],
        "EMBEDDINGS": ["VAMPIRE", "RANDOM"],
        "ENCODER": "AVERAGE",
        "EMBEDDING_DROPOUT": 0.5,
        "LEARNING_RATE": 0.004,
        "DROPOUT": 0.5,
        "VAMPIRE_DIRECTORY": "saved_vampires/ag_vampire 107",
        "BATCH_SIZE": 32,
        "NUM_ENCODER_LAYERS": 1,
        "NUM_OUTPUT_LAYERS": 2, 
        "MAX_FILTER_SIZE": RandomSearch.random_integer(3, 6),
        "NUM_FILTERS": RandomSearch.random_integer(64, 512),
        "HIDDEN_SIZE": RandomSearch.random_integer(64, 512),
        "AGGREGATIONS": RandomSearch.random_subset("maxpool", "meanpool", "attention", "final_state"),
        "MAX_CHARACTER_FILTER_SIZE": RandomSearch.random_integer(3, 6),
        "NUM_CHARACTER_FILTERS": RandomSearch.random_integer(16, 64),
        "CHARACTER_HIDDEN_SIZE": RandomSearch.random_integer(16, 128),
        "CHARACTER_EMBEDDING_DIM": RandomSearch.random_integer(16, 64),
        "CHARACTER_ENCODER": RandomSearch.random_choice("LSTM", "CNN", "AVERAGE"),
        "NUM_CHARACTER_ENCODER_LAYERS": RandomSearch.random_choice(1, 2),
}


VAMPIRE = {
        "LAZY_DATASET_READER": 0,
        "KL_ANNEALING": "sigmoid",
        "SIGMOID_WEIGHT_1": 0.6855069165689476,
        "SIGMOID_WEIGHT_2": 93.21758569698095,
        "LINEAR_SCALING": 31.588121391460245,
        "VAE_HIDDEN_DIM":  105,
        "ADDITIONAL_UNLABELED_DATA_PATH": None,
        "TRAIN_PATH": "/home/suching/vampire/train+unlabeled_pretokenized.jsonl",
        "DEV_PATH": DATASETS['imdb']['dev'],
        "VOCABULARY_DIRECTORY": "/home/suching/vampire/vocab/",
        "REFERENCE_COUNTS": DATASETS['imdb']['reference_counts'],
        "REFERENCE_VOCAB": DATASETS['imdb']['reference_vocabulary'],
        "STOPWORDS_PATH": DATASETS['imdb']['stopword_path'],
        "NUM_ENCODER_LAYERS": 2,
        "ENCODER_ACTIVATION": "softplus",
        "MEAN_PROJECTION_ACTIVATION": "linear",
        "NUM_MEAN_PROJECTION_LAYERS": 1,
        "LOG_VAR_PROJECTION_ACTIVATION": "linear",
        "NUM_LOG_VAR_PROJECTION_LAYERS": 1,
        "DECODER_HIDDEN_DIM":  406,
        "DECODER_ACTIVATION": "tanh",
        "DECODER_NUM_LAYERS": 2,
        "SEED": 58195,
        "Z_DROPOUT": 0.2,
        "LEARNING_RATE": 0.001,
        "NUM_GPU": 0,
        "THROTTLE": None,
        "TRACK_NPMI": True,
        "ADD_ELMO": 0,
        "CUDA_DEVICE": 0,
        "USE_SPACY_TOKENIZER": 0,
        "UPDATE_BACKGROUND_FREQUENCY": 0,
        "VOCAB_SIZE": 10000,
        "APPLY_BATCHNORM": 1,
        "APPLY_BATCHNORM_1": 0,
        "BATCH_SIZE": 64,
        "VALIDATION_METRIC": "+npmi"
}



VAMPIRE_FAST = {
        "LAZY_DATASET_READER": 0,
        "KL_ANNEALING": "sigmoid",
        "SIGMOID_WEIGHT_1": 0.25,
        "SIGMOID_WEIGHT_2": 15,
        "LINEAR_SCALING": 1000,
        "VAE_HIDDEN_DIM":  64,
        "ADDITIONAL_UNLABELED_DATA_PATH": None,
        "TRAIN_PATH": "/home/suching/vampire/data/ag/train.npz",
        "DEV_PATH": "/home/suching/vampire/data/ag/dev.npz",
        "REFERENCE_COUNTS": "s3://suching-dev/final-datasets/ag-news/valid_npmi_reference/train.npz",
        "REFERENCE_VOCAB": "s3://suching-dev/final-datasets/ag-news/valid_npmi_reference/train.vocab.json",
        "VOCABULARY_DIRECTORY": "/home/suching/vampire/data/ag/vocab/",
        "STOPWORDS_PATH": "s3://suching-dev/stopwords/snowball_stopwords.txt",
        "NUM_ENCODER_LAYERS": 2,
        "ENCODER_ACTIVATION": "softplus",
        "MEAN_PROJECTION_ACTIVATION": "linear",
        "NUM_MEAN_PROJECTION_LAYERS": 1,
        "LOG_VAR_PROJECTION_ACTIVATION": "linear",
        "NUM_LOG_VAR_PROJECTION_LAYERS": 1,
        "SEED": 234,
        "Z_DROPOUT": 0.2,
        "LEARNING_RATE": 0.001,
        "NUM_GPU": 0,
        "THROTTLE": None,
        "TRACK_NPMI": True,
        "ADD_ELMO": 0,
        "CUDA_DEVICE": 0,
        "USE_SPACY_TOKENIZER": 0,
        "UPDATE_BACKGROUND_FREQUENCY": 0,
        "VOCAB_SIZE": 30000,
        "APPLY_BATCHNORM": 1,
        "APPLY_BATCHNORM_1": 0,
        "BATCH_SIZE": 64,
        "VALIDATION_METRIC": "-nll"
}


ENVIRONMENTS = {
        'VAMPIRE': VAMPIRE,
        'VAMPIRE_FAST': VAMPIRE_FAST,
        "HATESPEECH_CLASSIFIER": HATESPEECH_CLASSIFIER,
        "AG_CLASSIFIER": AG_CLASSIFIER,
        "YAHOO_CLASSIFIER": YAHOO_CLASSIFIER,
        "IMDB_CLASSIFIER": IMDB_CLASSIFIER
}






