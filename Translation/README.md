# Panda Touch UI Translation

This page is specifically for users looking to assist with translation into different languages. If you are looking for different languages to use with your Panda Touch UI then please look for the relevant IMG file (each IMG contains a different language).

If you would like to help by translating the Panda Touch UI into your native language then please follow the steps below:

1. Create a fork of this repo.
2. Create your own branch on your fork.
3. Check your branch out locally.
4. Add this repo as an upstream source for your fork.
5. Create a new folder within this folder that uses the naming format "<2 char language ISO code>-<2 char country ISO code>".

- You can find the two character language ISO code on this wikipedia page under the 'Set 1' column: https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
- You can find the two character country ISO code on this wikipedia page under the 'Set 1' column: https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes
- If your language is not country specific then don't worry about adding a country code. Languages like English have variations in spelling and grammar between UK and US variants and in such cases, a country code would be useful.

6. Use the en-GB file as the master file and then translate the phrases contained therein into your local language.
7. Change the first level key within the yml file to reflect the language and country code that you have translated into. For example, en-GB becomes en-US in the sample file.
8. Ensure that your translated file is named according to your language and country code (use country code only if applicable).
9. If you have any questions about the original meaning of a phrase then please post them here: https://github.com/bigtreetech/PandaTouch/issues/82
10. Once the translation is complete, commit your changes to your fork and then create a PR to this repo.

If you struggle to use the git forking workflow but would still like to contribute a translation then please feel free to attach your translation to a comment in this thread: https://github.com/bigtreetech/PandaTouch/issues/82

As we make product updates, it is likely that more fields will become available for translation. Those fields will appear as English in the updated files until they receive a translation update.

Thanks to all those who contribute translations.
