#The following is an example of movie data.


#{
#    "year" : 2013,
#   "title" : "Turn It Down, Or Else!",
#    "info" : {
#       "directors" : [
#            "Alice Smith",
#            "Bob Jones"
#        ],
#        "release_date" : "2013-01-18T00:00:00Z",
#        "rating" : 6.2,
#        "genres" : [
#            "Comedy",
#            "Drama"
#        ],
#        "image_url" : "http://ia.media-imdb.com/images/N/O9ERWAU7FS797AJ7LU8HN09AMUP908RLlo5JF90EWR7LJKQ7@@._V1_SX400_.jpg",
#        "plot" : "A rock band plays their music at high volumes, annoying the neighbors.",
#        "rank" : 11,        "running_time_secs" : 5215,
#        "actors" : [
#            "David Matthewman",
#            "Ann Thomas",
#            "Jonathan G. Neff"       ]
#    }
#}
#Download the Sample Data File
#In the Cloud9 terminal use the following command to download the moviedata.zip

#wget https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/samples/moviedata.zip
#Use the following command extract the data file (moviedata.json)

#unzip moviedata.zip

#Load the Sample Data in to the Movies Table
#After you download the sample data, you can run the following program to populate the Movies table.

#Copy the following program and paste it into a file named MoviesLoadData.py. change the region name us-west-2 to the same region as the Cloud9 instance.



import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Movies')

with open("moviedata.json") as json_file:
    movies = json.load(json_file, parse_float = decimal.Decimal)
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']

        print("Adding movie:", year, title)

        table.put_item(
           Item={
               'year': year,
               'title': title,
               'info': info,
            }
        )