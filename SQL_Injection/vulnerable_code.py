def vulnerable_login(username, password):
    # DANGER: Direct string concatenation of user input!
    # This is an abstract, non-working example for illustration.
    query = "SELECT * FROM users WHERE username = '" + username + \
            "' AND password = '" + password + "';"
    
    # In a real app, this would execute the query: cursor.execute(query)
    print(f"Executing Query: {query}")
    return query # For demonstration purposes only