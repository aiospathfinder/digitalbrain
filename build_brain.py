import openai
import json
import textwrap

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


openai.api_key = open_file('openaiapikey.txt').replace(" ","")
openai.api_key = openai.api_key.replace("\n","") 
# print(openai.api_key) 

# This function takes two arguments, 'content' and 'engine'. 
# 'content' is the input text for which we want to generate the embedding vector
# 'engine' is the engine we want to use for the embedding generation (default is 'text-embedding-ada-002')
#The new model, text-embedding-ada-002, replaces five separate models for text search, text similarity, and code search, and outperforms our previous most capable model, Davinci, at most tasks, while being priced 99.8% lower.

def gpt3_embedding(content, engine='text-embedding-ada-002'):
    # OpenAI's Embedding API is used to create the embedding vector for the given input text
    response = openai.Embedding.create(input=content,engine=engine)
    
    # The embedding vector is extracted from the API response
    # The 'data' key in the response contains a list of dictionaries, each with an 'embedding' key.
    # The first dictionary in the list is selected (index 0) and its 'embedding' value is extracted
    vector = response['data'][0]['embedding']
    
    # The extracted embedding vector is returned as the function's output
    return vector



# The main function of the script, executed only when run as a standalone program
if __name__ == '__main__':
    # Open the input file and read its contents
    alltext = open_file('input.txt')
    
    # Wrap the text in chunks of 3000 characters each
    chunks = textwrap.wrap(alltext, 2700)
    
    # Initialize an empty list to store the processed information
    result = list()
    
    # Loop through each chunk and process its contents
    for chunk in chunks:
        # Get the embedding of the chunk using the gpt3_embedding function
        embedding = gpt3_embedding(chunk.encode(encoding='ASCII',errors='ignore').decode())
        
        # Store the chunk and its embedding in a dictionary
        info = {'content': chunk, 'vector': embedding}
        
        # Print the processed information for each chunk
        print(info, '\n\n\n')
        
        # Append the processed information to the result list
        result.append(info)
    
    # Write the result list as a JSON file
    #In this case, indent=2 means that each level in the JSON data will be indented by 2 spaces. This makes the output easier to read, as the structure of the JSON data is clearly defined.
    with open('secondbrain.json', 'w') as outfile:
        json.dump(result, outfile, indent=2)
