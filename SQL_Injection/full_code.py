import sqlite3
import os

# Define the database file name
DB_NAME = 'sql_injection_demo.sqlite'

def setup_database():
    """Sets up the database, table, and a single admin user."""
    
    # 1. Clean up old file for a fresh start
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Create Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    
    # Insert a test admin user (Password is 'password123')
    cursor.execute("INSERT INTO users (id, username, password) VALUES (1, 'admin', 'password123')")
    conn.commit()
    conn.close()
    print(f"--- Setup Complete: Database '{DB_NAME}' created with 'admin' user. ---")


def run_vulnerable_test(username, password):
    """VULNERABLE: Direct string concatenation of user input."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # 🛑 DANGEROUS STEP: String formatting allows code injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    print("\n[TEST 1: VULNERABLE LOGIN]")
    print(f"Query executed: {query}")
    
    try:
        cursor.execute(query)
        user = cursor.fetchone()
        
        if user:
            print(f"❌ RESULT: VULNERABILITY SUCCESSFUL! Logged in as: {user[1]}")
        else:
            print("RESULT: Login failed.")
    except sqlite3.Error as e:
        print(f"Database error during vulnerable test: {e}")
    finally:
        conn.close()


def run_secure_test(username, password):
    """SECURE: Uses prepared statements with '?' placeholders."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # ✅ SECURE STEP: Use '?' placeholders
    sql_query = "SELECT * FROM users WHERE username = ? AND password = ?"
    
    print("\n[TEST 2: SECURE LOGIN (The Fix)]")
    print(f"Query template: {sql_query}")
    
    try:
        # Input is passed separately and treated ONLY as data
        cursor.execute(sql_query, (username, password))
        user = cursor.fetchone()
        
        if user:
            print(f"❌ RESULT: Login SUCCESSFUL (Legitimate access only): {user[1]}")
        else:
            print("✅ RESULT: Login failed. (Attack failed successfully)")
    except sqlite3.Error as e:
        print(f"Database error during secure test: {e}")
    finally:
        conn.close()


# --- Main Execution ---

# 1. Prepare the database
setup_database()

# 2. Define the attack payload
ATTACK_USERNAME = 'admin'
# The payload uses ' OR 1=1' to bypass the password check, and '--' to comment out the rest.
ATTACK_PASSWORD = "' OR 1=1 --"

# 3. Run the Vulnerable Test
run_vulnerable_test(ATTACK_USERNAME, ATTACK_PASSWORD)

# 4. Run the Secure Test
run_secure_test(ATTACK_USERNAME, ATTACK_PASSWORD)

# 5. Show that secure login works with a valid password
print("\n[TEST 3: SECURE LOGIN (Valid Credentials)]")
run_secure_test('admin', 'password123')