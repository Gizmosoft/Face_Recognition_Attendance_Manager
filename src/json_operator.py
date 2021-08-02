import json

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

def get_id():
    if __name__ == '__get_id__':
        get_id()

    # load json file
    jsonFile = open("../database/userdata.json", 'r')
    values = json.load(jsonFile)
    jsonFile.close()

    # store id into variable
    id_value = values['users'][0]['id']
    name_value = values['users'][0]['name']
    return id_value + " " + name_value

print(get_id())
# print(write_to_json_file(1,"Mason"))
