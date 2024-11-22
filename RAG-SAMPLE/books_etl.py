import os
from dotenv import load_dotenv

from unstructured_ingest.v2.pipeline.pipeline import Pipeline
from unstructured_ingest.v2.interfaces import ProcessorConfig
from unstructured_ingest.v2.processes.connectors.local import (
    LocalIndexerConfig,
    LocalDownloaderConfig,
    LocalConnectionConfig,
)
from unstructured_ingest.v2.processes.connectors.mongodb import (
    MongoDBConnectionConfig,
    MongoDBUploadStagerConfig,
    MongoDBUploaderConfig,
    MongoDBAccessConfig
)

from unstructured_ingest.v2.processes.partitioner import PartitionerConfig
from unstructured_ingest.v2.processes.chunker import ChunkerConfig
from unstructured_ingest.v2.processes.embedder import EmbedderConfig

if __name__ == "__main__":
    load_dotenv()
    uri = "mongodb+srv://newmaharshihello:RCBFOtJ0Xaffon9a@clusterrag.c26rv.mongodb.net/?retryWrites=true&w=majority&appName=ClusterRAG"
    Pipeline.from_configs(
        context=ProcessorConfig(
            verbose=True,
            tqdm=True,
            num_processes=20,
        ),

        indexer_config=LocalIndexerConfig(input_path="books/",
                                          recursive=False),
        downloader_config=LocalDownloaderConfig(),
        source_connection_config=LocalConnectionConfig(),

        partitioner_config=PartitionerConfig(
            partition_by_api=True,
            api_key=os.getenv("UNSTRUCTURED_API_KEY"),
            partition_endpoint=os.getenv("UNSTRUCTURED_URL"),
            strategy="fast"
        ),

        chunker_config=ChunkerConfig(
            chunking_strategy="by_title",
            chunk_max_characters=512,
            chunk_multipage_sections=True,
            chunk_combine_text_under_n_chars=250,
        ),

        embedder_config=EmbedderConfig(
            embedding_provider="huggingface",
            embedding_model_name="hs-hf/jina-embeddings-v3-distilled",
        ),

        destination_connection_config=MongoDBConnectionConfig(
            access_config=MongoDBAccessConfig(uri=uri),
            collection="unstructured-demo",
            database="books",
        ),
        stager_config=MongoDBUploadStagerConfig(),
        uploader_config=MongoDBUploaderConfig(batch_size=10)
    ).run()