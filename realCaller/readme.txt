To check Search results, send get request like this:
http://127.0.0.1:8000/search-person-by-name/?name={{ Enter name of your choice }}
http://127.0.0.1:8000/search-person-by-number/?number={{ Enter number of your choice }}

Note: For spam likelihood I've created a column called 'spam_count', the idea is, if the spam count is more than 0, we can display it in the frontend like: "{{ spam_count }} users reported spam" 
