# CA-Project-FaceBook-scraping
How to capture Friends and Friends Friends on FB and get their profil photo and guest their age and gender with AWS Rekongnition
Readme_FaceBook_scraping

3 codes:

1.	FB friend final no loop.py : gets all the friends of someone in Facebook (here julie.fievez) and puts them in a CSV file: name_of_FB_profil.csv (here julie.fievez.csv)

2.	FB_Img_URL_extrac_AKA_loop.py : reads the 1st CSV file, gets URL the profile photo and adds them and puts them in a second CSV file: name_of_FB_profil2.csv (here julie.fievez2.csv)

3.	RekonFB_AKA_final.py : reads the second CSV, gets the estimation of the age and gender of the friends and adds them and puts them in a third CSV file : name_of_FB_profil3.csv (here julie.fievez3.csv)

Limits:
•	I use an FB account that I create here .......@gmail.com with pw "……….". I should get back this account
•	We should add a loop in program 1 to get the friends of the friends to have all the FB graph. But we should put a limit to the graph size
•	In program 1 root of the graph is 'https://www.facebook.com/julie.fievez/'. It is possible to choose any other root
•	In program 2 the limit of number photos was set to 50. That can be changed to any number.
