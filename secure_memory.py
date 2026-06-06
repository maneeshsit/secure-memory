import tenseal as ts
import numpy as np
import time
from sentence_transformers import SentenceTransformer


class SecureMemoryStore:

    def __init__(self):

        self.context = ts.context(
            ts.SCHEME_TYPE.CKKS,
            poly_modulus_degree=8192,
            coeff_mod_bit_sizes=[60, 40, 40, 60]
        )

        self.context.global_scale = 2**40
        self.context.generate_galois_keys()

        self.memories = []

        self.embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def create_embedding(self, text):

        embedding = self.embedding_model.encode(text)

        return embedding.tolist()

    def encrypt_embedding(self, embedding):

        return ts.ckks_vector(
            self.context,
            embedding
        )

    def add_memory(self, text):

        embedding = self.create_embedding(text)

        encrypted_embedding = self.encrypt_embedding(
            embedding
        )

        self.memories.append(
            {
                "text": text,
                "embedding": encrypted_embedding
            }
        )

    def search(self, query):

        query_embedding = self.create_embedding(query)

        encrypted_query = self.encrypt_embedding(
            query_embedding
        )

        results = []

        for memory in self.memories:

            score = encrypted_query.dot(
                memory["embedding"]
            )

            decrypted_score = score.decrypt()[0]

            results.append(
                (
                    memory["text"],
                    decrypted_score
                )
            )

        results.sort(
            key=lambda x: x[1],
            reverse=True
        )

        return results