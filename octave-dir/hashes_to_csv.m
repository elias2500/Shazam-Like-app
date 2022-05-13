global HashTable HashTableCounts

#loading songs with myls
s1 = myls(['/home/jonwicked/Downloads/Karudis/fingerprint_prototype/python/marcos_g-never_fall_in_love_with_strangers.mp3']);
s2 = myls(['/home/jonwicked/Downloads/Karudis/fingerprint_prototype/python/ASTN-Butterflies.mp3']);
s3 = myls(['/home/jonwicked/Downloads/Karudis/fingerprint_prototype/python/CHIKA-FWB.mp3']);
s4 = myls(['/home/jonwicked/Downloads/Karudis/fingerprint_prototype/python/Charlie_Puth-The_Way_I_Am.mp3']);
s5 =  myls(['/home/jonwicked/Downloads/Karudis/fingerprint_prototype/python/Charlie_Puth-Attention.mp3']);
s6 = myls(['/home/jonwicked/Downloads/Karudis/fingerprint_prototype/python/Charlie_Puth-Cheating_on_You.mp3']);
s7 = myls(['/home/jonwicked/Downloads/Karudis/fingerprint_prototype/python/Charlie_Puth-We_Dont_Talk_Anymore_feat._Selena_Gomez.mp3']);
s8 = myls(['/home/jonwicked/Downloads/Karudis/fingerprint_prototype/python/Wiz_Khalifa-See_You_Again_feat._Charlie_Puth.mp3']);
s9 = myls(['/home/jonwicked/Downloads/Karudis/fingerprint_prototype/python/Valntn-Mona_Lisa.mp3']);
s10 = myls(['/home/jonwicked/Downloads/Karudis/fingerprint_prototype/python/Audrey_Mika-Just_Friends.mp3']);

#adding all songs to table
table =[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]

#calling add_tracks so we can get the HashTable and HashTableCounts for each song
[N,T] = add_tracks(table);

#writing HashTable and HashTableCounts to .csv files
dlmwrite('hashes.csv',HashTable,','); 
dlmwrite('hashescounts.csv',HashTableCounts, ','); 



