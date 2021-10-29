# Object Processing

## Evelyn Griffith

## Program Output

### Use two fenced code blocks to provide output from two different runs of `objectprocessor` with two different inputs

TODO: Provide the complete command-line for your use of the `objectprocessor` program

#### Provide the command the output for the first run of the `objectprocessor`

TODO: Provide your own example of a command and the output that it produces

#### Provide the command the output for the second run of the `objectprocessor`

TODO: Provide your own example of a command and the output that it produces

## Source Code

### Describe in detail how the provided source code works

Provide a description of each line in the following source code

```
person_index = create_constants(
    "person", Name=0, Country=1, Phone_Number=2, Job=3, Email=4
)
```

This portion of the code is telling the computer to assign all of the attributes to a number so that they can be called on numerically within later source code. An example would be here:

```
       person_object = person.Person(
          line[0], 
          line[1],
          line[2],
          line[3],
          line[4]
        )
```

In the code above, the lines are calling upon Name, Country, Phone_Number, Job, and Email respectively becauase they are using person.Person. In doing this they are actually going into the person.py file and calling on the variable "Person" which can then be used to link those attributes to a number which can then be used like an index.

### Describe in detail how the provided source code works:

Provide a description of each line in the following source code

```
person_attribute = create_constants(
    "person",
    Name="name",
    Country="country",
    Phone_Number="phone_number",
    Job="job",
    Email="email",
)
```

This section of code is, first, creating a variable called "person_attribute". Then it is creating constants under that attribute which links the name, country, phone number, job, and email of each person in the txt file to a str value that can then be used to reference those sets of data which have now been set apart from each other and distinguished based on data type (meaning if its a phone number, job, country, name, or email).

### Describe in detail how the provided source code works

Provide a description of each line in the following source code

```
def __init__(
    self, name: str, country: str, phone_number: str, job: str, email: str
) -> None:
    """Define the constructor for a person."""
    self.name = name
    self.country = country
    self.phone_number = phone_number
    self.job = job
    self.email = email
```

This function, in a nut shell, is defining constructors. Basically what it is doing is first using a function definition to define the inputs and outputs of this function which are the variable "name", "country", "phone_number", "job", and "email" (all of which are strings). The function also has another variable input called self which doesnt chave a type definition in the beginning function definition. The function then states that the output of this function should be None. This is because this function doesn't really need to produce an output it just needs to define the constructors for a person. The function will then go into the self.name sections of the function which is really the meat and potatoes as for why the function exists. This will essentially give each of the already existing people a way to distinguish their own personal data fromt the rest of the group data. This self." " is a way for the Person Class to reference individual data as opposed to group sets of data.

### Describe in detail how the provided source code works

TODO: Provide a description of each line in the following source code

```
def __repr__(self) -> str:
    """Return a textual representation of the person."""
      return f"{self.name} is a {self.job} who lives in {self.country}. You can call this person at {self.phone_number} and email them {self.email}."
```

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet.

## Professional Development

### What are the benefits and drawbacks of object-oriented programming in Python?

TODO: Provide a one-paragraph response that answers this question in your own words.

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

### What was the greatest challenge that you faced when completing this assignment?

TODO: Provide a one-paragraph response that answers this question in your own words.
TODO: Provide a response to this question that is different from any previous answers.

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

### Leveraging your response to the previous question, how did you overcome the challenge?

TODO: Provide a one-paragraph response that answers this question in your own words.
TODO: Provide a response to this question that is different from any previous answers.

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
