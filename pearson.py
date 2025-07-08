# importing the needed libraries
import pandas as pd
import datetime
import math

# counting the similarity between 2 movies with Pearson Similarity    // Function i
def count_similarity_between_2_movies(movie1,movie2,users,movies,ratings):
    
    #we have to find between the 2 movies, users who have rated them both

    movies_len = len(movies)

    # user ids who have watched the movie1 and movie2 respectivelly
    movie1_users = []
    movie2_users = []

    # find the users who have watched the movie1
    for i in range(0,movies_len):
        if movies[i]==movie1:
            movie1_users.append(users[i])

    # find the users who have watched the movie2
    for i in range(0,movies_len):
        if movies[i]==movie2:
            movie2_users.append(users[i])

    # the intersection of the lists movie1_users and movie2_users
    intersection_movies_users = set(movie1_users).intersection(movie2_users)
    intersection_movies_users = sorted(intersection_movies_users)

    # ratings of the common users for each movie
    rating_users_movie1 = []
    rating_users_movie2 = []

    # for every user who watched both movies
    for user_id in intersection_movies_users:

        # finding the movie1 rating for every user
        line=0
        flag = True
        while line<len(movies) and flag:
            if users[line]==user_id and movies[line]==movie1:
                rating_users_movie1.append(ratings[line])
                flag = False
            else:
                line=line+1

        # finding the movie2 rating for every user
        line=0
        flag = True
        while line<len(movies) and flag:
            if users[line]==user_id and movies[line]==movie2:
                rating_users_movie2.append(ratings[line])
                flag = False
            else:
                line=line+1
    
    # how many ratings are there
    length = len(rating_users_movie1)

    # calculating the numerator for the pearson similarity
    numerator=0 # αριθμητής
    for i in range(0,length):
        numerator = numerator + rating_users_movie1[i]*rating_users_movie2[i]

    # calculating the denominator for the pearson similarity
    denominator=0 # παρονομαστής
    first=0
    second=0
    for i in range(0,length):
        first = first + rating_users_movie1[i]*rating_users_movie1[i]
        second = second + rating_users_movie2[i]*rating_users_movie2[i]
    first = math.sqrt(first)
    second = math.sqrt(second)
    denominator = first + second

    # so that we have no problem with the denominator value
    if denominator!=0:
        pearson = numerator/denominator
    else:
        pearson = 0

    return pearson


# finding the length of the movies similarity between movies    // FUNCTION ii
def length_of_simil_list(length):

    total_length=0;
    for i in range(0,length):
        total_length = total_length+i
    
    return total_length


# finding the similarity between all the movies 2 by 2    // Function iii
def finding_similarity_all_movies(unique_movies,users,movies,ratings):

    # number of unique movies
    unique_movies_len = len(unique_movies)

    # total number of pearson similarities that must be found
    simil_list_length = length_of_simil_list(unique_movies_len)

    # number of pearson similarities that must be found
    print("Must be found:",simil_list_length,"\n")

    # list storing the similarity between 2 movies
    movies_similarity = [[-1 for columns in range(3)] for rows in range(simil_list_length)]

    line=0
    i=0
    while line<len(users) and i<simil_list_length:

        # to get every other movie
        j=i+1
        # for every other movie expect from the i one
        while j<unique_movies_len:

            # ids of the movie1 and movie2
            movie1=unique_movies[i]
            movie2=unique_movies[j]
            # appending the data to the list
            movies_similarity[line][0]=movie1
            movies_similarity[line][1]=movie2
            movies_similarity[line][2]=count_similarity_between_2_movies(movie1,movie2,users,movies,ratings)
            # getting to the next line
            line=line+1
            # getting the next movie
            j = j+1
        if line==simil_list_length:
            break
        
        # for printing purposes
        calc = j-i
        print("Just calculated:",calc)

        # next movie
        i=i+1

    return movies_similarity

# time the program starts
now = datetime.datetime.now()
print ("Starting date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S\n"))

# reading data from csv file
df = pd.read_csv("new_ratings_data.csv")
print("Opening file: new_ratings_data.csv\n")

# finding out the length of data (total lines of info)
df_len=len(df)
print("The document file's length is:",df_len,"\n")

# appending to lists different columns of the data 
users_list=df.iloc[:,0]
movies_list=df.iloc[:,1]
ratings_list=df.iloc[:,2]

# getting the unique number of movies in the whole csv file
n = len(pd.unique(df['movieId']))
print("Number of total movies:",n,"\n")

# list with the unique movie ids
unique_movie_ids = pd.unique(df['movieId'])

# calculating the pearson similarity between all the movies
pearson_similarities_betw_all_movies = finding_similarity_all_movies(unique_movie_ids,users_list,movies_list,ratings_list)

# for comfort to enter the data to csv file
movie1_ids = []
movie2_ids = []
pearson_similarities = []

# appending to files_name and filtered_files, each file name and file text respectivelly
for data in pearson_similarities_betw_all_movies:
    movie1_ids.append(data[0])
    movie2_ids.append(data[1])
    pearson_similarities.append(data[2])

# writing out the data on a new csv file
dictionary = {'movie1Id':movie1_ids,
              'movie2Id':movie2_ids,
              'pearson_similarity':pearson_similarities}
new_df=pd.DataFrame(dictionary)
new_df.to_csv('pearson_similarity_data.csv',index=False)
print("\nCalculating Pearson Similarity has ended. There is a new file called: pearson_similarity_data.csv\n")

# time the program finishes
now = datetime.datetime.now()
print ("\nFinishing date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
