import json
import sys

def write_to_json_file(face_id, username):
    if __name__ == '__write_to_json_file__':
        write_to_json_file()

    try:
        user_dictionary = {
            "id"    : face_id,
            "name"  : username
        }
        with open("../database/userdata.json", "r+") as outfile:
            outfile_data = json.load(outfile)
            outfile_data["users"].append(user_dictionary)
            # Sets file's current position at offset.
            outfile.seek(0)
            # Serialization - converting above dictionary to a json object (binary)
            json.dump(outfile_data, outfile, indent = 4)
        return "Userdata stored successfully!"
    except:
        return "There was some error storing the userdata!"

def read_json_file():
    if __name__ == '__read_json_file__':
        read_json_file()

    # load json file
    jsonFile = open("../database/userdata.json", 'r')
    values = json.load(jsonFile)
    jsonFile.close()
    return values

def get_number_of_ids():            # Currently not using this
    if __name__ == '__get_number_of_ids__':
        get_number_of_ids()

    values = read_json_file()
    id_count = 0

    for i in values['users']:
        id_count = id_count + 1
    return id_count

def populate_name_array(name_value):
    if __name__ == '__populate_name_array__':
        populate_name_array(name_value)

    # if(len(name_value)<2):
    #     print("Insufficient User Database! Add more users to perform Face Recognition.")
    #     sys.exit(name_value)

    values = read_json_file()

    #parse through the userdata json file
    for i in values['users']:
        name_value.append(i['name'])
    return name_value


# print(write_to_json_file(1,"Mason"))
