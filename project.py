import json
import os

#class
class Studentp:
    def __init__(self, name, country, universities, major, documents, completed_documents):
        self.name = name
        self.country = country
        self.universities = universities
        self.major = major
        self.documents = documents
        self.completed_documents = completed_documents

    # Create a readable profile summary for printing
    def __str__(self):
        profile = "\n📃 Your application profile:\n"

        profile += f"\n🔘 Name: {self.name}\n"
        profile += f"🔘 Country: {self.country['name']}\n"
        profile += f"🔘 Major: {self.major}\n"
        profile += "🔘 Universities:\n"

        for university in self.universities:
            profile += f"- {university['name']}\n"
            profile += f"   Website: {university['website']}\n"

        profile += "\n🔘 Documents:\n"
        for document in self.documents:
            if document in self.completed_documents:
                profile += f"✔ {document}\n"
            else:
                profile += f"⏳ {document}\n"

        return profile

def main():
    # Try to load user's previous profile from profile.json
    saved_profile = load_profile()
    if saved_profile:
        print("=" * 45)
        print(f"👋 Welcome back dear {saved_profile.name}!")
        print("=" * 45)
        print("\nYour saved profile:")
        print(saved_profile)
        #open edit/save menu for existing users
        load_result = manage_profile(saved_profile)
        if load_result == "new_profile":
            main()
            return
        elif load_result == "exit":
            return

    # Creat new profile
    print("=" * 45)
    print("🎓 Welcome to the Study Abroad Planner 🎓")
    print("=" * 45)

    name = input("Please enter your name: ").capitalize()
    print(f" 👋 Hi dear {name}, let's start your journey!\n")
    # Selected target country
    country = search_country()

    # Keep asking until universities are found.
    while True:
        universities = get_universities(country['name'])
        if universities:
            break
        print("❌ No universities found for this country.")
        print("Please enter another country.\n")
        country = search_country()
    print("\n🎉 Your selected universities:")

    for university in universities:
        print(f" - {university['name']}")

    #Get major and requirement documents
    major, requirements = get_application_profile()

    # Check which documents are already completed
    completed_documents = check_documents(requirements,)

    # Creat user's profile object.
    profile = Studentp(
        name,
        country,
        universities,
        major,
        requirements,
        completed_documents,
    )
    print(profile)
    # open profile management menu
    profile_result = manage_profile(profile)

    # Restart program or exit based on user's choice
    if profile_result == "restart":
        main()
        return
    elif profile_result == "exit":
        return

def search_country():
    """
    Search for a country, display matching results,
    and return the user's selected country.
    """
    with open("countries.json", "r", encoding="utf-8") as file:
        countries = json.load(file)

    #Keep asking until a valid country is selected.
    while True:
        country = input("\n🌍 Enter your dream country: ").strip().lower()

        matches = []
        for item in countries:
            if country in item["name"].lower():
                matches.append(item)

        # If no match is found, ask again.
        if not matches:
            print("❌ Country not found.pleas enter the offitiall country name..")
            continue

        print(" 🌍 Matching countries:\n")
        for i, item in enumerate(matches, start=1):
            print(f"{i}. {item['name']}")

        print("0. Search again")

        choice = input("\n👉 Choose country number: ")
        #Allow user to search again
        if choice == "0":
            continue

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(matches):
                selected_country = matches[choice - 1]
                print(f" ✅ Country selected is: {selected_country['name']}")
                print("-" * 40)

                return selected_country
            else:
                print("❌ Invalid number. Please choose one of the available options.")

def get_universities(country_name):
    """
    Find universities of selected country
    and let user choose 2 universities
    """
    with open("universities.json", "r", encoding="utf-8") as file:
        universities_data = json.load(file)

    # find universities of selected country
    universities = []
    for university in universities_data:
        if university["country"].lower() == country_name.lower():
            universities.append(university)

    print(f"\n🎓 We found {len(universities)} universities in {country_name}")
    print("  Now, please enter the names of your two preferred universities.")

    # If only one university exists, return it directly
    if len(universities) == 1:
        print(f"We only found {universities[0]['name']}")
        return universities

    selected_universities = []
    while len(selected_universities) < 2:
        print(f"\nEnter university {len(selected_universities)+1}:")
        search = input("🔎 ").strip().lower()

        matches = []
        for university in universities:
            if search in university["name"].lower():
                matches.append(university)

        # If exact/partial matches exist
        if not matches :
            print("University not found.try another name")
            continue

        print("\nDid you mean:\n")
        for i, university in enumerate(matches[:10], start=1):
            print(f"{i}. {university['name']}")
        print("0. None of these? (search again)")

        choose = input("\nChoose number: ")
        if choose == "0":
            continue

        if not choose.isdigit():
            continue

        choose = int(choose)
        if 1 <= choose <= len(matches[:10]):
            selected = matches[choose - 1]

            # Prevent selecting the same university twice
            already_selected = False

            for university in selected_universities:
                if university["name"] == selected["name"]:
                    already_selected = True
                    break

            if already_selected:
                print("❌ You already selected this univresity")
                continue
            selected_universities.append(selected)
            print(f"✅ Added: {selected['name']}")

    return selected_universities

def get_application_profile():
    """
    Ask the user for their targeted major
    and application requirements, then
    return the collected information.
    """
    print("-" * 40)
    print("\n📃 Let's create your application profile.")
    major = input("Which major are you applying for?\n").strip()

    # Store all required documents.
    requirements = []

    print("\nNow enter the certificates and documents you want to prepare for your application. one by one")
    print("----Enter 'done/d' when finished----\n")

    number = 1
    while True:
        doc = input(f"\n Enter requirement #{number}:\n").strip().capitalize()

        if  doc.lower() == "done" or doc.lower() == "d":
            break
        requirements.append(doc)
        number += 1

    return major, requirements

def check_documents(documents):
    """
    Check which documents are already completed by the user.
    """

    completed = []
    answer = input("\nDo you have any completed documents? (yes/no)\n").strip().lower()
    if answer == "yes" or answer == "y":
        print("\nYour documents:")
        for i, doc in enumerate(documents, start=1):
            print(f"{i}. {doc}")

        print("\nEnter document numbers you completed.")
        print("--------Type done/d when finished--------.")

        while True:
            choice = input("Document number: ").strip()
            if choice == "done" or choice == "d":
                break
            if choice.isdigit():
                number = int(choice)
                if 1 <= number <= len(documents):
                    #Add selected document to completed list.
                    completed.append(documents[number - 1])
    else:
        print("You can update your documents later.")

    print("\nCompleted documents:")
    if completed:
        for doc in completed:
            print(f"✔ {doc}")
    else:
        print("No completed documents yet.")
    return completed

def manage_profile(profile):
    """
    Manage user's profile, documents progress,
    editing options, saving, and exiting.
    """

    while True:
        # Get current documents and completed documents
        documents = profile.documents
        completed = profile.completed_documents
        print("\n📊 Application Progress")
        print("\n✔ Completed:")

        for doc in completed:
            print(f"- {doc}")
        print("\n⏳ Remaining:")
        for doc in documents:
            if doc not in completed:
                print(f"- {doc}")

        if len(documents) > 0:
            # Calculate application readiness percentage.
            progress = (len(completed) / len(documents)) * 100
            print(f"\n📈 You are {progress:.0f}% ready.")
            if progress == 100:
                print("""🎉 congratulations you are now 100% ready
🌟 Good luch with your scholarship""")
        else:
            print("\n No documents added yet.")

        # edit or save profile
        print("""\nWhat do you want to do?
1. Edit documents
2. Edit full profile (start programm from zero)
3. Save and exit""")
        choice = input("\nChoose: ")

        # Open document editing menu.
        if choice == "1":
            while True:
                print("""\nEdit documents:
1. Add new document
2. Mark document as completed
3. Remove document
0. Back""")
                option = input("\nChoose: ")
                if option == "0":
                    break

                # 1. Add new document
                elif option == "1":
                    new_doc = input("New document: ")
                    if new_doc:
                        profile.documents.append(new_doc)
                        print(f"\n✅ {new_doc} added successfully.")
                        print("\n📃 Current documents:")
                        for i, doc in enumerate(profile.documents, start=1):
                            status = "✔" if doc in profile.completed_documents else "⏳"
                            print(f"{i}. {status} {doc}")

                # 2. Mark document as completed
                elif option == "2":
                    print("\n📃 Which documents is copmpleted?:")
                    for i, doc in enumerate(profile.documents, start=1):
                        status = "✔" if doc in profile.completed_documents else "⏳"
                        print(f"{i}. {status} {doc}")
                    number = int(input("\nDocument number: "))
                    if 1 <= number <= len(profile.documents):
                        selected = profile.documents[number-1]
                        if selected not in profile.completed_documents:
                            profile.completed_documents.append(selected)
                            print(f"✅ {selected} marked as completed.\n")
                        else:
                            print("This document is already completed.")

                # 3. Remove document
                elif option == "3":
                    print("\n📃 Your documents:")
                    for i, doc in enumerate(profile.documents, start=1):
                        print(i, doc)
                    number = int(input("\nRemove number: "))
                    removed = profile.documents.pop(number-1)
                    if removed in profile.completed_documents:
                        profile.completed_documents.remove(removed)
                    print(f"🗑️ {removed} removed successfully.\n")

        # Delete old profile and creat a new one
        elif choice == "2":
            print("""⚠️ Are you sure you want to create a new profile?
1. Yes, delete old profile
2. No, go back""")
            confirm = input("Choose(num): ").strip()
            if confirm == "1":
                if os.path.exists("profile.json"):
                    os.remove("profile.json")
                    print("\n🗑️ Old profile deleted.")

                print("🔄  Creating a new profile...")
                return "new_profile"

            elif confirm == "2":
                print("\n↩️  Returning to profile menu...")
                continue
            else:
                print("\n❌ Invalid choice pleas choose 1 or 2.")
                return "restart"

        # Save current profile data into JSON file
        elif choice == "3":

            # Convert profile object into dictionary for JSON storage
            data = {
                "name": profile.name,
                "country": profile.country,
                "universities": profile.universities,
                "major": profile.major,
                "documents": profile.documents,
                "completed_documents": profile.completed_documents
            }

            with open("profile.json", "w", encoding="utf-8") as file:
                json.dump(
                    data,
                    file,
                    indent=4,
                    ensure_ascii=False
                )
                print("\n💾 Profile saved successfully!")
                print("👋 Goodbye!")
                return "exit"

def load_profile():
    """
    Load saved user profile from JSON file.
    """
    try:
        with open("profile.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return None

    # Recreate Studentp object from saved data
    profile = Studentp(
        data["name"],
        data["country"],
        data["universities"],
        data["major"],
        data["documents"],
        data["completed_documents"]
    )
    return profile

if __name__ == "__main__":
    main()
