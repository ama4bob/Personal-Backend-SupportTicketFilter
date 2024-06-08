# Butler-APIEndpoint

Description:
This is an API endpoint that is used to remove JSON subsets (retrieved by the client through a POST) that do not conform to the ticketing rules, and also will filter the 'desc' part of the ticket by removing any words present in the ignore list. The API will return the mutated JSON back to the client.

The helper functions that are used (stored in the utils file) is tested through unit testing. Postman is used to conduct
UAT testing through different cases:
- Main test representing JSON derived from butlerchi github
- Empty test
- 1+ test of only required keys in ticket
- Invalid test of either or all requirement keys missing
- 1+ test of valid ticket containing only desc
- 1+ test of valid ticket containing only file
- 1 test of valid ticket that contains greetings
- 1+ test of valid ticket that contains custom ignored words and phrases

Assumptions:
- The ignore list may have collisions with phrases (example: "Where are you", "are you there?" for "Where are you there? there?")
- The dictionary keys in the JSON can only be "createdAt", "tel", "msg", "desc"
- Does not currently sort the JSON file by the "createdAt" values (could be redundant for Butler)
- The endpoint only accepts local connections and may not be safe for internet connections
- File and desc is always valid (Need to discuss if empty values should be removed)

How to use:
1. Run the app.py server with python Flask
2. Build API on Postman (or any API builder) with a JSON that conforms to the Butler ticket standard
3. POST the JSON to http://127.0.0.1:8080/POSTrun
4. Retrieve the mutated JSON in the response body

TODO:
- Implement Rabin-Karp algorithm in FilterUtil.filterIgnoreList function
- Optimize for loop in app filterPOST function
- Implement server control UI for adding or removing ignored words
- Implement text saving and loading for ignored words
- Implement phrase ignore with phrase hierarchy
- Allow connection to AWS to retrieve JSON files
- Validate if attached files can be opened
- Use chatgpt API to see if ticket makes sense in English 
