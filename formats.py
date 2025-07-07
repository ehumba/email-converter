supported_formats = [
    "first.last",
    "f.last",
    "first_last",
    "first.l",
    "last.first",
    "last.f",
    "l.first",
    "flast",
    "first",
    "last"
]

def generate_emails(names, format, domain):
    name_list = names.split("\n")
    output = ""

    for name in name_list:
        # Split the name into first and last name in lowercase
        lower_name = name.lower()
        split_name = lower_name.split()
        if len(split_name) > 2:
            raise Exception("Error: Please only enter first name and last name")
        first_name = split_name[0]
        last_name = split_name[1]
        
        # Modify the name into the given format
        match format:
            case "first.last":
                formatted_name = first_name + "." + last_name
            case "f.last":
                formatted_name = first_name[0] + "." + last_name
            case "first_last":
                formatted_name = first_name + "_" + last_name
            case "first.l":
                formatted_name = first_name + "." + last_name[0]
            case "last.first":
                formatted_name = last_name + "." + first_name
            case "last.f":
                formatted_name = last_name + "." + first_name[0]
            case "l.first":
                formatted_name = last_name[0] + "." + first_name
            case "flast":
                formatted_name = first_name[0] + last_name
            case "last":
                formatted_name = last_name
            case "first":
                formatted_name = first_name

        # Create the output string
        address = formatted_name + "@" + domain
        output += f"{address}\n"

    return output