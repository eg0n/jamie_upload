Overview
========
You should be able to download ia using a browser. Directions [here](https://archive.org/services/docs/api/internetarchive/cli.html) say that all you need is a python installation.

Once you have that, configure your credentials with 

    $ ia configure

Then create a CSV file (Excel should work) with the columns below, one row per file. (The first row should be the column names.) Once you have that set up, you can run

    $ ia upload --spreadsheet=upload.csv

Once that's done, you can get a list of URLs to the newly-created VBR MP3 files by running

    $ python get_urls.py

That script assumes that your CSV is called 'upload.csv'. You can edit the script to change the file name if you need to.

Notes
=====
I created a test using a public domain mp3:
https://archive.org/details/adamtest_abwreck

Here's how the csv seems to map to things on the website:

  * creator - TMS Mashups
  * title - Shows up on your user page with this text in big lettering
  * subject - Shows up under "Topics". It looks like you just set this to the same thing as title
  * mediatype - audio
  * collection - opensource_audio
  * uploader - your e-mail
  * identifier - This has to be a unique string across the archive. It looks like you smush the title together
  * description - Whatever you want, shows up underneath 'topic' on the item detail page
  * file - relative path to the file to upload

There's other metadata here:
https://archive.org/services/docs/api/metadata-schema/

So if you want to add some coverart, for example, then you'll need to set more stuff in the CSV.
