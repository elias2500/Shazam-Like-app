global HashTable HashTableCounts 
pkg load io
disp("Loading...");
HashTable = dlmread('hashes.csv',",");
HashTableCounts = dlmread('hashescounts.csv',",");

disp("Done!");