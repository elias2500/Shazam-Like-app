function R = recordena();
  pkg load signal
  fs = 44100; # Sample frequency
  freq = 1000;
  tone = sin(2*pi*freq * (1:fs)/fs);
  disp('recording...');
  x = record(10, fs); # Record ten seconds from mic
  disp('done')
  R = findSong(x)