from pyscript import Element

def generate_message():
    Name = Element("Name").element.value
    Age = Element("Age").element.value
    School = Element("School").element.value


    greeting = "Hello, \"Student\"!"
    info_header = "\tHere is your student profile information:\n"


    profile_message = f"""{greeting}
{info_header}
Name: {name}
Age: {age}
School: {school}
End of profile.
"""


    Element("output").element.innerText = profile_message