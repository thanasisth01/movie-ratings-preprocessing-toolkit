# printing the needed libraries
import pandas as pd
import datetime

# printing the time the program starts
now = datetime.datetime.now()
print ("Starting date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S\n"))

# reading data from csv file
df = pd.read_csv("ratings.csv")
print("Opening file: ratings.csv\n")

# getting the length of the csv file (total lines of info)
df_len=len(df)
print("The document file's length is:",df_len,"\n")

# appending the data from its column to a list
data = []
data.append(df.iloc[:,0])
data.append(df.iloc[:,1])
data.append(df.iloc[:,2])



# ****** USERS WHO RATED MORE THAN OR EQUAL TO 5 MOVIES ******

# the number of total users
n = len(pd.unique(df['userId']))
print("Number of total users:",n)

# setting the data from column 0 to a list named users_list
users_list = data[0]
# length of list of users
users_list_len = len(users_list)

# list with user's id who have rated more than or equal to 5 movies
users_exceed5 = []

# variables for the next while to get through the data
# count of times the user appears in the data
count_user=0
# the users id
user_id=1
# to get through the data
count_lines=0

# while we go through the data, until the end of the 
while count_lines<users_list_len:

    # if the current user is the user with the wanted id
    if users_list[count_lines]==user_id:

        # get to the next line and add 1 to the current users count
        count_user = count_user+1
        count_lines = count_lines+1

    # if user has more than 5 ratings, append him to the list
    if count_user==5:
        # appending user 
        users_exceed5.append(user_id)
        if user_id==610:
            break
        # when we have collected more than 5 ratings, we skip the next lines
        # when the users is the same
        while users_list[count_lines]==user_id and count_lines<users_list_len:
            count_lines = count_lines+1
        user_id = user_id+1
        count_user=0

# printing the number of users who have more than 5 ratings
len_exceed5 = len(users_exceed5)
print("Users exceeding 5 or more ratings: ", len_exceed5,"\n")
        


# ****** MOVIES WHO HAVE BEEN RATED BY MORE THAN OR EQUAL TO 5 BY USERS ******

# getting all the movie info from the data to list with only them
movies_list = []
movies_list = data[1]

# how many ratings exist in the file
len_movie = len(movies_list)
print("Movies list length:",len_movie,"\n")

# number of movies
count = 0
  
# list of unique movie ids
movie_ids = []
  
# loop for counting the unique movie ids
for i in range(0, len(df['movieId'])):
    if df['movieId'][i] not in movie_ids: 
        movie_ids.append(df['movieId'][i])
        count = count+1

# movie_count: list with 2 columns, movieId and count of ratings for it
movie_count = [[0 for columns in range(2)] for rows in range(count)]

# initializing the movie_count list with the movie ids
for rows in range(count):
    movie_count[rows][0] = movie_ids[rows]

# counting how many ratings its movie has
for i in range(0,len_movie):
    myMovie = movies_list[i]
    myIndex = movie_ids.index(myMovie)
    movie_count[myIndex][1] = movie_count[myIndex][1] + 1

# final movies having more than 5 ratings
movies_exceed5 = []
for i in range(0,count):
    if movie_count[i][1]>=5:
        movies_exceed5.append(movie_count[i][0])

# printing the data we found
print("Number of total movies:", count)
print("Number of movies exceeding 5 user ratings:", len(movies_exceed5))
print(movies_exceed5)

# new lists to easily enter them to a new csv file
user_list2=[]
movie_list2=[]
rating_list2=[]

# getting from the data the info we need, so as to enter them
# in the lists user_list2, movie_list2, rating_list2
line=0
for movie in data[1]:
    if movie in movies_exceed5:
        user_list2.append(data[0][line])
        movie_list2.append(data[1][line])
        rating_list2.append(data[2][line])
    line=line+1

# sorting all the lists based on the movie_list2
movie_list2,user_list2,rating_list=[list(v) for v in zip(*sorted(zip(movie_list2,user_list2,rating_list2)))]

# writing out to a new csv file
dictionary = {'userId':user_list2, 'movieId':movie_list2,'rating':rating_list2}
new_df=pd.DataFrame(dictionary)
new_df.to_csv('filtered_data.csv',index=False)
print("Prefiltering has ended. There is a new file called: filtered_data.csv\n")

# printing the time the program finishes
now = datetime.datetime.now()
print ("Finishing date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S\n"))
