curl -X DELETE "localhost:9200/songs"
curl -X PUT "http://localhost:9200/songs?pretty" -H "Content-Type: application/json" -d @mapping.json
python loader.py
