# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

    
# for county in counties_dict:
#     print(counties_dict[county])

# for county, voters in counties_dict.items():
#     print(county, voters)


# for key, value in counties_dict.items():
#     print(str(key) + "county has " + str(value) + "registered voters.")

#list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
                {"county":"Denver", "registered_voters": 463353}, 
                {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

# for i in range(len(voting_data)):
#     print(voting_data[i])

# for i in voting_data:
#     print(i)

# for i in voting_data:
#     for value in i.values():
#         print(value)

# #only print registered_voters from each dictionary
# for county_dict in voting_data:
#      print(county_dict['registered_voters'])

## only print county from each dictionary
# for county_dict in voting_data:
#     print(county_dict['county'])

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# # f'{value:{width},.{precision}}'
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
# print(message_to_candidate)

# for key, value in counties_dict.items():
#     print(f"{key} county has {value:,} registered voters.")

#only print registered_voters from each dictionary

# for i in voting_data:
#      print(i['registered_voters'])
# for i in voting_data:     
#     print(i['county'])
