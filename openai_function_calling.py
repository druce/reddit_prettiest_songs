# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: llama
#     language: python
#     name: llama
# ---

# +
# function calling with openai

# +
import os
import pandas as pd

import openai

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import dotenv
dotenv.load_dotenv()


# +
openai.api_key = os.getenv('OPENAI_API_KEY')

models = openai.Model.list()
print([(i, m.id,) for i, m in enumerate(models["data"])])
models['data'][2]


# +

scope = "playlist-modify-public"

sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(scope=scope,
                                                       client_id=os.getenv('SPOTIFY_CLIENT_ID'),
                                                       client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
                                                       redirect_uri="https://druce.ai"
                                                      ))


# +
# get playlist id
# first create a playlist in Spotify UI to load songs
def get_playlist_id(playlist_name, verbose=False):
    playlists = sp.user_playlists(os.getenv('SPOTIFY_USERNAME'))
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            if playlist['name'] == playlist_name:
                if verbose:
                    print('"%s": offset %d, URI %s' % (playlist['name'], i + 1 + playlists['offset'], playlist['uri']))
                return playlist['id']

        # not found yet, get next page if there is one
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            return None

playlist_id = get_playlist_id("Reddit Prettiest Songs")
print(playlist_id)


# +
def get_tracks(playlist_id):
    
    results = sp.user_playlist(os.getenv('SPOTIFY_USERNAME'), 
                               playlist_id,
                               fields='tracks,next,name')
    tracks = results['tracks']
    
    # get tracks, paging as needed
    track_list = []
    while tracks:
        for track_item in tracks['items']:
            track_list.append(track_item['track'])
        # more pages?
        tracks = sp.next(tracks) if tracks['next'] else None
                    
    return pd.DataFrame({'artist': [track['artists'][0]['name'] for track in track_list],
                         'track': [track['name'] for track in track_list],
                         'uri': [track['uri'] for track in track_list],
                         'id': [track['id'] for track in track_list],
                         'popularity': [track['popularity'] for track in track_list],
                        })

get_tracks('08YFkbtTV6GBfNtjJ4PHDu')

# -

system_prompt = """You are a Spotify helper AI. 
I will make requests related to Spotify and you will generate python code
to generate and answer using the functions provided"
"""

user_message1 = "What is the id of my playlist entitled 'Reddit Prettiest Songs'"


# +
system_prompt = """You are a Spotify helper AI. 
I will make requests related to Spotify and you will generate python code
to generate and answer using the functions provided"
"""

user_message1 = "What is the id of my playlist entitled 'Reddit Prettiest Songs'"

def get_response(messages):
    response = openai.ChatCompletion.create(
        messages=messages,
        functions=[{"name": "get_playlist_id",
                    "description": "Return the Spotify playlist id based on the name of the playlist",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "playlist_name": {
                                "type": "string",
                                "description": "The name of the playlist"
                            },
                        },
                        "required": ["playlist_name"]
                    }
                   },
                   {
                "name": "get_tracks",
                       "description": "Return a dataframe of tracks in a playlist based on a Spotify playlist ID",
                       "parameters": {
                           "type": "object",
                           "properties": {
                               "playlist_id": {
                                   "type": "string",
                                   "description": "The Spotify playlist ID"
                               },
                           },
                           "required": ["playlist_id"]
                       }
                   },
                   
                  ],
        model="gpt-3.5-turbo-0613",
        temperature=0.1
    )
    return response

messages=[
    {
        "role": "system",
        "content": system_prompt,
    },
    {
        "role": "user",
        "content": user_message1,
    }
]

response=get_response(messages)
response
# -

fn_obj = response['choices'][0]['message']['function_call']
fn_obj

args = eval(fn_obj['arguments'])
args

print(f"{fn_obj['name']}(**args)")
eval(f"{fn_obj['name']}(**args)")

# +
user_message2 = "give me a dataframe of tracks in the Spotify playlist with ID 08YFkbtTV6GBfNtjJ4PHDu"
messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_message2,
            }
        ]

response=get_response(messages)
response

# -

fn_obj = response['choices'][0]['message']['function_call']
args = eval(fn_obj['arguments'])
print(f"{fn_obj['name']}(**args)")
eval(f"{fn_obj['name']}(**args)")

chain_message1 = "get a dataframe of tracks in the Spotify playlist named 'Reddit Prettiest Songs'"
messages = []
messages.append({"role": "system", "content": system_prompt,})
messages.append({"role": "user", "content": chain_message1,})
response=get_response(messages)
response


assistant_message1 = response['choices'][0]
assistant_message1

# +
assistant_message1 = {"content": '',
                      "function_call": assistant_message1['message']['function_call']}
messages.append({"role": "assistant", "content": assistant_message1,})

fn_obj = response['choices'][0]['message']['function_call']
args = eval(fn_obj['arguments'])
result = eval(f"{fn_obj['name']}(**args)")

chain_message2 = f"the previous function returned {result}. What next?"
messages.append({"role": "user", 'content': chain_message2})
messages

# -

response=get_response(messages)
response



