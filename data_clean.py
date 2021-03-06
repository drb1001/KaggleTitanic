import pandas as pd

trainset_path = "original_data/train.csv"
testset_path = "original_data/test.csv"

trainset = pd.read_csv(trainset_path)
testset = pd.read_csv(testset_path)

cleantrain = trainset
cleantest = testset

dummies = pd.get_dummies(cleantrain.Sex)

print dummies
# df = pd.concat( [df, pd.get_dummies(df['Embarked']).rename(columns=lambda x: 'Embarked_' + str(x))], axis=1)









cleantrain.to_csv("cleaned_data/train_cleaned.csv", index=False, float_format='%.f')
cleantest.to_csv("cleaned_data/test_cleaned.csv", index=False, float_format='%.f')







# train_csv = csv.reader(open('train.csv', 'rb'))
# header = train_csv.next()
# train_data=[]
# for row in train_csv:
#     train_data.append(row)
# train_data = np.array(train_data)

# print train_data
# print train_data[0]

# train_data[0::,1].astype(np.int)
# # The size() function counts how many elements are in
# # in the array and sum() (as you would expects) sums up
# # the elements in the array.

# # number_passengers = np.size(data[0::,1].astype(np.float))
# # number_survived = np.sum(data[0::,1].astype(np.float))
# # proportion_survivors = number_survived / number_passengers


# print train_data
# print train_data[0]



# test_csv = csv.reader(open('test.csv', 'rb'))
# header = test_csv.next()

# prediction_file = open("genderbasedmodel.csv", "wb")
# prediction_file_object = csv.writer(prediction_file)

# prediction_file_object.writerow(["PassengerId", "Survived"])

# for row in test_csv:
#     if row[3] == 'female':
#         prediction_file_object.writerow([row[0],'1'])
#     else:
#         prediction_file_object.writerow([row[0],'0'])
# test_csv.close()
# prediction_file.close()
