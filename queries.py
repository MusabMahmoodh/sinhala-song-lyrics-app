def aggregations_query():
    payload = {
        "aggs": {
            "product": {
            "terms": {
                "field": "lyricist"
            }
        }
    }
  }
    return payload

def basic_search(query):
    q = {
        "query": {
            "query_string": {
                "query": query
            }
        }
    }
    return q


def search_with_field(query, field):
    q = {
        "query": {
            "match": {
                field: query
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
    return q


def search_with_field_filter_date(query, field,start_year,end_year):
    q =       {
            "query": {
                "bool": {
                "must": {
                    "match": {
                field: query
            }
                },
                "filter": {
                    "range": {
                    "year": {
                        "lte": str(end_year),
                        "gte": str(start_year)
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

    return q


def multi_match(query, fields=['title', 'song_lyrics'], operator='or'):
    q = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": fields,
                "operator": operator,
                "type": "best_fields"
            }
        }
    }
    return q