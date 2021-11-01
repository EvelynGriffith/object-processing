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

### Describe in detail how the provided source code works.

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

This is creating the constructor. This function is actually a Class definition which designates that we will create a new data type. When designation of method __init__ (short for initialization) is the constructor, the first parameter in this code is always called self. What does self do in context of a constructor? Self refers to the new instance of the class that is about to be constructed. This makes init self refferential and allows us to use itself to modify its own state. The self.name etc. block of code is creating a new instance of the person class that is defining a data set for each individual. What is the purpose of None? None usually means "no return value", but in this instance it means that the constructor doesnt return something but it does construct something and return it back to the code. This function, in a nut shell, is creating/defining the constructor. The function will then go into the self.name sections of the function which is really the meat and potatoes as for why the function exists. This will essentially give each of the already existing people a way to distinguish their own personal data fromt the rest of the group data. This self." " is a way for the Person Class to reference individual data as opposed to group sets of data.

### Describe in detail how the provided source code works

Provide a description of each line in the following source code

```
def __repr__(self) -> str:
    """Return a textual representation of the person."""
      return f"{self.name} is a {self.job} who lives in {self.country}. You can call this person at {self.phone_number} and email them {self.email}."
```

The __repr__ method is designed to produce a textual representation of what our python class looks like in terms of its state.
It is supposed to print or display the state. Whereas the __init__ constructs the state. The purpose of this prints out a representation as a string and returns it. It uses an f string because it helps to retrieve the state of the object. We access the state using `self."whatever is here"` (which is the state of the object, also known as an attribute). We then display the state using the same f string we would normally use. This helps to refer to an object through self which is an implicit parameter to all of the methods. We can then access the state inside of an object by using self.email, self.job, etc.

## Professional Development

### What are the benefits and drawbacks of object-oriented programming in Python?

Object Oriented Programming means that you have to write a lot more code usually. However, it helps to make your code more disciplined and your system is slightly better in terms of the structuring of your code.

### What was the greatest challenge that you faced when completing this assignment?

TODO: Provide a one-paragraph response that answers this question in your own words.
TODO: Provide a response to this question that is different from any previous answers.

The biggest challenge I faced when I was completing this project was completing the source code in the process.py file, and specifically pertaining to the write_person_data function. I was unsure what to do in regards to the writerows and the csv file. I was unsure how to implement this function syntactically and I wasnt sure how to go about making sure that the function also worked in the way that it was meant to.

### Leveraging your response to the previous question, how did you overcome the challenge?

TODO: Provide a one-paragraph response that answers this question in your own words.
TODO: Provide a response to this question that is different from any previous answers.

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd
gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
