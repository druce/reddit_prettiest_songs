# reddit_prettiest_songs

Use OpenAI API to do entity extraction of all the songs from this [huge Reddit thread](https://www.reddit.com/r/AskReddit/comments/12viv4v/what_is_the_prettiest_song_you_ever_heard_in_your/) (24k replies) and create a [Spotify playlist](https://open.spotify.com/playlist/08YFkbtTV6GBfNtjJ4PHDu?si=753676632a9b47c6) with ~800+ songs

 - Use Reddit [PRAW API](https://praw.readthedocs.io/en/stable/) to download all the comments (with [Reddit API key](https://www.reddit.com/prefs/apps))
 - Use [OpenAI API](https://platform.openai.com/docs/quickstart) with a prompt like, extract all the songs from this text to CSV (with [OpenAI API key](https://platform.openai.com/account/api-keys))
 - Use [Spotify API](https://developer.spotify.com/documentation/web-api/reference/add-tracks-to-playlist) with [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/#examples) to make a playlist (with [Spotify API key](https://developer.spotify.com/documentation/web-api/tutorials/getting-started))
 - Needed a bit of scrubbing, but about 1 day of work, wouldn't have been possible to do a 900-song playlist manually without a team of Mechanical Turks or something
 - Possible enhancements: Could prompt ChatGPT on a per-comment basis and save a file for each comment's extracted songs, make it easier to track down what OpenAI gets wrong, have a resumable, retryable, repeatable process.
 - Could get the reply karma score and save it, rank the songs by sum(mention x reply karma)
 - Could make a Reddit bot that people could summon to extract all the songs

To run the Jupyter notebook you will need to sign up for those 3 APIs, and put IDs and secrets in a `.env` file similar to `dot-env-template`.

Submit pull requests if anything can be fixed, and also any correction to `gold.csv` which was the final file after some manual scrubbing. But still had some songs that weren't found via Spotify search, or where wrong song like a karaoke cover was returned.

| artist | track |
| :------ |:------ |
| 311 | Amber |
| A Perfect Circle | 3 Libras |
| A Perfect Circle | Blue |
| A Perfect Circle | Gimme Gimme Gimme |
| A Perfect Circle | Judith |
| A Perfect Circle | Orestes |
| A Perfect Circle | The Noose |
| A Perfect Circle | The Nurse Who Loved Me |
| ABBA | Fernando |
| ABBA | One Of Us |
| ABBA | The Winner Takes It All |
| Aaron Copland | Fanfare for the Common Man |
| Aerosmith | Dream On |
| Al Stewart | Year of the Cat |
| Alanis Morissette | Uninvited |
| Alice In Chains | Don't Follow |
| Alice In Chains | Nutshell |
| Alice In Chains | Rain When I Die (2022 Remaster) |
| Alicia Keys | If I Ain't Got You |
| Alison Krauss & Union Station | The Lucky One |
| Alison Krauss & Union Station | When You Say Nothing At All |
| Alison Krauss | Whiskey Lullaby |
| Allman Brothers Band | Little Martha |
| Alphaville | Forever Young |
| America | A Horse with No Name |
| America | Sister Golden Hair |
| America | Ventura Highway |
| Amy Winehouse | Wake Up Alone |
| Anderson .Paak | Heart Don't Stand a Chance |
| Andrea Bocelli | Con te partirò |
| Andrew Lloyd Webber | Pie Jesu |
| Andy Williams | Days of Wine and Roses |
| Anne Murray | You Needed Me |
| Annie Lennox | Into the West |
| Aphex Twin | #20 |
| Aphex Twin | Acrid Avid Jam Shred |
| Aphex Twin | Avril 14th |
| Aphex Twin | Donkey Rhubarb |
| Aphex Twin | Fingerbib |
| Aphex Twin | IZ-US |
| Aphex Twin | QKThr |
| Art Garfunkel | All I Know |
| Art Garfunkel | Watermark |
| Babyface | Every Time I Close My Eyes (with Kenny G) |
| Band of Horses | No One's Gonna Love You |
| Band of Horses | The Funeral |
| Barry Manilow | Could It Be Magic |
| Basil Poledouris | Conan the Barbarian (arr. P. Pelster for organ): Theology / Civilization |
| Beach House | 10 Mile Stereo |
| Beach House | Myth |
| Beach House | PPP |
| Beach House | Space Song |
| Bee Gees | How Deep Is Your Love |
| Ben E. King | Stand by Me |
| Bette Midler | The Rose |
| Beyoncé | PLASTIC OFF THE SOFA |
| Bibio | lovers’ carvings |
| Big Shaq | Man's Not Hot |
| Big Star | Thirteen |
| Bill Withers | Lovely Day |
| Billie Eilish | ocean eyes |
| Billy Joel | 52nd Street |
| Billy Joel | And So It Goes |
| Billy Joel | Only the Good Die Young |
| Billy Joel | She's Always a Woman |
| Billy Joel | She's Got a Way |
| Billy Joel | Vienna |
| Billy Joel | Where's the Orchestra |
| Björk | Hyperballad |
| Björk | Unison |
| Björkliden | Yoga Nidra |
| Black Pumas | Colors |
| Blue Rodeo | Try - 2012 Remaster |
| Bob Dylan | Girl from the North Country |
| Bob Dylan | Just Like a Woman |
| Bobby Charles | I Must Be in a Good Place Now |
| Bon Iver | Flume |
| Bon Iver | Holocene |
| Bon Iver | Skinny Love |
| Bonnie Raitt | Angel from Montgomery - 2008 Remaster |
| Bonnie Raitt | I Can't Make You Love Me |
| Boston | Feelin' Satisfied |
| Box Car Racer | There Is |
| Boz Scaggs | Harbor Lights |
| Brand New | The Boy Who Blocked His Own Shot |
| Brandi Carlile | The Story |
| Bread | Aubrey |
| Bread | Everything I Own |
| Bread | If |
| Brian Eno | Deep Blue Day - Remastered 2005 |
| Bright Eyes | Something Vague |
| Bruce Springsteen | Atlantic City |
| Buddy Holly | (Ummmm, Oh Yeah) Dearest |
| CHVRCHES | The Mother We Share |
| Camille Saint-Saëns | The Carnival of the Animals, R. 125: XIII. The Swan (Arr. for Cello and Piano) |
| Camille Saint-Saëns | Carnival of the Animals: XIII. Le Cygne (The Swan) |
| Carole King | (You Make Me Feel Like) A Natural Woman |
| Carpenters | (They Long To Be) Close To You |
| Carpenters | Superstar |
| Carpenters | We’ve Only Just Begun |
| Carpenters | Yesterday Once More |
| Charlie Chaplin | Smile (Theme from Modern Times) [with Joshua Bell] |
| Chris Cornell | Thank You - Recorded Live At Sixth & I Historic Synagogue, Washington, DC on April 17, 2011 |
| Chris Cornell | Nothing Compares 2 U - Live At SiriusXM/2015 |
| Chris Stapleton | Traveller |
| Christophe | Aline |
| Cj Da Juice | Better than I was Yesterday |
| Claude Debussy | Debussy: Arabesque no. 2 in G major (Deux Arabesques, L. 66) |
| Claude Debussy | Préludes / Book 1, L. 117: 8. La fille aux cheveux de lin |
| Claude Debussy | Suite bergamasque, L. 75: III. Clair de lune |
| Climax Blues Band | I Love You |
| Cocteau Twins | Evangeline |
| Cody Fry | I Hear a Symphony |
| Coldplay | A Sky Full of Stars |
| Coldplay | Clocks |
| Coldplay | Fix You |
| Coldplay | Paradise |
| Coldplay | The Scientist |
| Céline Dion | The Prayer |
| Dan Fogelberg | Longer |
| Daniel Bedingfield | If You're Not The One |
| Daniel Caesar | Best Part (feat. H.E.R.) |
| Dave Matthews Band | Crash into Me |
| Death Cab for Cutie | Black Sun |
| Death Cab for Cutie | Crooked Teeth |
| Death Cab for Cutie | I Will Follow You into the Dark |
| Death Cab for Cutie | Soul Meets Body |
| Death Cab for Cutie | Transatlanticism |
| Death Cab for Cutie | What Sarah Said |
| Declan O'Rourke | Galileo |
| Deftones | Beauty School |
| Denez Prigent | Gortoz A Ran - From Black Hawk Down |
| Des'ree | I'm Kissing You |
| Dire Straits | Brothers In Arms |
| Dire Straits | Romeo and Juliet |
| Dire Straits | Sultans of Swing |
| Dire Straits | Your Latest Trick |
| Disturbed | The Sound of Silence |
| Dolly Parton | I Will Always Love You |
| Dolly Parton | Love Is Like a Butterfly |
| Don McLean | Vincent (Starry, Starry Night) |
| Don McLean | Crying |
| Donna Lewis | I Love You Always Forever |
| Donnie Iris | Ah! Leah! |
| Doris Day | Dream a Little Dream of Me (with Paul Weston & His Music From Hollywood) |
| Eagles | Desperado - 2013 Remaster |
| Eagles | Seven Bridges Road - Live; 1999 Remaster |
| Edvard Grieg | Peer Gynt Suite No. 2, Op. 55: IV. Solveig's Song |
| Edvard Grieg | Peer Gynt, Op. 23, Act IV: Morning Mood |
| Ella Fitzgerald | I Can't Stop Loving You - Live / 1972 |
| Ella Fitzgerald | Stars Fell On Alabama |
| Ella Fitzgerald | Summertime |
| Elliott Smith | Angeles |
| Elton John | Rocket Man (I Think It's Going To Be A Long, Long Time) |
| Elton John | Bennie And The Jets - Remastered 2014 |
| Elton John | Bennie And The Jets |
| Elton John | Goodbye Yellow Brick Road - Remastered 2014 |
| Elton John | Tiny Dancer |
| Elton John | Your Song |
| Elvis Presley | Can’t Help Falling in Love - Acoustic Cover |
| Elvis Presley | Yesterday - Live |
| Elvis Presley | Young and Beautiful |
| Emerson, Lake & Palmer | Lucky Man - 2012 Remaster |
| Emilíana Torrini | Sunny Road |
| Ennio Morricone | Finale from Once Upon a Time in the West - Instrumental |
| Ennio Morricone | Un amico - Titoli |
| Enya | Amarantine |
| Enya | Boadicea |
| Enya | Book of Days |
| Enya | Caribbean Blue |
| Enya | Flora's Secret |
| Enya | Lothlórien |
| Enya | May It Be |
| Enya | No Holly for Miss Quinn |
| Enya | Only Time |
| Enya | Orinoco Flow |
| Enya | Shepherd Moons |
| Enya | Storms in Africa |
| Enya | Wild Child |
| Eric Clapton | Tears in Heaven - Acoustic Live |
| Eric Clapton | Wonderful Tonight |
| Eric Johnson | Cliffs Of Dover - Instrumental |
| Erik Satie | Gnossienne No. 1 |
| Erik Satie | Gymnopédie No. 1 |
| Erykah Badu | Green Eyes |
| Esthero | Breath From Another |
| Etta James | At Last |
| Etta James | I'd Rather Go Blind |
| Eva Cassidy | Fields Of Gold |
| Eva Cassidy | Songbird |
| Evanescence | Good Enough |
| Evanescence | My Immortal |
| Explosions In The Sky | Your Hand In Mine |
| Extreme | More Than Words |
| Family of the Year | Hero |
| Fiona Apple | I Know |
| First Aid Kit | Emmylou |
| First Aid Kit | My Silver Lining |
| Fleet Foxes | Blue Spotted Tail |
| Fleet Foxes | Helplessness Blues |
| Fleet Foxes | Meadowlarks |
| Fleet Foxes | Mykonos |
| Fleet Foxes | Ragged Wood |
| Fleet Foxes | Sunblind |
| Fleet Foxes | The Shrine / An Argument |
| Fleet Foxes | Tiger Mountain Peasant Song |
| Fleet Foxes | Wading In Waist-High Water |
| Fleet Foxes | White Winter Hymnal |
| Fleetwood Mac | The Chain - Live at Warner Brothers Studios in Burbank, CA 5/23/97 |
| Fleetwood Mac | Dreams - 2004 Remaster |
| Fleetwood Mac | Everywhere - 2017 Remaster |
| Fleetwood Mac | Landslide |
| Fleetwood Mac | Little Lies - 2017 Remaster |
| Fleetwood Mac | Over My Head |
| Fleetwood Mac | Sara |
| Fleetwood Mac | Silver Springs - 2004 Remaster |
| Fleetwood Mac | Songbird - 2004 Remaster |
| Flight Facilities | Clair De Lune |
| Florence + The Machine | Stand By Me |
| Flying Lotus | Getting There |
| Flyte | Archie, Marry Me |
| Foo Fighters | Everlong - Acoustic Version |
| Frank Mills | Music Box Dancer |
| Frank Ocean | Ivy |
| Frank Ocean | Pink + White |
| Frank Ocean | White Ferrari |
| Frank Zappa | Watermelon In Easter Hay |
| Fred Astaire | Cheek to Cheek |
| Frédéric Chopin | Chopin: Nocturne No. 20 in C-Sharp Minor, Op. Posth. |
| Frédéric Chopin | Nocturne No. 2 in E-Flat Major, Op. 9 No. 2 |
| Fugees | Killing Me Softly With His Song |
| Gang Starr | Moment Of Truth |
| Gary Jules | Mad World |
| George Michael | Careless Whisper |
| Glee Cast | Blackbird |
| Glen Hansard | Falling Slowly |
| Goldfrapp | Felt Mountain |
| Gordon Lightfoot | Beautiful |
| Gordon Lightfoot | If You Could Read My Mind |
| Gordon Lightfoot | The Wreck of the Edmund Fitzgerald |
| Gorillaz | On Melancholy Hill |
| Gorillaz | To Binge (feat. Little Dragon) |
| Grateful Dead | They Love Each Other - Live at Barton Hall, Cornell University, Ithaca, NY 5/8/77 |
| Grateful Dead | Box of Rain - 2013 Remaster |
| Grateful Dead | Casey Jones - 2013 Remaster |
| Grateful Dead | Mountains of the Moon - 2013 Remaster |
| Grateful Dead | Ripple - 2013 Remaster |
| Grateful Dead | Standing on the Moon - 2013 remaster |
| Green Day | Good Riddance (Time of Your Life) |
| Greg Brown | Spring Wind |
| Gregory Alan Isakov | The Stable Song |
| Grimes | Symphonia IX (My Wait Is U) |
| Grover Washington, Jr. | Just the Two of Us (feat. Bill Withers) |
| Gustav Holst | The Planets, Op. 32: 4. Jupiter, the Bringer of Jollity |
| Hans Zimmer | This Land - From The Lion King/Score |
| Hans Zimmer | Chevaliers De Sangreal - From The Da Vinci Code Original Motion Picture Soundtrack |
| Hans Zimmer | Injection |
| Hans Zimmer | No Time for Caution |
| Hans Zimmer | Time |
| Hans Zimmer | Wallace |
| Harold Arlen And E.Y. Harburg | Somewhere over the Rainbow |
| Harry Chapin | Cat's in the Cradle |
| Harry Styles | Sign of the Times |
| Hayde Bluegrass Orchestra | All My Tears |
| Heart | Dog & Butterfly |
| Heart | Dreamboat Annie |
| Heart | These Dreams |
| Henry Mancini | Moon River(Vocal Audrey Hepburn) |
| Herb Alpert & The Tijuana Brass | Ladyfingers |
| Howie Day | Collide |
| Hozier | Wasteland, Baby! |
| Hozier | Cherry Wine - Live |
| Hozier | In a Week (feat. Karen Cowley) |
| Hozier | In the Woods Somewhere |
| Hozier | Jackie and Wilson |
| Hozier | Like Real People Do |
| Hozier | Run |
| INXS | Beautiful Girl |
| INXS | Never Tear Us Apart |
| IZ*ONE | Secret Story of the Swan |
| Ichiko Aoba | Pilgrimage |
| Imogen Heap | Goodnight and Go |
| Imogen Heap | Hide and Seek |
| Incubus | Aqueous Transmission |
| Indigo Girls | Closer to Fine |
| Indigo Girls | Ghost |
| Iron & Wine | Flightless Bird, American Mouth |
| Iron & Wine | Boy With a Coin |
| Iron & Wine | Naked as We Came |
| Iron & Wine | Such Great Heights |
| Iron & Wine | Upward Over the Mountain |
| Israel Kamakawiwo'ole | Over the Rainbow |
| JVKE | golden hour |
| Jackie DeShannon | What The World Needs Now Is Love |
| Jacob James | Rushes |
| James Taylor | Handy Man |
| James Taylor | You’ve Got a Friend |
| Jay-Jay Johanson | Poison |
| Jed Kurzel | Dead Civilization |
| Jed Kurzel | The Animus |
| Jeff Buckley | Lover, You Should've Come Over |
| Jeff Buckley | Grace |
| Jeff Buckley | Hallelujah |
| Jeff Buckley | Just Like a Woman |
| Jeff Buckley | Lilac Wine |
| Jeremy Soule | Kyne's Peace |
| Jewel | Angel Standing By |
| Jim Croce | Next Time, This Time - Live at Harper College 2/5/73 |
| Jim Croce | Age |
| Jim Croce | Alabama Rain |
| Jim Croce | Dreamin' Again |
| Jim Croce | I'll Have To Say I Love You In A Song |
| Jim Croce | Lover's Cross |
| Jim Croce | Operator (That's Not the Way It Feels) |
| Jim Croce | Photographs & Memories |
| Jim Croce | Rapid Roy (That Stock Car Boy) |
| Jim Croce | Speedball Tucker |
| Jim Croce | These Dreams |
| Jim Croce | Time in a Bottle |
| Jimi Hendrix | All Along the Watchtower |
| Jimi Hendrix | Bold as Love |
| Jimi Hendrix | Castles Made of Sand |
| Jimi Hendrix | If 6 Was 9 |
| Jimi Hendrix | Little Wing |
| Jimmy Eat World | Hear You Me |
| Joaquín Rodrigo | Aranjuez Concerto BWV 1056 |
| Joe Cocker | Up Where We Belong - From An Officer And A Gentleman |
| Joe Cocker | You Are So Beautiful |
| Johann Pachelbel | Pachelbel: Canon and Gigue for Three Violins and Continuo in D Major: Canon |
| Johann Sebastian Bach | Brandenburg Concerto No. 2 in F Major, BWV 1047: I. Allegro |
| Johann Sebastian Bach | Cello Suite No. 1 in G Major, BWV 1007: I. Prélude |
| Johann Sebastian Bach | Orchestral Suite No. 3 in D Major, BWV 1068: II. Air Air on the G string |
| Johann Sebastian Bach | Toccata and Fugue in D minor |
| John Denver | Take Me Home, Country Roads - Original Version |
| John Denver | Annie's Song |
| John Denver | Aspenglow |
| John Denver | Sunshine On My Shoulders |
| John Denver | Thank God I'm a Country Boy |
| John Denver | This Old Guitar |
| John Fogerty | Joy Of My Life |
| John Legend | All of Me |
| John Lennon | Beautiful Boy (Darling Boy) - Remastered 2010 |
| John Mayer | Gravity |
| John Prine | Christmas in Prison |
| John Prine | In Spite of Ourselves (feat. Iris DeMent) |
| Johnny Cash | Hurt |
| Johnny Mathis | Chances Are (with Ray Conniff & His Orchestra) |
| Jon Bellion | Hand Of God - Outro |
| Jon Hopkins | Immunity |
| Joni Mitchell Tribute by Strings Attached | A Case of You |
| Joni Mitchell | Both Sides Now |
| Joni Mitchell | River |
| Joni Mitchell | The Circle Game |
| Journey | Faithfully |
| Journey | Open Arms |
| Judy Collins | So Early, Early in the Spring |
| Judy Collins | First Boy I Loved |
| Julie London | Fly Me To The Moon (In Other Words) |
| KISS | Beth |
| Kansas | Dust in the Wind |
| Kanye West | 24 |
| Kanye West | Runaway |
| Kate Bush | This Woman's Work - 2018 Remaster |
| Kate Bush | Wuthering Heights - 2018 Remaster |
| Katie Melua | Dreams on Fire |
| Keane | Somewhere Only We Know |
| Keola Beamer | Kalena Kai |
| Kurt Cobain | And I Love Her |
| Lana Del Rey | Salvatore |
| Lana Del Rey | West Coast |
| Lana Del Rey | Young And Beautiful |
| Led Zeppelin | Going to California - Remaster |
| Led Zeppelin | Ten Years Gone - Remaster |
| Led Zeppelin | Thank You - 1990 Remaster |
| Led Zeppelin | The Rain Song - Remaster |
| Leon Bridges | River |
| Leonard Cohen | Hallelujah |
| Lil Yachty | drive ME crazy! |
| Lily Allen | Somewhere Only We Know |
| Linda Ronstadt | Blue Bayou |
| Linda Ronstadt | Long Long Time |
| Linkin Park | My December |
| Linkin Park | One More Light |
| Live | The Dolphin's Cry |
| Loggins & Messina | Danny's Song |
| Loggins & Messina | House at Pooh Corner - Live |
| Lord Huron | Harvest Moon - Recorded at Spotify Studios NYC |
| Lord Huron | I Lied (with Allison Ponthier) |
| Lord Huron | Meet Me in the Woods |
| Lord Huron | The Night We Met |
| Loreena McKennitt | Never-Ending Road (Amhrán Duit) |
| Louis Armstrong | Dream A Little Dream Of Me |
| Louis Armstrong | What A Wonderful World |
| Ludovico Einaudi | Nuvole Bianche |
| Ludwig van Beethoven | Bagatelle No. 25 in A Minor, WoO 59 Für Elise |
| Ludwig van Beethoven | Beethoven: 'Ode To Joy' From Symphony No. 9 In D Minor 'Choral', Op. 125 |
| Låpsley | Painter (Valentine) |
| Léo Delibes | The Flower Duet (From Lakmé) |
| M83 | Outro |
| Mac Miller | 2009 |
| Mac Miller | Come Back to Earth |
| Mad Season | River of Deceit |
| Mariah Carey | Without You |
| Mark Lowry | Mary, Did You Know? |
| Marty Robbins | Ribbon Of Darkness |
| Marvin Berry | Earth Angel (Will You Be Mine?) |
| Massive Attack | Dissolved Girl |
| Massive Attack | Teardrop |
| Massive Attack | Unfinished Sympathy - 2012 Mix/Master |
| Maurice Duruflé | Maurice Duruflé: Ubi caritas |
| Max Richter | On the Nature of Daylight |
| Mayer Hawthorne | All Better |
| Mazzy Star | Fade Into You |
| Mazzy Star | Into Dust |
| Meat Loaf | For Crying Out Loud |
| Metallica | Nothing Else Matters (Remastered) |
| Metallica | Turn The Page |
| Michael Jackson | Human Nature |
| Michael Jackson | Man in the Mirror - 2012 Remaster |
| Minnie Riperton | Les Fleurs |
| Minnie Riperton | Lovin' You |
| Miranda Lambert | If I Was a Cowboy |
| Moby | Porcelain |
| Mogwai | Mogwai Fear Satan |
| Molly Burch | Please Be Mine |
| Morcheeba | Who Can You Trust? |
| Morrissey | Everyday Is Like Sunday - 2011 Remaster |
| Natalia Lafourcade | El lugar correcto |
| Nicole Kidman | Come What May - From Moulin Rouge Soundtrack |
| Norman Connors | Love from the Sun |
| Prince | Nothing Compares 2 U (feat. Rosie Gaines) - Live |
| Pyotr Ilyich Tchaikovsky | Tchaikovsky: The Nutcracker, Op. 71, Act II: No. 13, Waltz of the Flowers |
| R.E.M. | Everybody Hurts |
| Radiohead | There, There |
| Radiohead | All I Need |
| Radiohead | Daydreaming |
| Radiohead | Decks Dark |
| Radiohead | Exit Music (For A Film) |
| Radiohead | Fake Plastic Trees |
| Radiohead | Faust Arp |
| Radiohead | How to Disappear Completely |
| Radiohead | Jigsaw Falling Into Place |
| Radiohead | Karma Police |
| Radiohead | Kid A |
| Radiohead | Let Down |
| Radiohead | Motion Picture Soundtrack |
| Radiohead | Nude |
| Radiohead | Pyramid Song |
| Radiohead | Reckoner |
| Radiohead | Sail To The Moon |
| Radiohead | Street Spirit (Fade Out) |
| Radiohead | The Tourist |
| Radiohead | Tinker Tailor Soldier Sailor Rich Man Poor Man Beggar Man Thief |
| Radiohead | True Love Waits |
| Rainbow | Catch The Rainbow |
| Ralph Vaughan Williams | The Lark Ascending |
| Ramin Djawadi | Light of the Seven |
| Ray Charles | Georgia on My Mind |
| Ray LaMontagne | Jolene |
| Ray Peterson | Tell Laura I Love Her |
| Red Hot Chili Peppers | Wet Sand |
| Regina Spektor | Fidelity |
| Roberta Flack | The First Time Ever I Saw Your Face |
| Rod Stewart | Maggie May |
| Ron Sexsmith | Gold In Them Hills |
| Roy Orbison | In Dreams |
| Sade | Pearls |
| Sam Brown | Stop |
| Sammy Davis Jr. | Till Then |
| Samuel Barber | Barber: Adagio for Strings |
| Sarah McLachlan | Angel |
| Sarah Vaughan | Misty |
| Savage Garden | Truly Madly Deeply |
| Seal | Kiss from a Rose |
| Selena | Dreaming Of You |
| Shawn Colvin | I Don't Know Why |
| Sia | Breathe Me |
| Sigur Rós | Flugufrelsarinn |
| Sigur Rós | Glósóli |
| Sigur Rós | Hoppípolla |
| Sigur Rós | Olsen olsen |
| Sigur Rós | Starálfur |
| Sigur Rós | Svefn-g-englar |
| Sigur Rós | Sæglópur |
| Sigur Rós | Untitled #3 - Samskeyti |
| Sigur Rós | Varúð |
| Silversun Pickups | Lazy Eye |
| Simon & Garfunkel | For Emily, Whenever I May Find Her - Live in St. Louis, MO - November 1969 |
| Simon & Garfunkel | Mrs. Robinson - From The Graduate Soundtrack |
| Simon & Garfunkel | Wednesday Morning, 3 A.M. |
| Simon & Garfunkel | America |
| Simon & Garfunkel | April Come She Will |
| Simon & Garfunkel | Bleecker Street |
| Simon & Garfunkel | Bridge Over Troubled Water |
| Simon & Garfunkel | Cecilia |
| Simon & Garfunkel | El Condor Pasa (If I Could) |
| Simon & Garfunkel | Flowers Never Bend with the Rainfall |
| Simon & Garfunkel | Homeward Bound |
| Simon & Garfunkel | I Am a Rock |
| Simon & Garfunkel | Kathy's Song |
| Simon & Garfunkel | Scarborough Fair / Canticle |
| Simon & Garfunkel | The 59th Street Bridge Song (Feelin' Groovy) |
| Simon & Garfunkel | The Boxer |
| Simon & Garfunkel | The Only Living Boy in New York |
| Simon & Garfunkel | The Sound of Silence - Acoustic Version |
| Simply Red | Holding Back the Years - 2008 Remaster |
| Sinéad O'Connor | Nothing Compares 2 U |
| Sinéad O'Connor | Troy |
| Sixpence None The Richer | Kiss Me |
| Sleeping At Last | Saturn |
| Snail's House | frostbite |
| Sneaker Pimps | Becoming X |
| Snow Patrol | Chasing Cars |
| Sophie B. Hawkins | As I Lay Me Down |
| Soundgarden | Black Hole Sun |
| Sounds Of Life | A Spice Of Jazz |
| St. Vincent | Strange Mercy |
| Steve Perry | Open Arms (Arr. for Guitar) |
| Stevie Nicks | Gold Dust Woman - Live |
| Stevie Ray Vaughan | Lenny |
| Stevie Wonder | Isn’t She Lovely |
| Sting | Fields Of Gold |
| Sting | It's Probably Me |
| Sting | Shape Of My Heart |
| Straylight Run | Existentialism On Prom Night |
| Sufjan Stevens | Casimir Pulaski Day |
| Sufjan Stevens | Mystery of Love (From the Original Motion Picture “Call Me by Your Name”) |
| Supertask | Healing |
| Sweet Sweet Loverboy | The Love Of My Life |
| TOOL | 10,000 Days (Wings Pt 2) |
| TOOL | Sober |
| TOOL | Wings For Marie (Pt 1) |
| TOTO | I'll Be Over You |
| Tash Sultana | Blackbird |
| Taylor Swift | Delicate |
| Taylor Swift | epiphany |
| Taylor Swift | invisible string |
| Tears For Fears | Mad World |
| Tenacious D | Fuck Her Gently |
| The Appleseed Cast | A Dream For Us |
| The Band | Atlantic City |
| The Band | When I Paint My Masterpiece - Remastered |
| The Beach Boys | Caroline, No - Mono |
| The Beach Boys | God Only Knows - Mono |
| The Beach Boys | Good Vibrations - Remastered 2001 |
| The Beach Boys | I Just Wasn't Made For These Times - Mono |
| The Beach Boys | I Know There's An Answer - Mono |
| The Beach Boys | Let's Go Away For A While - Mono |
| The Beach Boys | Pet Sounds - Mono |
| The Beach Boys | Sloop John B |
| The Beach Boys | Wouldn’t It Be Nice |
| The Beach Boys | You Still Believe In Me - Mono |
| The Beatles | Here, There And Everywhere - Remastered 2009 |
| The Beatles | Across The Universe - Remastered 2009 |
| The Beatles | All You Need Is Love - Remastered 2009 |
| The Beatles | Because - Remastered 2009 |
| The Beatles | Blackbird - Remastered 2009 |
| The Beatles | Carry That Weight - Remastered 2009 |
| The Beatles | Golden Slumbers - Remastered 2009 |
| The Beatles | Here Comes The Sun - Remastered 2009 |
| The Beatles | In My Life - Remastered 2009 |
| The Beatles | Julia - Remastered 2009 |
| The Beatles | Let It Be - Remastered 2009 |
| The Beatles | Revolution 9 - Remastered 2009 |
| The Beatles | Sgt. Pepper's Lonely Hearts Club Band - Remastered 2009 |
| The Beatles | She's Leaving Home - Remastered 2009 |
| The Beatles | Something - Remastered 2009 |
| The Beatles | The End - Remastered 2009 |
| The Beatles | The Long And Winding Road - Remastered 2009 |
| The Beatles | While My Guitar Gently Weeps - Remastered 2009 |
| The Beatles | Yesterday - Remastered 2009 |
| The Black Crowes | She Talks To Angels |
| The Cardigans | Lovefool |
| The Chicks | Landslide |
| The Chordettes | They Say It's Wonderful |
| The Cranberries | Dreams |
| The Cranberries | Linger |
| The Cranberries | Ode To My Family |
| The Cure | A Letter to Elise |
| The Cure | A Night like This - 2006 Remaster |
| The Cure | Close to Me - 2006 Remaster |
| The Cure | From the Edge of the Deep Green Sea |
| The Cure | In Between Days - 2006 Remaster |
| The Cure | Just like Heaven |
| The Cure | Lovesong - 2010 Remaster |
| The Cure | Lullaby - 2010 Remaster |
| The Cure | Pictures of You - 2010 Remaster |
| The Cure | Plainsong - 2010 Remaster |
| The Cure | The Lovecats |
| The Cure | The Same Deep Water as You - 2010 Remaster |
| The Cure | Underneath The Stars |
| The Cure | Untitled - 2010 Remaster |
| The Dream Academy | Life in a Northern Town |
| The Flaming Lips | Do You Realize?? |
| The Flamingos | I Only Have Eyes for You |
| The Foundations | Baby Now That I've Found You - Stereo |
| The Fray | How to Save a Life |
| The Goo Goo Dolls | Black Balloon |
| The Goo Goo Dolls | Iris |
| The Hollies | He Ain't Heavy, He's My Brother |
| The Killers | Shadowplay |
| The King's Singers | You are the new day |
| The La's | There She Goes |
| The Left Banke | Walk Away Renee |
| The Mamas & The Papas | Dream A Little Dream Of Me |
| The Moldy Peaches | Anyone Else But You |
| The Monkees | Riu Chiu |
| The Moody Blues | Nights In White Satin - Single Version / Mono |
| The Niro | No One Must Find You Here |
| The Paper Kites | Bloom - Bonus Track |
| The Penguins | Earth Angel (Will You Be Mine) |
| The Postal Service | Such Great Heights - Remastered |
| The Righteous Brothers | Unchained Melody |
| The Rolling Stones | She's A Rainbow |
| The Rolling Stones | Wild Horses - 2009 Mix |
| The Shins | New Slang - 2021 Remaster |
| The Smashing Pumpkins | 1979 - Remastered 2012 |
| The Smashing Pumpkins | Mellon Collie And The Infinite Sadness - Remastered 2012 |
| The Smiths | Please, Please, Please, Let Me Get What I Want - 2011 Remaster |
| The Smiths | Asleep |
| The Smiths | Stop Me If You Think You've Heard This One Before - 2011 Remaster |
| The Smiths | There Is a Light That Never Goes Out - 2011 Remaster |
| The Sundays | Here's Where The Story Ends |
| The Sundays | Wild Horses |
| The Sundays | You're Not The Only One I Know |
| The Tallest Man On Earth | Love is All |
| The Velvet Underground | Pale Blue Eyes |
| The Verve | The Drugs Don't Work |
| This Mortal Coil | Song To The Siren - Remastered |
| Thomas Newman | The Night Window |
| Tom Odell | Another Love |
| Tori Amos | A Sorta Fairytale |
| Tori Amos | Josephine |
| Tori Amos | Little Earthquakes - 2015 Remaster |
| Tori Amos | Pretty Good Year |
| Tori Amos | Putting the Damage On - 2016 Remaster |
| Tori Amos | Winter - 2015 Remaster |
| Tracy Chapman | Fast Car |
| U2 | One Tree Hill |
| U2 | Stuck In A Moment You Can't Get Out Of - Acoustic Version / Remastered 2020 |
| U2 | Where The Streets Have No Name - Remastered |
| VV | Heartful of Ghosts |
| Van Halen | (Oh) Pretty Woman - 2015 Remaster |
| Van Morrison | Astral Weeks - 1999 Remaster |
| Van Morrison | Into the Mystic - 2013 Remaster |
| Van Morrison | Someone Like You |
| Van Morrison | Sweet Thing - 1999 Remaster |
| Vertical Horizon | Best I Ever Had (Grey Sky Morning) |
| Vince Gill | Go Rest High On That Mountain |
| Virtual Riot | Never Let Me Go |
| Weyes Blood | Picture Me Better |
| When In Rome | The Promise |
| Whitney Houston | I Will Always Love You |
| Wolfgang Amadeus Mozart | Requiem in D minor, K.626: 3. Sequentia: Lacrimosa |
| Yazoo | Only You |
| Yazoo | Situation |
| Yazoo | Winter Kills |
| Yeah Yeah Yeahs | Maps |
| Yes | And You and I - 2003 Remaster |
| Yiruma | River Flows In You |
| Yusuf / Cat Stevens | Moonshadow - Remastered 2021 |
| Yusuf / Cat Stevens | Morning Has Broken - Remastered 2021 |
| Yusuf / Cat Stevens | The Wind - Remastered 2021 |
| Yusuf / Cat Stevens | Trouble |
| a-ha | Take On Me - MTV Unplugged |
| beabadoobee | Glue Song |
| bôa | Duvet |
| k.d. lang | Constant Craving |
| k.d. lang | Hallelujah |
| Édith Piaf | La Vie en rose |
