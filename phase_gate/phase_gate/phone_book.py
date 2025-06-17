contacts = []

def add_contact(first_name, last_name, phone_number):
    if len(phone_number) != 11 or not phone_number.startswith("0") or not phone_number.isdigit():
        return "Invalid phone number. It must be 11 digits and start with 0."

    for contact in contacts:
        if contact["phone_number"] == phone_number:
            return "Phone number already exists."

    new_contact = {
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number
    }
    contacts.append(new_contact)
    return f"Contact added: {first_name} {last_name} - {phone_number}"

def remove_contact(phone_number):
    for contact in contacts:
        if contact["phone_number"] == phone_number:
            contacts.remove(contact)
            return f"Contact removed: {contact['first_name']} {contact['last_name']}"
    return f"Contact with phone number {phone_number} not found."

def find_by_first_name(first_name):
    return [c for c in contacts if c["first_name"].lower() == first_name.lower()]

def find_by_last_name(last_name):
    return [c for c in contacts if c["last_name"].lower() == last_name.lower()]

def find_by_phone(phone_number):
    for contact in contacts:
        if contact["phone_number"] == phone_number:
            return contact
    return None

def edit_contact(phone_number, new_first, new_last, new_phone):
    for contact in contacts:
        if contact["phone_number"] == phone_number:
            contact["first_name"] = new_first
            contact["last_name"] = new_last
            contact["phone_number"] = new_phone
            return f"Contact updated to: {new_phone}"
    return f"Contact with phone number {phone_number} not found."

def list_all_contacts():
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{c['first_name']} {c['last_name']} - {c['phone_number']}" for list in contacts)