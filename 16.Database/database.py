import sqlite3 # import the sqlite3 module

# 1. Connect to the database (creates a new file if it doesn't exist)
# Using the with statement automatically closes the connection
try:
    with sqlite3.connect('my_app.db') as conn:
        cursor = conn.cursor() # Create a Cursor object to run SQL Commands

        # 2. Create a Table (if it doesn't exist)
        # CREATE TABLE IF NOT EXISTS creates the table only if it doesn't already exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        """)
        print("Table 'users' created successfully (or already exists).")

        # 3. Insert Data (INSERT)
        # Using a Parameterized Query (Placeholder) helps prevent SQL Injection
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Bob", "bob@example.com"))
        print("New users inserted.")

        # This will cause an IntegrityError due to the UNIQUE constraint on email
        try:
            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice Duplicate", "alice@example.com"))
            print("Duplicate user inserted. (This should have caused an error)")
        except sqlite3.IntegrityError:
            print("Error: The email 'alice@example.com' already exists.")

        # 4. Get Data (SELECT)
        print("\n--- Data from the Users Table ---")
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall() # Get all results as a List of Tuples
        for row in rows:
            print(row)

        # 5. Get Data with a Condition (WHERE Clause)
        print("\n--- Searching by Email (Bob) ---")
        cursor.execute("SELECT * FROM users WHERE email = ?", ("bob@example.com",))
        bob_data = cursor.fetchone() # Get a single result
        print(bob_data)

        # 6. Update Data (UPDATE)
        cursor.execute("UPDATE users SET name = ? WHERE email = ?", ("Robert", "bob@example.com"))
        print("\nBob's name has been updated to Robert.")

        # Verify the update
        cursor.execute("SELECT * FROM users WHERE email = ?", ("bob@example.com",))
        updated_bob = cursor.fetchone()
        print(updated_bob)

        # 7. Delete Data (DELETE)
        cursor.execute("DELETE FROM users WHERE name = ?", ("Alice",))
        print("\nAlice has been deleted.")

        # Verify the deletion
        print("\n--- Data from the Users Table after deletion ---")
        cursor.execute("SELECT * FROM users")
        remaining_users = cursor.fetchall()
        for user in remaining_users:
            print(user)

    # When the with block ends, the connection automatically commits and closes
    print("\nDatabase operations completed. Connection is closed.")

except sqlite3.Error as e:
    print(f"Database Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# The WRONG way (prone to SQL Injection)
# user_input_name = "Robert'; DROP TABLE users;--"
# cursor.execute(f"DELETE FROM users WHERE name = '{user_input_name}'")

# The CORRECT way (Parameterized Query)
user_input_name = "Robert'; DROP TABLE users;--" # Even if this string is provided
cursor.execute("DELETE FROM users WHERE name = ?", (user_input_name,)) # The Database will see this as just Text

