# importing the needed libraries
import pandas as pd
import datetime

# finding the avergae rating of every user based on the rating they gave    // Function i
def finding_user_average_rating(data):

    # splitting the data based on the data they carry to 3 different lsits
    users_list = data[0]
    movies_list = data[1]
    ratings_list = data[2]

    # sorting the lists based on users_list
    users_list,movies_list,ratings_list=[list(v) for v in zip(*sorted(zip(users_list,movies_list,ratings_list)))]

    # users_avg_rat: contains 2 items: userId and his average of ratingss
    users_avg_rat = []

    # number of unique users 
    num_users = len(pd.unique(df['userId']))

    # line of data we are currently on
    line=0
    # the user's id we examine
    user_id=1

    # while there are users
    while line<len(users_list):

        # number of ratings
        num_of_rat=0;
        # total rating of all movies they have rated
        total_rat=0;
        # while we are on the same user
        while users_list[line]==user_id:
            # adding 1 to the counter
            num_of_rat = num_of_rat+1
            # adding the rating to the total_rat
            total_rat = total_rat + ratings_list[line]
            # getting to the next data 
            line = line+1
            if line==len(users_list):
                break

        # if there are more than 0 ratings
        if num_of_rat!=0:
            # get the 3 first decimal digits of the average rating
            result = round(total_rat/num_of_rat,3)
            # append the user's id and their average rating
            users_avg_rat.append([user_id,result])
        else:
            # if user has 0 ratings
            users_avg_rat.append([user_id,0])
            
        # getting the next user's id
        user_id = user_id+1

    # returning users with their average rating
    return users_avg_rat


# returns the average rating of the given user
def find_user_avg(aUser,users_avg_rat):

    # initializing variables
    user_avg=0
    line=0
    # going through the lines of the list users_avg_rat
    # while the user is not the wanted, we go on the next line
    while users_avg_rat[line][0]!=aUser:
        line = line+1

    # getting and returning the user's average rating
    user_avg = users_avg_rat[line][1]
    return user_avg


# WHERE THE PROGRAM STARTS

# the time the program starts
now = datetime.datetime.now()
print ("*** Starting date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S\n"))

# reading the data from a csv file
df = pd.read_csv("filtered_data.csv")
print("Opening file: filtered_data.csv\n")

# the length of the csv file (total lines of info)
df_len=len(df)
print("The document file's length is:",df_len,"\n")

# splitting the data into training and testing data
ratio = 0.9
total_rows = df.shape[0]
train_size = int(total_rows*ratio)
print("The training set's length is:",train_size,"\n")
train_set = df[0:train_size]
test_set = df[train_size:]

# getting the wanted data from columns 0-2 from the training set
data = []
data.append(train_set.iloc[:,0])
data.append(train_set.iloc[:,1])
data.append(train_set.iloc[:,2])

# finding out for each user their average rating of movies they saw
users_avg_rating = finding_user_average_rating(data)

# list with the transformed rating for each movie based on which user saw that
new_movies_rat = []

# for each rating
line=0
for rating in data[2]:
    # find which user wrote the rating and get his average rating
    avg_rat = find_user_avg(data[0][line],users_avg_rating)
    # calculate the new rating of the movie based on the user
    new_rating = round(rating-avg_rat,3)
    # append the new rating to the list
    new_movies_rat.append(new_rating)
    # get the next data
    line = line+1

# writing the final data to a new csv file
dictionary = {'userId':data[0], 'movieId':data[1],'rating':new_movies_rat}
new_df=pd.DataFrame(dictionary)
new_df.to_csv('new_ratings_data.csv',index=False)
print("The new ratings have been calculated. There is a new file called: new_ratings_data.csv")

# the time the program finishes
now = datetime.datetime.now()
print ("\n*** Finishing date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S\n"))
