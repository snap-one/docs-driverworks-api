
## Overview

The examples used in the Albums section of this document will reference the following albums:

```lua
mediaId1 = C4:MediaAddAlbumInfo("http://127.0.0.1/music/Album1", "Funky Music", Album1)

songLocation1="http://127.0.0.1/music/song1.mp3"
songLocation2="http://127.0.0.1/music/song2.mp3"
songLocation3="http://127.0.0.1/music/song3.mp3"

SomeSong1 = {
--required fields
="Title Test Song Number 1",
location=songLocation1,
track_no="6",
--optional fields
name = "Name Test Song Number 1",
artist = "C4 Music Factory",
record_label="Island",
release_date="15 Jun 2004",
}

SomeSong2 = {
title="Test Song Number 2",
location=songLocation2,
track_no="1",
name = "Name Test Song Number 2",
artist = "C4 Music Factory",
record_label="Dos Record Label",
release_date="15 Jun 2222",
}

SomeSong3 = {
title="Test Song Number 3",
track_no="7",
location=songLocation3,
name = "Name Test Song Number 3",
artist = "C4 Music Factory",
record_label="Boat",
release_date="3 Dec 2002",
}

Album1 = {
artist = "Jimmy Joe",
description = "Worst episode ever",
genre = "Blues & Browns",
release_date = "1992",
release_label = "Grass and Cash",
songs = {SomeSong1, SomeSong2, SomeSong3}, 
}
```
