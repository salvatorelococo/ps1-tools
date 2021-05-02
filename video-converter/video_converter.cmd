@REM drop the videos you want to convert on THIS file

@REM configuration variables

@REM Add the ffmpeg\bin folder to your system environment variable PATH
@REM or
@REM Set your ffmpeg\bin\ffmpeg.exe file path instead of ffmpeg (ES: @SET ffmpeg=C:\ffmpeg\bin\ffmpeg.exe)
@SET ffmpeg=ffmpeg
@SET resolution=320x240
@SET frame_rate=15

FOR %%g IN (%*) DO (
	%ffmpeg% -i %%g -vcodec rawvideo -s %resolution% -r %frame_rate% -an %%g.avi
	%ffmpeg% -i %%g -acodec pcm_s16le -vn %%g.wav
)

@PAUSE