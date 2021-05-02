# drop the videos you want to convert on THIS file

# configuration variables
ffmpeg="ffmpeg"
resolution="320x240"
frame_rate="15"

for file in "$@"; do
    "${ffmpeg}" -i "$file" -vcodec rawvideo -s $resolution -r $frame_rate -an "$file".avi
    "${ffmpeg}" -i "$file" -acodec pcm_s16le -vn "$file".wav
done;