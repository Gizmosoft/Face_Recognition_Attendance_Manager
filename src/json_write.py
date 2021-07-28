import json

def write_to_json_file(face_id, username):
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

# print(write_to_json_file(1,"Mason"))
