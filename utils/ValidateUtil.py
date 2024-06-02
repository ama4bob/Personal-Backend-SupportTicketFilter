# Validates the ticket to see if the ticket is missing the time or the phone number, and it must be populated
# Input: A ticket
# Output: A boolean indicating whether the ticket is valid or not
def validateTicket(input: dict):
    if input.get("createdAt") != None and input.get("createdAt") != "" and input.get("tel") != None and input.get("tel") != "":
        return False
    return True

