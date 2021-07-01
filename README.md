# Train the Best Sentence Embedding Model Ever with 1B Training Pairs.

Contribution to the project [Flax/JAX Projects](https://discuss.huggingface.co/t/train-the-best-sentence-embedding-model-ever-with-1b-training-pairs/7354)

## Dataset

The iteration on the dataset are crucial for this task as the characteristics of the batch will directly impact on the model performances.
**Increasing the batch size** will increase performances as well [Qu and all., 2021](https://www.aclweb.org/anthology/2021.naacl-main.466.pdf).
Each batch should also be somehow **center on one specific sub-domain** or dataset such that samples could not be discriminated from their general "domain" only.
However batches should **also mix different sub-domains in some proportion** such that the mapping of distinct domain do not overlap.

I implemented basic function to download the various corpora and load them in python. Download time should be approximatively 20 minutes for all datasets currently listed in the "Available Datasets" sheet. 
I also implemented a basic lazy dataloader. For now the dataloader takes a single `jsonl.gz` file as input and iterates over it to retrieve sample.
The dataloader is implemented in `PyTorch` for now and support multi-threading. It uses a pointer mechanism to load a sample one by one in memory.

Please refere to the demonstration notebook: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AntoineSimoulin/1B_sentence_embeddings/blob/master/dataset.ipynb)

You can download the data using the python script:

```bash
python download_data.py --dataset_list=datasets_list.tsv --data_path=PATH_TO_STORE_DATASETS
```