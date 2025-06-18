import asyncio
import json
from pathway_config import get_client
from pathway.table import Table
from aiokafka import AIOKafkaConsumer
from your_embedding_lib import compute_embedding  # implement as needed

async def main():
    client = get_client()

    # Tables for raw events and vector index
    events = Table(client, name="events_stream")
    vectors = Table(client, name="doc_vectors")

    consumer = AIOKafkaConsumer(
        "events-topic",
        bootstrap_servers="localhost:9092",
        group_id="pathway-consumer"
    )
    await consumer.start()
    try:
        async for msg in consumer:
            payload = json.loads(msg.value)
            # Insert raw event
            events.insert(payload)

            # Compute embedding & upsert into vector index
            embedding = compute_embedding(payload["text"])
            vectors.upsert(id=payload["id"], vector=embedding, metadata=payload)
    finally:
        await consumer.stop()

if __name__ == "__main__":
    asyncio.run(main())