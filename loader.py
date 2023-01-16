from elasticsearch import Elasticsearch

import csv

es = Elasticsearch(hosts=["http://127.0.0.1:9200"])

print(f"Connected to ElasticSearch cluster `{es.info().body['cluster_name']}`")

with open("./song_corpus.csv", "r") as f:
    reader = csv.reader(f)

    for i, line in enumerate(reader):        
        document = {
            "name": line[1],
            "Movie": line[2],
            "year": line[3],
            "lyricist": line[4],
            "singers": line[5],
            "metophar": line[6],
        }
        print(document["name"])
        es.index(index="songs", document=document)
