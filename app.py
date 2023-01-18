from flask import Flask, request, render_template
from elasticsearch import Elasticsearch
from flask_cors import CORS

es = Elasticsearch(hosts=["http://127.0.0.1:9200"])
print(f"Connected to ElasticSearch cluster `{es.info().body['cluster_name']}`")

app = Flask(__name__)
CORS(app)

MAX_SIZE = 100

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search_autocomplete():
    query = request.args["q"].lower()
    # start_year = request.args["start_year"]
    end_year = request.args["end_year"]
    synonym_enable = request.args["synonym_enable"]
    max_results = request.args["max_results"]
    print(query+" "+end_year+" "+synonym_enable+" "+max_results)
    # date = request.args["date"]
    tokens = query.split(" ")

    clauses = [
        {
            "span_multi": {
                "match": {"fuzzy": {"name": {"value": i, "fuzziness": "AUTO"}}}
            }
        }
        for i in tokens
    ]

    payload = {
        "bool": {
            "must": [{"span_near": {"clauses": clauses, "slop": 0, "in_order": False}}]
        }
    }

    resp = es.search(index="songs", query=payload, size=MAX_SIZE)
    print(resp)
    return [result['_source']['name'] for result in resp['hits']['hits']]


@app.route("/summary")
def get_summary():

    payload = {
        "aggs": {
            "product": {
            "terms": {
                "field": "singers"
            }
        }
    }
  }
    

    resp = es.search(index="songs", body=payload, size=MAX_SIZE)
    print(resp)
    return [{result['key']:result['doc_count']} for result in resp['aggregations']['product']['buckets']]    


if __name__ == "__main__":
    app.run(debug=True)
