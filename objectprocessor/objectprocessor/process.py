"""Extract the data about the person from the CSV file."""

from typing import List, Text

import csv

from objectprocessor import person

# Sample of the data set:

# Mrs. Natalie Lee,Bolivia,036-126-0340x0094,"Engineer, building services",david82@example.org
# Michael Anderson,Honduras,(627)610-9166,Writer,ryan23@example.org
# Cindy Burns,Dominican Republic,(102)481-3875,"Pharmacist, hospital",rtorres@example.org
# Jason Bailey,Falkland Islands (Malvinas),+1-552-912-2326,Leisure centre manager,daniel51@example.com
# Andrew Johnson,Portugal,733-554-3949,"Engineer, site",michael94@example.com
# Carol Poole,Isle of Man,365.529.7270,Pensions consultant,piercebrenda@example.com


def extract_person_data(data: str) -> List[person.Person]:
    """Extract a specified data column from the provided textual contents."""
    # create an empty list of the data
    person_list = []
    # note that the data file:
    # --> contains five columns
    # --> each of which contains textual data with a different meaning
    #  refer to the file called input/people.txt to learn more about
    # the format of the comma separated value (CSV) file that we must parse;
    # iterate through each line of the file and extract all relevant details
    # use the csv.reader to accomplish the task of parsing the CSV file
    for line in csv.reader(
      data.splitlines(),
      quotechar='"',
      delimiter=",",
      quoting=csv.QUOTE_ALL,
      skipinitialspace=True,
    ):
        # extract each of the attributes about a person from the line variable
        # construct a new instance of the Person class that contains all
        # of the attributes that were extracted from the CSV file
        person_object = person.Person(
          line[0], 
          line[1],
          line[2],
          line[3],
          line[4]
        )
        # append the current instance of the person class to the data_list variable
        person_list.append(person_object)
    # return the list of all of the specified column
    return person_list


def write_person_data(file_name: str, person_data: List[person.Person]) -> None:
    """Write the person data stored in a list to the specified file."""
    # create an empty list that will store the person data as a list of strings
    converted_person_data = []
    # iterate through every person inside of the person_data list
    for person in converted_person_data:
      # create a list out of this person where each of the person's
      # attributes are stored inside of an index in the list
      person_list = []
      person_list.append(str(person.name))
      person_list.append(str(person.country))
      person_list.append(str(person.phone_number))
      person_list.append(str(person.job))
      person_list.append(str(person.email))
      # append this converted person list to the list called converted_person_data
      converted_person_data.append(person_list)
      # use the csv.writer approach and the writerows function to write out
      # the list of lists of strings that contain all of the person data
      with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(converted_person_data)


def find_matching_people(
    attribute: str, match: str, person_data: List[person.Person]
) -> List[person.Person]:
    """Find people who have matching data for a specified attribute."""
    # create an empty list of people who have an attribute matching the search term in match
    matching_person_list = []
    # iterate through all of the people in the person_data list
    for person in person_data:
      if is_matching_person(attribute, match, person):
      # the current person has an attribute that contains the search term in match
      # add the current person to the matching_person_list        
        matching_person_list.append(person)
    # return the matching_person_list
    return matching_person_list


def is_matching_person(
    attribute: str, match: str, search_person: person.Person
) -> bool:
    """Determine if the person's specified attribute contains the search term in match."""
    # the attribute for matching is name
      # return True if the provided search term is in the match
      # variable appears inside of the specified attribute
    # the attribute for matching is country
      # return True if the provided search term is in the match
      # variable appears inside of the specified attribute
    # the attribute for matching is phone number
      # return True if the provided search term is in the match
      # variable appears inside of the specified attribute
    # the attribute for matching is job
      # return True if the provided search term is in the match
      # variable appears inside of the specified attribute
    # the attribute for matching is email
      # return True if the provided search term is in the match
      # variable appears inside of the specified attribute
    # return False if none of the conditions are matching
    if attribute == "name":
      if match in search_person.name:
        return True
      else:
        return False
    elif attribute == "country":
      if match in search_person.country:
        return True
      else: 
        return False
    elif attribute == "phone_number":
      if match in search_person.phone_number:
        return True
      else:
        return False
    elif attribute == "job":
      if match in search_person.job:
        return True
      else:
        return False
    elif attribute == "email":
      if match in search_person.email:
        return True
      else:
        return False

