curl -X DELETE "localhost:9200/songs"
curl -X PUT "http://localhost:9200/songs?pretty" -H "Content-Type: application/json" -d @mapping.json
curl -XPUT "http://localhost:9200/_ingest/pipeline/splitter" -H "kbn-xsrf: reporting" -H "Content-Type: application/json" -d'
{
  "processors": [
    {
      "split": {
        "field": "singers",
        "separator": ","
      }
    },
    {
      "trim": {
        "field": "singers"
      }
    }
  ]
}'
curl -XPUT "http://localhost:9200/_ingest/pipeline/splitter" -H "kbn-xsrf: reporting" -H "Content-Type: application/json" -d'
{
  "processors": [
    {
      "split": {
        "field": "lyricist",
        "separator": ","
      }
    },
    {
      "trim": {
        "field": "lyricist"
      }
    }
  ]
}'
curl -XPOST "http://localhost:9200/songs/_update_by_query?pipeline=splitter" -H "kbn-xsrf: reporting"
python loader.py
