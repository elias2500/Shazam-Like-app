function R = findSong(x);
%To line 7: A small workarround needed because the output of the recording function
%is in .wav form and .mp3 is needed for matching
audiowrite('test.wav',x,44100);
[y,fs] = audioread('test.wav');
mp3write(y, fs, 'sample');
[dt,srt] = mp3read('sample.mp3');
%Calling the function that matches the recorded song to one from the database
R = match_query(dt,srt);