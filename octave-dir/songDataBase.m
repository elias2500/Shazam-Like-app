pkg load io

[status, output] = system('curl -X "GET" "https://api.spotify.com/v1/playlists/1YzHgIzS7D30Ex2gGEaNJC/tracks?market=ES&fields=items(track(name%2Cpreview_url%2Cartists(name)%2Calbum(images)))&limit=10&offset=19" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer BQAHk-OWcoxcGZN3QjgSVK_d4yetU6UhagMbO-cvV9YhGXOqxwsHRCTOpypEQt2XVapS2sVgf_R_HLEKfxI9Gp2gEV-GHoiPYemzzLSkotg82VFKtu5EbnDxEj1_NYWbNXq-AZSKGdajqPBMl_Y6pwDCUV5f0aPyCok"')

kkj = fromJSON(output)

for i = 1:10
  song_details(i) = kkj.items(i).track 
  artist_name(i) = getfield(song_details(i), {1}, 'artists', {1})
  prov_image_url(i) = getfield(song_details(i), {1}, 'album', {1})
endfor 
song_details = rmfield(song_details,'artists')
song_details = rmfield(song_details,'album')
for i = 1:10
  prov_image_url2(i) = getfield(prov_image_url(i),{1},'images',{1})
endfor

song_details1 = struct2cell(song_details)
artist_name1 = struct2cell(artist_name)
image_url = struct2cell(prov_image_url2)

cell2csv('song_title.txt',song_details1(1,1,:)(:),',')
cell2csv('preview_url.txt',song_details1(2,1,:)(:),',')
cell2csv('artist_name.txt',artist_name1(:,1,:)(:),',')
cell2csv('image_url.txt',image_url(2,1,:)(:),',')