from flask import Flask, request, render_template
from elasticsearch import Elasticsearch
from flask_cors import CORS

from queries import aggregations_query
from queries import search_with_field
from queries import search_with_field_filter_date
from queryanalyzer import get_data_from_query

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
    query = request.args["q"]
    start_year = request.args["start_year"]
    end_year = request.args["end_year"]
    synonym_enable = request.args["synonym_enable"]
    max_results = request.args["max_results"]
    lyricist = None;
    
    tokenized_query = query.split(" ")
    yearsDataFromQuery,lyricistDataFromQuery = get_data_from_query(tokenized_query)
    if len(yearsDataFromQuery) > 0:
        print("Years data from query: ", yearsDataFromQuery)
        end_year = max(yearsDataFromQuery)
        start_year = min(yearsDataFromQuery)
        print("Start year: ", start_year)
        print("End year: ", end_year)
    if len(lyricistDataFromQuery) > 0:
        lyricist = lyricistDataFromQuery[0]
      
        
    if(lyricist != None and start_year != "null" and end_year != "null"):
        payload = search_with_field_filter_date(lyricist, "lyricist",start_year,end_year)     
    elif(lyricist != None and start_year == "null" and end_year == "null"): 
        payload = search_with_field(lyricist, "lyricist")
    elif(synonym_enable == "true" and start_year != "null" or end_year != "null"):
        modified_start_year = start_year if start_year != "null" else 1989
        modified_end_year = end_year if end_year != "null" else 2011
        payload = {
            "query": {
                "bool": {
                "must": {
                    "multi_match": {
                    "query": "அஞ்சாதே",
                    "type": "most_fields",
                    "fields": [
                        "name",
				"metophar.stop_word_and_inflections_and_synonym"
                    ]
                    }
                },
                "filter": {
                    "range": {
                    "year": {
                        "lte": str(modified_end_year),
                        "gte": str(modified_start_year)
                    }
                    }
                }
                }
            },
            "highlight":{
                "fields":{
			"metophar.stop_word_and_inflections_and_synonym":{
				
			}
		},
                "pre_tags":"<u>",
                "post_tags":"</u>",
                "fragment_size":200
            }            
        }
    elif(synonym_enable == "false" and start_year != "null" or end_year != "null"):
        print("Here 4")
        modified_start_year = start_year if start_year != "null" else 1989
        modified_end_year = end_year if end_year != "null" else 2011
        payload = {
            "query": {
                "bool": {
                "must": {
                    "multi_match": {
                    "query": query,
                    "type": "most_fields",
                    "fields": [
                        "name",
				"metophar.stop_word_and_inflections_and_synonym"
                    ]
                    }
                },
                "filter": {
                    "range": {
                    "year": {
                        "lte": str(modified_end_year),
                        "gte": str(modified_start_year)
                    }
                    }
                }
                }
            },
            "highlight":{
                "fields":{
			"metophar.stop_word_and_inflections_and_synonym":{
				
			}
		},
                "pre_tags":"<u>",
                "post_tags":"</u>",
                "fragment_size":200
            }
        }   
    elif(synonym_enable == "true" and start_year == "null" and end_year == "null"):        payload = {
            "query": {
                "bool": {
                    "must":  {
                    "multi_match": {
                    "query": query,
                    "type": "most_fields",
                    "fields": [
                        "name",
				"metophar.stop_word_and_inflections_and_synonym"
                    ]
                    }
                }
                }
            },
            "highlight":{
                "fields":{
			"metophar.stop_word_and_inflections_and_synonym":{
				
			}
		},
                "pre_tags":"<u>",
                "post_tags":"</u>",
                "fragment_size":200
            }
        }
    else:
        payload = {
            "query": {
                "bool": {
                    "must": 
                         {
                    "multi_match": {
                    "query": query,
                    "type": "most_fields",
                    "fields": [
                        "name",
				"metophar.stop_word_and_inflections_and_synonym"
                    ]
                    }
                },
                    
                }
            },
            "highlight":{
                "fields":{
			"metophar.stop_word_and_inflections_and_synonym":{
				
			}
		},
                "pre_tags":"<u>",
                "post_tags":"</u>",
                "fragment_size":200
            }
        }
    print(payload)
    resp = es.search(index="songs", body=payload, size=MAX_SIZE)
    print(resp)
    return [result for result in resp['hits']['hits']]


@app.route("/summary")
def get_summary():

    payload = aggregations_query()
    

    resp = es.search(index="songs", body=payload, size=MAX_SIZE)
    print(resp)
    return [{result['key']:result['doc_count']} for result in resp['aggregations']['product']['buckets']]    


if __name__ == "__main__":
    app.run(debug=True)
