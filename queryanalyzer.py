def get_data_from_query(tokenized_query):
    yearsData = [str(i) for i in range(1990,2011)]
    yearsDataFromQuery = []
    lyricistDataFromQuery = []
    lyricists = ["வைரமுத்து", "பழனி பாரதி", "வாலி", "பா.விஜய்", "தாமரை", "நா.முத்துக்குமார்", "அகத்தியன்", "அறிவுமதி"]
    if(len(tokenized_query) >= 2):
        for value in tokenized_query:
            if value in yearsData:
                yearsDataFromQuery.append(value)
            elif value in lyricists:
                lyricistDataFromQuery.append(value)
    return (yearsDataFromQuery,lyricistDataFromQuery)
