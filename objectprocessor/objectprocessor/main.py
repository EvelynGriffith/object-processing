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
    text = ""
    # iterate through each of the people in the person_list and
    # add all of their textual details to a string; making sure to
    # preface each entry with a "-" and add a newline
    # return the list of generated text for each person
    for per in person_list:
        text += f"\n- {per}"
    return text

    


@cli.command()
def main(
    search_term: str = typer.Option(...),
    attribute: str = typer.Option(...),
    input_file: Path = typer.Option(...),
    output_file: Path = typer.Option(...),
):
    """Input data about a person and then analyze and save it."""

    with open(input_file, "r") as f:
        extracted_data = process.extract_person_data(f.read())
    # display the details about the matching people to the console
    # make sure to use the prepare_person_list_for_display function for creating a suitable display
    # save the details about the matching people to the file system in the specified output directory
    # extracted_data = process.extract_person_data(search_term)
    matching_data = process.find_matching_people(
        attribute, search_term, extracted_data
    )
    display_data = prepare_person_list_for_display(matching_data)

    process.write_person_data(str(output_file), matching_data)

    console.print(
        ":abacus: Reading in the data from the specified file input/people.txt"
    )
    console.print()
    console.print(
        ":rocket: Parsing the data file and transforming it into people objects"
    )
    console.print()
    console.print(
        f":detective: Searching for the people with an email that matches the search term {search_term}"
    )
    console.print()
    console.print(":Sparkles: Here are the matching people:")
    console.print(f"{display_data}")
    console.print()
    console.print(
        ":Sparkles: Saving the matching people to the file output/people.txt"
    )
