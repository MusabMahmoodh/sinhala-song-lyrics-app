**Introduction**

This report details the implementation of a Tamil Song Metaphor application, which is designed to search and recommend Tamil songs based on the user's query. The application is built using the Elasticsearch engine, the Flask web framework, and various other libraries. The primary focus of this application is to provide an easy-to-use interface for searching Tamil songs and also to provide a summary of the search results. The application also includes features such as synonym search, date range filtering and maximum number of results.

The corpus used in this application contains 100 Tamil songs, with each song including metadata such as the song's title, lyrics, and other relevant information. To enhance the search functionality, the application uses custom analyzers that include stop word filters, synonym filters, and stemmers. The application also uses Elasticsearch's aggregation query to display a summary of the search results.

This report will provide a detailed overview of the application's architecture, development process, and functionality, as well as its potential future improvements.

**Implementation**

The implementation of this application involved several key steps. First, a corpus of 100 Tamil songs was compiled and processed to be used as the source of data for the search engine. Next, an Elasticsearch index was created and custom analyzers were added to the mapping in order to improve the search functionality, including stop word filters, synonym filters, and a stemmer.

A Flask server was then set up to handle the web application's backend functionality, including handling search queries, aggregations for viewing summary data, and field filters for date range searches. Search queries were created for basic searches, searches with synonyms, and searches with date range filters.

The frontend of the application was built using HTML, CSS and JavaScript, with a design that included a search bar, results displayed in a list format, and a loading icon while results were being fetched. A logo was also added above the search bar, and the overall design was consistent with a music theme. The user interface also includes a configuration section for users to input the date range and other values which are used to set as query params for search request.

Finally, the application was deployed on Github and the link is provided in the report. The report also provides details on the usage of libraries such as elasticsearch and flask, and the steps taken to improve the search functionality with the use of custom analyzers.


**Tools

Elasticsearch**: Elasticsearch is a search engine based on the Lucene library. It provides a distributed, multitenant-capable full-text search engine with an HTTP web interface and schema-free JSON documents. Elasticsearch is developed in Java and is released as open source under the terms of the Apache License.

**Kibana**: Kibana is an open-source data visualisation and exploration tool. It is used to search, view, and interact with data stored in Elasticsearch indices. Kibana provides a browser-based interface for creating, visualising, and Elasticsearch:

Elasticsearch is a search engine based on the Lucene library. It provides a distributed, multitenant-capable full-text search engine with an HTTP web interface and schema-free JSON documents. Elasticsearch is developed in Java and is released as open source under the terms of the Apache License.

**Flask**: Flask is a lightweight web framework for Python. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. Flask provides a simple and flexible way to create web applications and APIs, with support for routing, request handling, and template rendering.

**Flask**: Flask is a lightweight web framework for Python. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. Flask provides a simple and flexible way to create web applications and APIs, with support for routing, request handling, and template rendering.


**User Interface**
![](https://github.com/MusabMahmoodh/tamil-song-metophar-app/blob/master/Aspose.Words.4fb90d0a-d500-44a5-b13f-e7e1c943d006.001.png)

**Use Cases**

1. Users can query the metaphor and can retrieve the songs having that metaphor with its interpretation, source, and target domain.
1. Users can perform field-wise searches for all the features, including basic search, wildcard search, exact search, and multi-match search.
1. Users can filter the search results by date range, and enable/disable synonym matching.
1. Users can view the summary of the search results, including the top occurring metaphorical phrases, and their frequency of occurrence, by using aggregation queries in Elasticsearch.

**Techniques used in Designing, Indexing and Querying**

**Custom Analyzers**:

To improve the accuracy and relevance of search results, custom analyzers were created and added to the Elasticsearch configuration. The custom analyzers included:

**Tamil stemmers** - This was used to remove the inflectional suffixes from words to get the root form of the word. For example, "வளர்ந்து" would be stemmed to "வளர்"

**Tamil stopwords** - These are common words that are not useful for search and were removed from the indexed data. Examples include "உள்", "பது" and "ஆகிய"

**Tamil lemmatizer** - This was used to group together the inflected forms of a word so they can be analysed as a single term. For example, "மிகச்சிேந்ே" and "மிகசிேந்ே" would be lemmatized to "சிேந்ே". After applying these analyzers, the data was indexed and made available for searching.
