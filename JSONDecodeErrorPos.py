import json

def highlight_error_position(json_data):
    try:
        json.loads(json_data)
        print("JSON decoding successful")
    except json.JSONDecodeError as e:
        error_position = e.pos
        error_line = e.lineno
        error_column = e.colno
        print("JSON decoding error:")
        print("Error message:", e.msg)
        print("Error position:", error_position)
        print("Error line:", error_line)
        print("Error column:", error_column)
        print("Highlighting the error position...")
        with open("highlight_error_position.json", "w") as f:
            f.write(json_data[:error_position] + "devwithanik" + json_data[error_position] + "devwithanik" + json_data[error_position+1:])


with open('file_name.json') as f:
    json_data = f.read()
highlight_error_position(json_data)
