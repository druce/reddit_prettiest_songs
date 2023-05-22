# reddit_prettiest_songs

Use OpenAI API to do entity extraction of all the songs from this [huge Reddit thread](https://www.reddit.com/r/AskReddit/comments/12viv4v/what_is_the_prettiest_song_you_ever_heard_in_your/) (25k replies) and create a [Spotify playlist](https://open.spotify.com/playlist/08YFkbtTV6GBfNtjJ4PHDu?si=753676632a9b47c6) with ~1000+ songs

 - Use Reddit [PRAW API](https://praw.readthedocs.io/en/stable/) to download all the comments (with [Reddit API key](https://www.reddit.com/prefs/apps))
 - Use [OpenAI API](https://platform.openai.com/docs/quickstart) with a prompt like, extract all the songs from this text to CSV (with [OpenAI API key](https://platform.openai.com/account/api-keys)). Made a couple of followup prompts to fix spelling, dedupe, cleanup.
 - Use [Spotify API](https://developer.spotify.com/documentation/web-api/reference/add-tracks-to-playlist) with [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/#examples) to make a playlist (with [Spotify API key](https://developer.spotify.com/documentation/web-api/tutorials/getting-started))
 - Needed a bit of scrubbing, but about 1 day of work, wouldn't have been possible to do a 1000-song playlist manually without a team of Mechanical Turks or something

To run the Jupyter notebook you will need to sign up for those 3 APIs, and put IDs and secrets in a `.env` file similar to `dot-env-template`.

ChatGPT sometimes does really well, for instance this extracts 4 good CSV records:

```
Gordon is an amazing poet and so versatile. Il"If You Could Read My Mind," "Early Morning Rain," Old Dan's Records," "Don Quixote," and of course, "The Wreck of the Edmund Fitzgerald" are all so different but so good. 
```

also handles `" Smaointe" is beautiful too.` in the context of an Enya conversation.

also handles `The Killers do a pretty fantastic version of this tune as well. Around the release of "Sam's Town" they recorded a few tracks at Abbey Road studios that were eventually dropped as B-sides and a cover of this song was one of them.` in the context of Romeo and Juliet, by Dire Straits

But sometimes it hallucinates, Mrs. Robinson ended up in the playlist but it's nowhere in the thread. Possibly ChatGPT just thought it should be there. (not wrong probably). 

Note that all of this is at a temperature of 0, so ChatGPT should not get super creative.

Spotify search API is pretty wonky, doesn't like apostrophes, maybe they need to be escaped, sometimes returns covers and karaoke versions instead of well known songs.

Top 20 tracks  below.

| artist | track | votes |
| :----- |:----- | ----: |
|Claude Debussy|Clair de Lune|22088|
|Simon & Garfunkel|Scarborough Fair|11922|
|The Beatles|In my Life|9049|
|Erik Satie|Gymnopédies|7620|
|The Cranberries|Dreams|7305|
|Israel Kamakawiwoole|Over the Rainbow|6681|
|Neil Young and Crazy Horse|Harvest Moon|5337|
|Jim Croce|Time in a Bottle|5285|
|Mazzy Star|Fade into you|4357|
|Don McLean|Vincent (Starry, Starry Night)|3989|
|The Beach Boys|God Only Knows|3882|
|Sigur Ros|Hoppipolla|3819|
|Elton John|Your Song|3636|
|Edith Piaf|La Vie en Rose|3205|
|Lord Huron|The night we met|3187|
|Fleet Foxes|White Winter Hymnal|2888|
|The Righteous Brothers|Unchained Melody|2862|
|Fleetwood Mac|Landslide|2822|
|Joni Mitchell|Both Sides Now|2810|
|John Denver|Annie’s Song|2779|
