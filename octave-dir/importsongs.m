% function x = importsongs();

 p=dir('*.mp3');
 for i = 1:numel(p):
   A=dlmread(p(i).name);
 endfor
