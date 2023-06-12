# JSONDecodeError-Position-Highlighter


This script defines the highlight_error_position function, which takes a JSON string (json_data) as input. Inside the function, we attempt to decode the JSON using json.loads.
If decoding is successful, a success message is printed. However, if a JSONDecodeError occurs, we catch the exception and extract the error position, line number, and column number.
Next, we create a new file called "highlight_error_position.json" and write the original JSON string with the error position highlighted.
The error position is highlighted using string "devwithanik"
