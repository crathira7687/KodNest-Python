n = int(input("enter the number:"))
registrations = set()

# 1. Collect student IDs
for i in range(n):
    student_id = input("enter the student id:").strip()
    registrations.add(student_id)

# 2. Prompt for search ID outside the loop
search_id = input("enter the student id to be searched:").strip()

# 3. Calculate unique and duplicate counts
unique_count = len(registrations)
duplicate_count = n - unique_count

print(f"unique registrations: {unique_count}")
print(f"Duplicate entries: {duplicate_count}")

# 4. Check if search_id is registered
if search_id in registrations:
    print("Registered")
else:
    print("Not registered")
