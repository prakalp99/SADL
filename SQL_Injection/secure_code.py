import sqlite3

def secure_login(username, password):
    # Use '?' as placeholders for user input
    sql_query = "SELECT * FROM users WHERE username = ? AND password = ?"
    
    # User inputs are passed as a separate tuple (username, password)
    # The database driver handles the secure injection of data.
    
    try:
        # Connect to a dummy database for the example
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        
        # This is the crucial step: passing parameters separately
        cursor.execute(sql_query, (username, password))
        
        # Check if a user was found
        user = cursor.fetchone()
        
        if user:
            print("✅ Login Successful! (Securely handled)")
            print(f"Found User: {user}")
            return True
        else:
            print("❌ Login Failed. (Securely handled)")
            return False
            
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        if conn:
            conn.close()

# --- Testing the Secure Fix ---

# 1. Test with the attack payload:
print("--- Testing with Attack Payload ---")
secure_login("'admin'", "' OR 1=1 --")
# Output will be "Login Failed" because the input is treated as literal text.

# 2. Test with a valid (but non-existent) user to show it works:
print("\n--- Testing with Normal Input ---")
# The actual SQL query would still be safe:
# SELECT * FROM users WHERE username = ''admin'' AND password = '' OR 1=1 --';
# The inner quotes are part of the literal username/password being searched for.
secure_login("user123", "secure_pass")