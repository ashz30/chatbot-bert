
from sentence_transformers import SentenceTransformer
import scipy.spatial

embedder = SentenceTransformer('bert-base-nli-mean-tokens')

def queryresponse(query, categories):

    corpus_embeddings = embedder.encode(categories)

    # Query sentences:
    queries = [query]
    query_embeddings = embedder.encode(queries)
    response = list()
    # Find the closest 5 sentences of the corpus for each query sentence based on cosine similarity
    closest_n = 5
    for query, query_embedding in zip(queries, query_embeddings):
        distances = scipy.spatial.distance.cdist([query_embedding], corpus_embeddings, "cosine")[0]

        results = zip(range(len(distances)), distances)
        results = sorted(results, key=lambda x: x[1])

        print("\n\n======================\n\n")
        print("Query:", query)
        print("\nTop 5 most similar sentences in corpus:")

        for idx, distance in results[0:closest_n]:
            print(categories[idx].strip(), "(Score: %.4f)" % (1 - distance))
            response.append({categories[idx].strip(): (1 - distance)})

    return response




