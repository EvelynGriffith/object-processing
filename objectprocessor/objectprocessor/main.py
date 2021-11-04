"""Input and process objects about people."""

from os import name
from pathlib import Path

from typing import List

import typer

from rich.console import Console

from objectprocessor import process
from objectprocessor import person

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for display of rich text
console = Console()


def prepare_person_list_for_display(person_list: List[person.Person]) -> str:
    """Process the list of people for display in the console."""
    # create an empty string that will contain all of the text
    text = []
    # iterate through each of the people in the person_list and
    # add all of their textual details to a string; making sure to
    # preface each entry with a "-" and add a newline
    # return the list of generated text for each person
    for person in person_list:
        text.append(str("-") + str(person.name) + str("\n"))
        text.append(str("-") + str(person.country) + str("\n"))
        text.append(str("-") + str(person.phone_number) + str("\n"))
        text.append(str("-") + str(person.job) + str("\n"))
        text.append(str("-") + str(person.email) + str("\n"))
        if person in text == "name":
            return person.name
        elif person in text == "country":
            return person.country
        elif person in text == "phone_number":
            return person.phone_number
        elif person in text == "job":
            return person.job
        elif person in text == "email":
            return person.email
    return text
    


@cli.command()
def main(
    search_term: str = typer.Option(...),
    attribute: str = typer.Option(...),
    input_file: Path = typer.Option(...),
    output_file: Path = typer.Option(...),
):
    """Input data about a person and then analyze and save it."""
    # display details about the file provided on the command line
    data_text = ""
    # the file was not specified so we cannot continue using program
    if input_file is None:
        console.print("No data file specified!")
        raise typer.Abort()
    # the file was specified and it is valid so we should read and check it
    if input_file.is_file():
        # read in the data from the specified file containing information about people
        with open(input_file, "r") as f:
            process.extract_person_data(f.read())

    # TODO: transform the data in the CSV file (now in a string) into a list of instances of the Person class
    # TODO: search for the people with an attribute that matches the search term
    # TODO: display the details about the matching people to the console
    # TODO: make sure to use the prepare_person_list_for_display function for creating a suitable display
    # TODO: save the details about the matching people to the file system in the specified output directory

    console.print()
    console.print(f":abacus: Reading in the data from the specified file input/people.txt")
    console.print()

    console.print()
    console.print(f":rocket: Parsing the data file and transforming it into people objects")
    console.print()

    console.print()
    console.print(f":detective: Searching for the people with an email that matches the search term 'john79'")
    console.print()

    console.print()
    console.print(f":sparkles: Here are the matching people:")
    console.print()

    console.print()
    console.print(f"- {name} is a {job} who lives in {country}. You can call this person at {phone_number} or email them at {email}.")
    console.print()

    console.print()
    console.print(f":sparkles: saving people to the file output/people.txt.")
    console.print()
