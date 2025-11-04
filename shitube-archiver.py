import subprocess

print("shitube-archiver")
print("youtube fucking sucks. change my mind.\n")
print("URL:")
URLwaybackmachine = input()
subprocess.run(f'yt-dlp "{URLwaybackmachine}"', shell=True)
